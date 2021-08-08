import requests

try:
    print('selamat datang')

    r = requests.get('https://goo gle.com')

    print(r.status_code)

    if r.status_code == 200:
        print(r.text)

except:
    print('Terjadi Kesalahan')


calculate_hours = 24


def convers_hours(input_days):
    if input_days > 0:
        return f'{input_days} hari adalah {input_days * calculate_hours} jam'
    elif input_days == 0:
        return ('Nilai yang anda masukkan adalah 0, silahkan masukkan nilai yang valid')
    else:
        return ('Nilai yang anda masukkan adalah nilai negatif, silahkan masukkan nilai yang valid')


def convertional_user_input():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculation_input_user = convers_hours(user_input_number)
        print(calculation_input_user)
    else:
        print('anda memasukkan teks, silahkan masukkan nilai yang valid')


user_input = input('program mengkonversikan hari ke jam \n')
convertional_user_input()






