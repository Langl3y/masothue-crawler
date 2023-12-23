from scraper import scrape_companies
from database import insert_data


def main():
    for i in range(1, 20):
        url = f'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/dien-bien-1007?page={i}'
        company_list = scrape_companies(url)
        print(company_list)

        insert_data(company_list)


if __name__ == '__main__':
    main()