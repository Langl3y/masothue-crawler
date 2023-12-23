from scraper import scrape_companies


def main():
    for i in range(1, 20):
        url = f'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/hai-duong-147?page={i}'
        company_list = scrape_companies(url)
        print(company_list)


if __name__ == '__main__':
    main()