
import requests, datetime


def currency_rates_adv(code: str) -> tuple:
    """возвращает курс валюты `code` по отношению к рублю в формате float и дату в формате datetime.date"""
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    if r['Valute'].get(code.upper()) == None:
        result_value = None
    else:
        dt = r['Date']
        result_value = r['Valute'].get(code.upper())['Value'], datetime.date(int(dt[:4]), int(dt[5:7]), int(dt[8:10]))
    return result_value


kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)


