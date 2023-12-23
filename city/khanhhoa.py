from scraper import scrape_companies
from database import insert_data


def main():
    for i in range(1, 20):
        url = f'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/khanh-hoa-26?page={i}'
        company_list = scrape_companies(url)
        print(company_list)

        insert_data(company_list)


if __name__ == '__main__':
    main()
