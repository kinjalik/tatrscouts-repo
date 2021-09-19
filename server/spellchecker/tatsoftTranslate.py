import re
from urllib.parse import quote
import urllib.request
import json


def rus_to_tat(query):
    fin_text = ""
    query = urllib.parse.quote_plus(query)
    url = "http://byhackathon.translate.tatar/translate?lang=0&text=" + query
    # fin_text+=(url)

    hdr = {"Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}

    req = urllib.request.Request(url, headers=hdr)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    if result[0] == '<':
        result = (result.splitlines()[-1])
        fin=""
        beg=False
        result=result[2:]
        for i in result:
            if i=="<":
                break
            if beg:
                fin+=i
            if i==">":
                beg=True
        result=fin
    return result


def tat_to_rus(query):
    fin_text = ""
    query = urllib.parse.quote_plus(query)
    url = "http://byhackathon.translate.tatar/translate?lang=1&text=" + query
    # fin_text+=(url)

    hdr = {"Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}

    req = urllib.request.Request(url, headers=hdr)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    if result[0] == '<':
        result = (result.splitlines()[-1])
        fin = ""
        beg = False
        result = result[2:]
        for i in result:
            if i == "<":
                break
            if beg:
                fin += i
            if i == ">":
                beg = True
        result = fin
    return result
