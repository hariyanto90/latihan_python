user_input = input('Masukkan Kata : ')

temp = ''

for i in range(len(user_input) -1, -1, -1) : #lopping dari karakter atau huruf terakhir
    temp += user_input[i]


if user_input == temp:
    print('Palindrom')
else:
    print('Bukan Palindrom')
