#!/usr/bin/python3
#currency exchange tracking application.
from requests import get

PRIVATBANKURL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
TRADEUAURL = 'https://btc-trade.com.ua/api/ticker'

PRIVATBANK_COURSES = get(PRIVATBANKURL).json()
TRADEUA_COURSES = get(TRADEUAURL).json()

USD = float(PRIVATBANK_COURSES[0]['buy'])
EUR = float(PRIVATBANK_COURSES[1]['buy'])
RUB = float(PRIVATBANK_COURSES[2]['buy'])
BTC_BUY = float(TRADEUA_COURSES['btc_uah']['buy']); BTC_SELL = float(TRADEUA_COURSES['btc_uah']['sell'])
ETH_BUY = float(TRADEUA_COURSES['eth_uah']['buy']); ETH_SELL = float(TRADEUA_COURSES['etc_uah']['sell'])

print(
'''-------------------------
USD = {USD} UAH
EUR = {EUR} UAH
RUB = {RUB} UAH

BTC = {BTC_BUY} UAH #buy
ETH = {ETH_BUY} UAH #buy

BTC = {BTC_SELL} UAH #sell
ETH = {ETH_SELL} UAH #sell
-------------------------'''.format(USD=USD,EUR=EUR,RUB=RUB,BTC_BUY=BTC_BUY, BTC_SELL=BTC_SELL, ETH_BUY=ETH_BUY, ETH_SELL=ETH_SELL))
input('\nPress ENTER to continue. . .')