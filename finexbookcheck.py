#!/usr/bin/python3

import ts3
import datetime
from urllib.request import urlopen
import json
import math
import time
from twitter import *
from num2words import num2words

url = "https://api.bitfinex.com/v1/book/btcusd?&limit_asks=100&limit_bids=100"
page = urlopen(url)
data=page.read()
decodedata=json.loads(data.decode())
finexasks=decodedata['asks']
finexbids=decodedata['bids']

ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/lastfinexorder.txt', encoding='utf-8')
lastbfxorder = f.readline().strip()
f.close()
f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/finexbooklogs.txt', 'a', encoding='utf-8')
f.write(str(ts) + " - Book fetched \n")
f.close()
for ask in finexasks:
	askorder = round(float(ask['amount']))
	if askorder > 0.95*round(float(lastbfxorder)) and askorder < 1.05*round(float(lastbfxorder)):
		continue
	if askorder > 1000:
		f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/finexbooklogs.txt', 'a', encoding='utf-8')
		f.write(str(ts) + "ALERT: FINEX has a [b]ASK[/b] order of [b]" + str(askorder) + "BTC[/b]  in the book at [b]" + str(ask['price']) + "\n")
		f.close()
		t = Twitter(auth=OAuth('', '', '', ''))

		t.statuses.update(status="NOTE: FINEX has a ASK order of " + str(askorder) + " BTC in the book at " + str(ask['price']) + " USD")
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
			ts3conn.clientupdate(client_nickname="[OrderBook-BOT]")
			resp = ts3conn.whoami()
			client_id=resp[0]['client_id']
			#ts3conn.clientgetids(cluid="aS/5fz/mt08I1cY+UUvoALi7xOU=")
			#botid=ts3conn.last_resp.parsed[0]['clid']
			ts3conn.sendtextmessage(targetmode=2, target=1, msg="NOTE: [b]FINEX[/b] has a [b]ASK[/b] order of [b]" + str(askorder) + " BTC[/b] in the book at [b]" + str(ask['price']) + " USD")	
			ts3conn.clientmove(cid=44184, clid=client_id)
			ts3conn.sendtextmessage(targetmode=2, target=1, msg="NOTE: [b]FINEX[/b] has a [b]ASK[/b] order of [b]" + str(askorder) + " BTC[/b]  in the book at [b]" + str(ask['price']) + " USD")	
			f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/lastfinexorder.txt', 'w+', encoding='utf-8')
			f.write(str(askorder))
			f.close()
			#ts3conn.sendtextmessage(targetmode=1, target=botid, msg="!yt [URL]http://austeritysucks.com/orderwall.mp3[/URL]")
			time.sleep(4)
			#ts3conn.sendtextmessage(targetmode=1, target=botid, msg="!say \"Finn-ex ASK WALL " + str(num2words(askorder)) + " BTC\"")		
			ts3conn.quit()

		#ts3conn.sendtextmessage(targetmode=2, target=1, msg="!say \"Bot permission Alert test\" en")		
time.sleep(5)
for bid in finexbids:
	bidorder = round(float(bid['amount']))
	if bidorder > 0.95*round(float(lastbfxorder)) and bidorder < 1.05*round(float(lastbfxorder)):
		continue
	if bidorder > 1000:
		f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/finexbooklogs.txt', 'a', encoding='utf-8')
		f.write(str(ts) + "ALERT: FINEX has a [b]BID[/b] order of [b]" + str(bidorder) + "[/b] in the book at [b]" + str(bid['price']) + "\n")
		f.close()
		t = Twitter(auth=OAuth('4873475789-ZqmODHIJvdAewASdoBu1VkZ8iq9tnyVWAIcYVfE', 'Gd1zyaHTOAw8n3MX6fny8BHGTiHzMHdBKiU4RKPosKD5d', 'akB27TrZAD2Oa4L3gelsRVTTq', 'PmPWrlY6ZcwRDkAIhxT1KzzJc6Y59q7voSE9xUv1Anc5619Vlq'))
		t.statuses.update(status="NOTE: FINEX has a BID order of " + str(bidorder) + " BTC in the book at " + str(bid['price']) + " USD")	
		with ts3.query.TS3Connection("158.69.115.146", 2009) as ts3conn:
			try:
				ts3conn.login(
				client_login_name="botking",
				client_login_password="aQziiUPY"
				)
			except ts3.query.TS3QueryError as err:
				print("Login failed:", err.resp.error["msg"])
				exit(1)
				#print(whalecallsupdate)
			ts3conn.use(sid=778)
			ts3conn.clientupdate(client_nickname="[OrderBook-BOT]")
			resp = ts3conn.whoami()
			client_id=resp[0]['client_id']
			ts3conn.sendtextmessage(targetmode=2, target=1, msg="NOTE: [b]FINEX[/b] has a [b]BID[/b] order of [b]" + str(bidorder) + " BTC[/b] in the book at [b]" + str(bid['price']) + " USD")
			ts3conn.clientmove(cid=44184, clid=client_id)
			time.sleep(3)
			#ts3conn.sendtextmessage(targetmode=1, target=botid, msg="!yt [URL]http://austeritysucks.com/orderwall.mp3[/URL]")
			ts3conn.sendtextmessage(targetmode=2, target=1, msg="NOTE: [b]FINEX[/b] has a [b]BID[/b] order of [b]" + str(bidorder) + " BTC[/b] in the book at [b]" + str(bid['price']) + " USD")
			time.sleep(4)
			#ts3conn.sendtextmessage(targetmode=1, target=botid, msg="!say \"Finn-ex BID WALL " + str(num2words(bidorder)) + " BTC\"")	
			ts3conn.quit()	
			f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/lastfinexorder.txt', 'w+', encoding='utf-8')
			f.write(str(bidorder))
			f.close()

