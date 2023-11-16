import requests
import codecs
from  bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('work', 'rabota')

headers = [{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0)'
                         ' Gecko/20100101 Firefox/120.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           },
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           },
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                           'Version/17.1 Safari/605.1.15',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           },
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }

]




def work(url):
    jobs = []
    errors = []
    url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers[randint(0,3)])
    domain = 'https://www.work.ua'
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='pjax-job-list')
        div_list = main_div.find_all('div', attrs={'class': 'job-link'})
        if main_div:
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                content = div.p.text
                company = 'Без названия'
                logo = div.find('img')
                if logo:
                    company = logo['alt']

                jobs.append({'title': title.text, 'url': domain + href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exist'})
    else:
        errors.append({'url': url, 'title': 'Page not found'})

    return jobs, errors

def rabota(url):
    jobs = []
    errors = []
    resp = requests.get(url, headers=headers[randint(0,3)])
    domain = 'https://www.rabota.ru'
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'r-serp__infinity-list'})
        article_list = main_div.find_all('article', attrs={'class': 'r-serp__item_vacancy'})

        if main_div:
            for art in article_list:
                div_pointer = art.find('div', attrs={'class': 'vacancy-preview-card__wrapper_pointer'})
                div_card__top = div_pointer.find('div', attrs={'class': 'vacancy-preview-card__top'})
                div_card__content = div_card__top.find('div', attrs={'class': 'vacancy-preview-card__content-wrapper'})
                header = div_card__content.find('header', attrs={'class': 'vacancy-preview-card__header'})
                h3 = header.find('h3', attrs={'class': 'vacancy-preview-card__title'})
                title = h3.a.text
                #href = title.a['href']
                #content = div.p.text
                #company = 'Без названия'
                #logo = div.find('img')
                #if logo:
                #   company = logo['alt']

                jobs.append({'title': title})
        else:
            errors.append({'url': url, 'title': 'Div does not exist'})
    else:
        errors.append({'url': url, 'title': 'Page not found'})

    return jobs

if __name__ == '__main__':
    url = 'https://www.rabota.ru/vacancy/?query=python&location.ll=55.75396,37.620393&location.kind=region&location.radius=any&location.regionId=3&location.name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&sort=relevance'
    jobs = rabota(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
