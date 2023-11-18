import codecs
import os, sys

from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping.settings"

import django

django.setup()

from scraping_app.parser import *
from scraping_app.models import Vacancy, City, Language

parser = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
    (rabota,
     'https://www.rabota.ru/vacancy/?query=python&location.ll=55.75396,37.620393&location.kind=region&location.radius=any&location.regionId=3&location.name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&sort=relevance')
)

city = City.objects.filter(slug='moskva').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parser:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
