import requests
from lxml.html import HtmlElement
from pyquery import PyQuery as pq
import mysql.connector

url_tinh_thanh = 'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

html_string = requests.get(url_tinh_thanh, headers=headers).content.decode('utf-8')

document = pq(html_string)

daknong = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/dak-nong-245"]')
dienbien = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/dien-bien-1007"]')
dongnai = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/dong-nai-57"]')
dongthao = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/dong-thap-63"]')
gialai = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/gia-lai-563"]')
hagiang = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/ha-giang-529"]')
hanam = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/ha-nam-162"]')
hanoi = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/ha-noi-7"]')
hatinh = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/ha-tinh-342"]')
haiduong = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/hai-duong-147"]')
haiphong = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/hai-phong-99"]')
haugiang = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/hau-giang-190"]')
hochiminh = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/ho-chi-minh-23"]')
hoabinh = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/hoa-binh-786"]')
hungyen = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/hung-yen-123"]')
khanhhoa = document('a[href="/tra-cuu-ma-so-thue-theo-tinh/khanh-hoa-26"]')


cities = [daknong, dienbien, dongnai, gialai, hagiang, hanam, hanoi, hatinh, haiduong, haiphong, haugiang, hochiminh, hoabinh, hungyen, khanhhoa]


connection = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    database='crawled_data',
    port=3306
)


for city in cities:
    endpoint = city.attr('href')
    endpoint = endpoint.split('tra-cuu-ma-so-thue-theo-tinh/')[1]

    url_city = url_tinh_thanh + endpoint

    html_string = requests.get(url_city).content.decode('utf-8')

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

    cursor = connection.cursor()

    for json_data in company_list:
        company_name = json_data['company_name']
        company_id = json_data['company_id']
        company_owner = json_data['company_owner']
        company_address = json_data['company_address']

        # NHAP DATA VAO MYSQL
        insert_query = "INSERT INTO companies (company_name, company_id, company_owner, company_address) VALUES (%s, %s, %s, %s)"
        values = (company_name, company_id, company_owner, company_address)
        cursor.execute(insert_query, values)

    connection.commit()


cursor.close()
connection.close()