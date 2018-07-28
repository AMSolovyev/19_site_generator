import json
import argparse
from jinja2 import Environment, FileSystemLoader
from os import makedirs
from jinja2_markdown import MarkdownExtension
from os.path import basename, splitext, join, exists, dirname


dir_input = 'articles'
dir_output = 'public'
dir_templates = 'templates'

env_template = Environment(
    loader=FileSystemLoader(dir_templates),
    extensions=['jinja2_markdown.MarkdownExtension'])


def get_md_content(source_file):
    file_path = join(dir_input, source_file)
    with open(file_path, 'r') as file_handler:
        return file_handler.read()


def create_static_page(article):
    static_page = env_template.get_template('page.html')
    new_path = join(dir_output, article['destiny'])
    if not exists(dirname(new_path)):
        makedirs(dirname(new_path))

    with open(new_path, 'w') as file_handler:
        file_handler.write(static_page.render(
            title_page=article['title'],
            content=get_md_content(article['source'])))


def create_index_page(topics):
    index_page = env_template.get_template('index.html')
    with open(join(dir_output, 'index.html'), 'w') as file_handler:
        file_handler.write(index_page.render(
            title_page='Генератор сайтов',
            topics=topics))


def get_articles_list(topic, json_data):
    articles = json_data['articles']
    for article in articles:
        if article['topic'] == topic:
            dest_name = splitext(basename(article['source']))[0]
            article['destiny'] = join(topic, dest_name+'.html')
            create_static_page(article)
            yield article


def generate_static_pages(json_data):
    topics = json_data['topics'].copy()
    for topic in topics:
        topic['articles'] = []
        for article in get_articles_list(topic['slug'], json_data):
            topic['articles'].append(article)
    create_index_page(topics)


def load_config(file_path):
    with open(file_path) as file_handle:
        json_data = json.load(file_handle)
        generate_static_pages(json_data)


if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument(
        'config_file',
        help="Json config file"
    )
    args = aparser.parse_args()
    load_config(args.config_file)
