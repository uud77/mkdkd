#$$$$$$$$$حقوق عبود$$$$$$$$$$$
import os
import time
import random
import requests
import sqlite3
import socket
import webbrowser
from urllib.parse import urlparse
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

API_KEY_ABUSEIPDB = "c1e29afd368d25ae1985b280fedfad4b6df683312f1c600ceab40453aad7be80a99e29b29396b883"
API_KEY_VIRUSTOTAL = "4b6890506e66571cae4bb5ca3829d7537972cec81fcf54b006ce49a13a0a4cc9"
start_time = datetime.now()
DB_NAME = "cyberblade_log.db"

MRT_LOGO = """
███╗   ███╗██████╗ ████████╗
████╗ ████║██╔══██╗╚══██╔══╝
██╔████╔██║██████╔╝   ██║
██║╚██╔╝██║██╔═══╝    ██║
██║ ╚═╝ ██║██║        ██║
╚═╝     ╚═╝╚═╝        ╚═╝
user Telegram: https://t.me/N_QJS
chaneel: https://t.me/Q_X_TX

"""

DEV_NAME = "المطور: عبود ☠️"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F)",
]

COMMON_HEADERS = {
    "Accept": "/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

def get_session():
    session = requests.Session()
    headers = COMMON_HEADERS.copy()
    headers["User-Agent"] = random.choice(USER_AGENTS)
    session.headers.update(headers)
    return session

def db_init():
    conn = sqlite3.connect(DB_NAME)
    conn.execute('''CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        active INT,
        suspicious INT,
        status TEXT
    )''')
    conn.commit()
    conn.close()

def save_report(url, active, suspicious, status):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("INSERT INTO reports (url, active, suspicious, status) VALUES (?, ?, ?, ?)",
                 (url, active, suspicious, status))
    conn.commit()
    conn.close()

def is_active(url):
    try:
        session = get_session()
        return session.get(url, timeout=5).status_code == 200
    except:
        return False

def is_suspicious(url):
    keywords = ['login', 'secure', 'bank', 'reset', 'verify']
    return any(word in url.lower() for word in keywords)

def extract_domain(url):
    return urlparse(url).hostname

def domain_to_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def report_to_abuseipdb(ip):
    try:
        headers = {
            "Key": API_KEY_ABUSEIPDB,
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "ip": ip,
            "categories": "18",
            "comment": "Reported by MRT | Dev: Abod @N_QJS"
        }
        res = requests.post("https://api.abuseipdb.com/api/v2/report", headers=headers, data=data)
        return res.status_code == 200
    except:
        return False

def report_to_virustotal(url):
    try:
        headers = {"x-apikey": API_KEY_VIRUSTOTAL}
        data = {"url": url}
        res = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=data)
        return res.status_code in [200, 201]
    except:
        return False

def scan_url(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    domain = extract_domain(url)
    ip = domain_to_ip(domain)
    active = is_active(url)
    suspicious = is_suspicious(url)

    print(Fore.CYAN + f"\n  فحص الرابط: {url}")
    print(Fore.YELLOW + f"  الدومين: {domain}")
    print(Fore.YELLOW + f"  IP: {ip or 'غير معروف'}")
    print(Fore.GREEN + f"  الموقع نشط: {active}")
    print(Fore.RED + f"  سلوك مشبوه: {suspicious}")

    abuse = report_to_abuseipdb(ip) if ip else False
    vt = report_to_virustotal(url)

    print(Fore.LIGHTGREEN_EX + ("  تم التبليغ لـ AbuseIPDB" if abuse else "  فشل التبليغ لـ AbuseIPDB"))
    print(Fore.LIGHTGREEN_EX + ("  تم التبليغ لـ VirusTotal" if vt else "  فشل التبليغ لـ VirusTotal"))

    status = f"Abuse: {abuse}, VT: {vt}"
    save_report(url, int(active), int(suspicious), status)

def start_intro_animation():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    start = time.time()
    while time.time() - start < 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(random.choice(colors) + Style.BRIGHT + MRT_LOGO)
        print(Fore.LIGHTBLACK_EX + DEV_NAME.center(60))
        print(Fore.LIGHTYELLOW_EX + "جاري تشغيل ادات المطور عبود🇲🇷 ...".center(60))
        print(Fore.LIGHTBLUE_EX + "-"*60)
        time.sleep(0.3)

    # عرض ثابت
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + MRT_LOGO)
    print(Fore.LIGHTBLACK_EX + DEV_NAME.center(60))
    print(Fore.LIGHTYELLOW_EX + "اختار من القائمة.".center(60))
    print(Fore.LIGHTBLUE_EX + "-"*60)

def main_menu():
    while True:
        print(Fore.LIGHTMAGENTA_EX + "\n[1] تواصل مع المطور ")
        print("[2] قناة تليجرام")
        print("[3] وقت تشغيل الأداة")
        print("[4] اسم المطور")
        print("[5] IP الجهاز")
        print("[6] فحص روابط وإرسال بلاغ")
        print("[0] خروج")

        choice = input(Fore.CYAN + "\nاختر خيارًا: ")

        if choice == '1':
            webbrowser.open("https://t.me/N_QJS")
        elif choice == '2':
            webbrowser.open("https://t.me/Q_X_TX")
        elif choice == '3':
            elapsed = datetime.now() - start_time
            print(Fore.YELLOW + f"⏱️ وقت التشغيل: {str(elapsed).split('.')[0]}")
        elif choice == '4':
            print(Fore.CYAN + f"👨‍💻 المطور: عبود")
        elif choice == '5':
            ip = socket.gethostbyname(socket.gethostname())
            print(Fore.CYAN + f"📍 IP: {ip}")
        elif choice == '6':
            urls = input("🇲🇷 أدخل روابط (مفصولة بفاصلة): ").split(',')
            for url in urls:
                scan_url(url.strip())
        elif choice == '0':
            print("🥲 تم الخروج، مع السلامة.")
            break
        else:
            print(Fore.RED + "👌 خيار غير صالح!")

if __name__ == "__main__":
    db_init()
    start_intro_animation()
    main_menu()