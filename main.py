#!/usr/bin/python3
#currency exchange tracking application.
from requests import get

PRIVATBANKURL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
TRADEUAURL = 'https://btc-trade.com.ua/api/ticker'

PRIVATBANK_COURSES = get(PRIVATBANKURL).json()
TRADEUA_COURSES = get(TRADEUAURL).json()

USD = PRIVATBANK_COURSES[0]['buy']
EUR = PRIVATBANK_COURSES[1]['buy']
RUB = PRIVATBANK_COURSES[2]['buy']
BTC_BUY = TRADEUA_COURSES['btc_uah']['buy']
ETH_BUY = TRADEUA_COURSES['eth_uah']['buy']

COURSES = (USD, EUR, RUB, BTC_BUY, ETH_BUY)

if __name__ == "__main__":
    SEPLINE = ("-" * 29) + "\n"
    print(SEPLINE + 'USD = {0} UAH\nEUR = {1} UAH\nRUB = {2} UAH\nBTC = {3} UAH\nETH = {4} UAH'.format(*COURSES))
    input('\nPress ENTER to continue. . .')
