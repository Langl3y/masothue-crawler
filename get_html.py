import requests
from fake_useragent import UserAgent
import time
import random as rd


def get_html(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    sleep_period = rd.uniform(1, 3)
    time.sleep(sleep_period)
    response = requests.get(url, headers=headers)
    html_string = response.content.decode('utf-8')

    return html_string
