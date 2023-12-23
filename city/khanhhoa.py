from data_processing.scraper import scrape_companies
from data_processing.database import insert_data


def khanhhoa_crawler():
    for i in range(1, 20):
        url = f'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/khanh-hoa-26?page={i}'
        company_list = scrape_companies(url)
        print(company_list)

        insert_data(company_list, "khanhhoa")


if __name__ == '__main__':
    khanhhoa_crawler()