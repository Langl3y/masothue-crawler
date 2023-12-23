from data_processing.scraper import scrape_companies
from data_processing.database import insert_data


def haugiang_crawler():
    for i in range(1, 20):
        url = f'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/hau-giang-190?page={i}'
        company_list = scrape_companies(url)
        print(company_list)

        insert_data(company_list, "haugiang")


if __name__ == '__main__':
    haugiang_crawler()