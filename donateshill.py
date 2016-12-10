#!/usr/bin/python3
 
import ts3
import datetime
from urllib.request import urlopen
import json
import math
import time
import random


with ts3.query.TS3Connection("158.69.115.146", 2009) as ts3conn:
        try:
	        ts3conn.login(
	        client_login_name="",
	        client_login_password=""
	        )
        except ts3.query.TS3QueryError as err:
                print("Login failed:", err.resp.error["msg"])
                exit(1)
        reasons=[]
        reasons.append("a kitten lives")
        reasons.append("Davyd05 will blow you")
        reasons.append("the profit gods will bless you")
        reasons.append("Satoshi will be found again")
        reasons.append("one less rapefugee will enter your country")
        reasons.append("flibbr will anti-coup your ass")
        reasons.append("thegimp will clean your pipes")
        reasons.append("Bitcoin-Viper will baghold your shitcoin")
        reasons.append("Aztek gives a psycho-anal-ysis session")
        reasons.append("Rick Stoner will bore you to death with shitcoin shilling")
        reasons.append("Marty will FOMO long")
        reasons.append("aknix will vocal fry you to death")
        shillreason = random.choice(reasons)
        #print(shillreason)
        #shillmessage="StakePool will always be a free and open community for traders, but we have bills. Do you find our services useful? Support StakePool costs by donating here: [url=https://chart.googleapis.com/chart?cht=qr&chs=200x200&chl=175oRbKiLtdY7RVC8hSX7KD69WQs8PcRJA]175oRbKiLtdY7RVC8hSX7KD69WQs8PcRJA[/url] or [url=http://raffle.stakepool.com]contribute in other ways[/url]."
        shillmessage2="Want to support the WhalePool bitcoin traders community? [url=https://whalepool.io/about/support] Find out how here. [/url] Or if you simply would like to donate to our BTC addie: [url=https://chart.googleapis.com/chart?cht=qr&chs=200x200&chl=175oRbKiLtdY7RVC8hSX7KD69WQs8PcRJA]175oRbKiLtdY7RVC8hSX7KD69WQs8PcRJA[/url] [b]For every donation " + shillreason + "[/b]"
        #shillmessage2="thegimp is activist in little indianboys bungholes doe"
	#[b]ZERO CONFIRMATION (not 0-fee) DEPOSITS ACCEPTED UNTIL LAST MINUTE![/b]
        ts3conn.use(sid=778)
        #print(shillmessage)
        ts3conn.clientupdate(client_nickname="[GuiltTrip-Bot]")
        ts3conn.sendtextmessage(targetmode=2, target=1, msg=shillmessage2)
        #ts3conn.sendtextmessage(targetmode=2, target=1, msg=str(reasons))
        resp = ts3conn.whoami()
        time.sleep(3)
        client_id=resp[0]['client_id']
        ts3conn.clientmove(cid=44184, clid=client_id)
        ts3conn.sendtextmessage(targetmode=2, target=1, msg=shillmessage2)
        ts3conn.quit()
