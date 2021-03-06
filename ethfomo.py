#!/usr/bin/python3

import ts3
import datetime
from urllib.request import urlopen
import json
import math
import time
from twitter import *
from telegram import *
import telegram
from num2words import num2words

url = "https://poloniex.com/public?command=returnTicker"
page = urlopen(url)
data=page.read()
decodedata=json.loads(data.decode())
lastprice=round(float(decodedata['BTC_ETH']['last']),5)
f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/lasteth.txt', encoding='utf-8')
priorprice = f.readline().strip()
f.close()

f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/lasteth.txt', 'w+', encoding='utf-8')
f.write(str(lastprice))
f.close()

ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
pricediff = round(float(lastprice) - float(priorprice),5)
pricediff2 = abs(pricediff)
pricedifffrac = abs(pricediff) / float(priorprice)
pricediffperc = str(round(pricedifffrac*100,2))
f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/ethfomologs.txt', 'a', encoding='utf-8')
f.write(str(ts) + " - " + str(lastprice) + " - " + pricediffperc + "\n")
f.close()
if pricediff < 0:
	direction = "down"
else:
	direction = "up"
if float(pricedifffperc) > 2: 
	fomotg = "ALERT: HARD-FORK VITALIUM is FOMO'ing " + direction + " by " + str(pricediff2) + " BTC (" + pricediffperc + "%) to " + str(lastprice) + " BTC in the past 5 minutes"

	f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/etcfomologs.txt', 'a', encoding='utf-8')
	f.write(str(ts) + " - " + str(lastprice) + "ALERT: HARD-FORK VITALIUM is FOMO'ing [b]" + direction + "[/b] by " + pricediffperc + "% to [b] in the past 5 minutes\n")
	f.close()
	token=''
	bot=telegram.Bot(token=token)
	bot.sendMessage(chat_id="@ethclassic", text=fomotg)

	time.sleep(3)
	with ts3.query.TS3Connection("158.69.115.146", 2009) as ts3conn:
		try:
			ts3conn.login(
			client_login_name="",
			client_login_password=""
			)
		except ts3.query.TS3QueryError as err:
			print("Login failed:", err.resp.error["msg"])
			exit(1)
			#print(whalecallsupdate)
		ts3conn.use(sid=778)
		ts3conn.clientupdate(client_nickname="[FOMO-Bot]")
		#ts3conn.clientgetids(cluid="aS/5fz/mt08I1cY+UUvoALi7xOU=")
		#botid=ts3conn.last_resp.parsed[0]['clid']
	
		if "down" in direction:
			fomots = "ALERT: [color=red][b]HARD-FORK VITALIUM[/b][/color] is FOMO'ing [color=red][b]" + direction + "[/b][/color] by [color=red][b]" + str(pricediff2) + " BTC[/b][/color](" + pricediffperc + "%) to [color=red][b]" + str(lastprice) + " BTC[/b][/color] in the past 5 minutes"
		if "up" in direction:
			fomots = "ALERT: [color=green][b]HARD-FORK VITALIUM[/b][/color] is FOMO'ing [color=green][b]" + direction + "[/b][/color] by [color=green][b]" + str(pricediff2) + " BTC[/b][/color](" + pricediffperc + "%) to [color=green][b]" + str(lastprice) + " BTC[/b][/color] in the past 5 minutes"
		ts3conn.sendtextmessage(targetmode=2, target=1, msg=fomots)
		time.sleep(3)	
		resp = ts3conn.whoami()
		client_id=resp[0]['client_id']
		ts3conn.clientmove(cid=44184, clid=client_id)
		ts3conn.sendtextmessage(targetmode=2, target=1, msg=fomots)	
		ts3conn.clientmove(cid=56600, clid=client_id)
		ts3conn.sendtextmessage(targetmode=2, target=1, msg=fomots)
		time.sleep(7)	
		#ts3conn.sendtextmessage(targetmode=1, target=botid, msg="!say \"CHOY-NAH is foe-mowing " + direction + " by " + str(num2words(float(pricediffperc))) + " percent. Check your PNL\"")		
		ts3conn.quit()
		
