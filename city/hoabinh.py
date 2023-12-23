from data_processing.scraper import scrape_companies
from data_processing.database import insert_data


def hoabinh_crawler():
    for i in range(1, 20):
        url = f'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/hoa-binh-786?page={i}'
        company_list = scrape_companies(url)
        print(company_list)

        insert_data(company_list, "hoabinh")


if __name__ == '__main__':
    hoabinh_crawler()
