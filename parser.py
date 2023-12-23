from lxml.html import HtmlElement
from pyquery import PyQuery as pq


def parse_company(el: HtmlElement):
    company_element = pq(el)
    return {
        'company_name': company_element('div>h3>a').text(),
        'company_id': company_element('div>a').text(),
        'company_owner': company_element('div>em>a').text(),
        'company_address': company_element('address').text(),
    }