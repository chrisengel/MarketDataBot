#!/usr/bin/python3

import ts3
import datetime
import dateutil.parser
from urllib.request import urlopen
import json
import math
import time
from twitter import *


#scrape from bitmex instrument endpoint
url = "https://www.bitmex.com/api/v1/instrument?symbol=XBTUSD&count=100&reverse=false"

#grab url
page = urlopen(url)

#read data
data=page.read()
grabmexarray=json.loads(data.decode())

#get funding rates
fundingrate8hr = grabmexarray[0]['fundingRate']*100
fundingratedaily = (((1+(fundingrate8hr/100))**3)-1)*100

predictedfundingrate = grabmexarray[0]['indicativeFundingRate']*100

fundingrateannual = (((1+(fundingrate8hr/100))**1095)-1)*100

nextfunding = dateutil.parser.parse(grabmexarray[0]['fundingTimestamp'])

nextfundingint=round(nextfunding.timestamp())

currentts = dateutil.parser.parse(grabmexarray[0]['timestamp'])

currenttsint = round(currentts.timestamp())

timetofunding = nextfundingint-currenttsint

#print(str(timetofunding))

minstofunding=timetofunding/60

#grab bid/ask and index data 

currentbid = grabmexarray[0]['bidPrice']

currentask = grabmexarray[0]['askPrice']

currentindex = grabmexarray[0]['indicativeSettlePrice']

premiumask=((currentindex-currentask)/currentask)*100

premiumbid=((currentindex-currentbid)/currentbid)*100

premiumask=round(premiumask,4)
premiumbid=round(premiumbid,4)

if fundingrate8hr<0:
   shillmessage="[b]BitMEX BTCUSD[/b] perpetual swap funding payout in [u]15 minutes[/u]: " + str(round(fundingrate8hr,4)) + "% (" + str(round(fundingratedaily,4)) + "% daily rate). [b][color=red]Short contract holders will pay long holders " + str(abs(round(fundingrate8hr,4))) + "%.[/color][/b] Current Bid: " + str(currentbid) + ", Ask: " + str(currentask) + ", Index: " + str(currentindex) + "(" + str(premiumask) + "% premium to best ask)"
else:
   shillmessage="[b]BitMEX BTCUSD[/b] perpetual swap funding payout in [u]15 minutes[/u]: " + str(round(fundingrate8hr,4)) + "% (" + str(round(fundingratedaily,4)) + "% daily rate). Long contract holders will pay short holders " + str(abs(round(fundingrate8hr,4))) + "%. Current Bid: " + str(currentbid) + ", Ask: " + str(currentask) + ", Index: " + str(currentindex) + "(" + str(premiumbid) + "% premium to best bid)"


if minstofunding<30:
   print(shillmessage)

   with ts3.query.TS3Connection("158.69.115.146", 2009) as ts3conn:
           try:
                   ts3conn.login(
                           client_login_name="",
                           client_login_password=""
                   )
           except ts3.query.TS3QueryError as err:
                   print("Login failed:", err.resp.error["msg"])
                   exit(1)

           ts3conn.use(sid=778)
        #print(shillmessage)
           ts3conn.clientupdate(client_nickname="[SWAP-Bot]")
           ts3conn.sendtextmessage(targetmode=2, target=1, msg=shillmessage)
           resp = ts3conn.whoami()
           time.sleep(3)
           client_id=resp[0]['client_id']
           ts3conn.clientmove(cid=44184, clid=client_id)
           ts3conn.sendtextmessage(targetmode=2, target=1, msg=shillmessage)
           ts3conn.clientmove(cid=56600, clid=client_id)
           ts3conn.sendtextmessage(targetmode=2, target=1, msg=shillmessage)
           ts3conn.clientmove(cid=57474, clid=client_id)
           ts3conn.sendtextmessage(targetmode=2, target=1, msg=shillmessage)
           ts3conn.quit()
           t = Twitter(auth=OAuth('', '', '', ''))
           shilltweet= "BitMEX BTCUSD funding payout in 15 minutes: " + str(round(fundingrate8hr,4)) + "%,  Bid: " + str(currentbid) + ", Ask: " + str(currentask) + ", Index: " + str(currentindex) + "(" + str(premiumask) + "% premium to ask, " + str(premiumbid) + "% to bid)"
           t.statuses.update(status=shilltweet)


