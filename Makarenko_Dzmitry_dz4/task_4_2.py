
import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    if r['Valute'].get(code.upper()) == None:
        result_value = None
    else:
        result_value = (r['Valute'].get(code.upper())['Value'], r['Date'])

    return result_value


print(currency_rates("eur"))
print(currency_rates("noname"))


