#!/usr/bin/python3

import datetime
from urllib.request import urlopen
import requests
import json
import dateutil.parser as dp
from telegram import *
import telegram
#res = requests.get('http://stackoverflow.com/questions/26000336')

#url     = http://example.tld
#payload = { 'key' : 'val' }
#headers = {}
#res2 = requests.post(url, data=payload, headers=headers)

#grab comments from issue

#https://api.github.com/repos/bharathrao/coinpit-tech/issues/9/comments

#grab issues

r = requests.get('https://api.github.com/repos/bharathrao/coinpit-tech/issues', auth=('', ''))
data=r.text
decodeddata=json.loads(data)
issuecount=len(decodeddata)

f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/cptupdate.txt', encoding='utf-8')
latestid = f.readline().strip()
highestid=latestid

f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/cptissue.txt', encoding='utf-8')
latestissue = f.readline().strip()
highestissue=latestissue


token=''
bot=telegram.Bot(token=token)


for x in range(0, issuecount):
	lastupdatetime=decodeddata[x]['updated_at']
	parsed_t = dp.parse(lastupdatetime)
	updatetimeins=parsed_t.strftime('%s')
	#print(updatetimeins)
	#print(str(decodeddata[x]['number']))
	if updatetimeins>latestid:
		newissuebody=decodeddata[x]['body']
		newissuetitle=decodeddata[x]['title']
		newissueurl=decodeddata[x]['html_url']
		newissuelogin=decodeddata[x]['user']['login']
		if newissuelogin=="ntom":
			username="@flibbr"
		elif newissuelogin=="chrisengel":
			username="@swapman"
		else:
			username=newissuelogin
		newissuenumber=decodeddata[x]['number']
		if newissuenumber>int(highestissue):
			highestissue=str(newissuenumber)
			textnewissue='New Issue #' + str(newissuenumber) + ': ' + newissuetitle + '\nPosted by ' + username + '\n' + newissuebody + '\nLink: '  + newissueurl
			#print(textnewissue)
			bot.sendMessage(chat_id="-1001083422919", text=textnewissue)
		else:
			textnewcomment='New comment in Issue #' + str(newissuenumber) + ': ' + newissuetitle + '\nRead more here: '  + newissueurl
			#print(textnewcomment)
			bot.sendMessage(chat_id="-1001083422919", text=textnewcomment)
		highestid=updatetimeins
	#print(updatetimeins)

f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/cptupdate.txt', 'w+', encoding='utf-8')
f.write(str(highestid))

f = open('/home/ubuntu/volume1/stakepool/teamspeakbots/cptissue.txt', 'w+', encoding='utf-8')
f.write(str(highestissue))

#"created_at": "2016-09-15T17:22:02Z",
#   "updated_at": "2016-09-15T17:22:02Z",
#  "closed_at": null,


#"url": "https://api.github.com/repos/bharathrao/coinpit-tech/issues/2",
#   "repository_url": "https://api.github.com/repos/bharathrao/coinpit-tech",
    #"events_url": "https://api.github.com/repos/bharathrao/coinpit-tech/issues/2/events",
    #"#html_url": "https://github.com/bharathrao/coinpit-tech/issues/2",
   # "id": 177304349,
   # "number": 2,
  # "body": "At the moment it is difficult to work out the notional value of any given order under the active orders. \r\nIt is also difficult to work out what is the average leverage used if you were to merge all the contracts. \r\n\r\nKnowing these cumulative and average values provides important information to the trader. \r\n\r\nHow many contracts have i got open ? \r\nWhat % margin Long/short am I on average if i Just merged everything .. \r\n\r\netc"
 # },

