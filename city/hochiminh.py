import requests
from lxml.html import HtmlElement
from pyquery import PyQuery as pq
from fake_useragent import UserAgent

ua = UserAgent()

url = 'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/ho-chi-minh-23'

headers = {"User Agent": ua.random}

html_string = requests.get(url).content.decode('utf-8')

document = pq(html_string)

tax_listing = document('.tax-listing>div')


def parse_company(el: HtmlElement):
    company_element = pq(el)

    return {
        'company_name': company_element('div>h3>a').text(),
        'company_id': company_element('div>a').text(),
        'company_owner': company_element('div>em>a').text(),
        'company_address': company_element('address').text(),
    }


company_list = []

for tax_info in tax_listing:
    company = parse_company(tax_info)

    company_list.append(company)

print(company_list)
