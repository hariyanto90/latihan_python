import requests

try:
    print('selamat datang')

    r = requests.get('https://goo gle.com')

    print(r.status_code)

    if r.status_code == 200:
        print(r.text)
except:
    print('Terjadi Kesalahan')