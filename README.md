# Encyclopedia

The ```manage_site.py``` generates static files from configs. The ```manage_site.py``` convertes articles from markdown into html.
All results are collected in the ```public``` folder.

There are the files in the folders:
- ```articles``` - static files (basic);
- ```templates``` - the static pages generation template, `layout.html`, `index.html`, `page.html`;
- ```public``` - results

[The result](http://AMSolovyev.github.io/19_site_generator/public/index.html)

# How to use

```
1. virtualenv -p python3 env
2. source env/bin/activate
3. pip install -r requirements.txt
4. python manage_site.py /home/solo/git/19_site_generator/config.json
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
