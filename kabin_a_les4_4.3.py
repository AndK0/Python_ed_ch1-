from datetime import date
from requests import get, utils

answer = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def list_of_currency(num_code):
    data = answer.split("Valute ID=")
    d, m, y = data[0].split('"')[-4].split(".")

    for i in data:
        if num_code.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(list_of_currency(input("write a currency ")))
print(list_of_currency(input("write a currency ")))
