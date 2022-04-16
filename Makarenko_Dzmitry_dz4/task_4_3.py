
import requests
import datetime


def currency_rates_adv(code: str):
    """возвращает курс валюты `code` по отношению к рублю"""
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    if r['Valute'].get(code.upper()) == None:
        result_value = None
    else:
        dt = r['Date']
        result_value = (r['Valute'].get(code.upper())['Value'], datetime.date(int(dt[:4]), int(dt[5:7]), int(dt[8:10])))

    return result_value


print(currency_rates_adv("eur"))
print(currency_rates_adv("noname"))


