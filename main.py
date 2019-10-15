import requests
import argparse
import sys
import os
from dotenv import load_dotenv




def shorten_link(token, url):
    long_token = "{0} {1}".format("Bearer", token)
    headers = {"Authorization": long_token}
    body = {"long_url": url}
    host = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(host, headers=headers, json=body)
    if response.status_code == 200:
        a = 0
    elif response.status_code == 201:
        a = 0
    else:
        return None
    return response.json()["id"]


def count_clicks(token, link):
    long_token = "{0} {1}".format("Bearer", token)
    headers = {"Authorization": long_token}
    payload = {"unit": "day", "units": "-1"}
    host = "{0}{1}{2}".format("https://api-ssl.bitly.com/v4/bitlinks/", link, "/clicks/summary")
    response = requests.get(host, headers=headers, params=payload)
    if response.status_code == 200:
        a = 0
    elif response.status_code == 201:
        a = 0
    else:
        return None
    return response.json()["total_clicks"]


def main():
    parser = argparse.ArgumentParser(description='Программа определяет короткую ссылку или считает колво кликов по короткой ссылке')
    parser.add_argument('ref', help='Введите ссылку : ')
    args = parser.parse_args()
    url = args.ref

    token = os.getenv("TOKEN_BIT_LY")
    try:
        if url.startswith("http") :
            short_ref = shorten_link(token, url)
            print('Битлинк', short_ref)
        else:
            number_clics_ref = count_clicks(token, url)
            print('Число кликов = ', number_clics_ref)

    except requests.exceptions.HTTPError:
        print("Все остановили.Ошибочная ссылка =  ", url)


if __name__ == '__main__':
    load_dotenv()
    main()