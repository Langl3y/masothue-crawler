from pyquery import PyQuery as pq
from parser import parse_company
from get_html import get_html


def scrape_companies(url):
    html_string = get_html(url)
    document = pq(html_string)
    tax_listing = document('.tax-listing>div')

    company_list = []

    for tax_info in tax_listing:
        company = parse_company(tax_info)
        company_list.append(company)

    return company_list
