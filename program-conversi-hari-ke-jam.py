# program convert hari ke jam
calculation_hours = 24


def convert_day_to_hours(number_of_day):
    return f'{number_of_day} hari adalah {number_of_day * calculation_hours} hours'


def validation_and_excute():

    try:
        user_input_number = int(list_user_input)
        if user_input_number > 0:
            output_hours = convert_day_to_hours(user_input_number)
            print(output_hours)
        elif user_input_number == 0:
            print('Anda memasukkan nilai 0, silahkan masukkan nilai yang valid')
        else:
            print('Anda memasukkan nilai negatif, silahkan masukkan nilai yang valid')
    except:
        print('anda memasukan text, silahkan memasukan nilai yang valid')


user_input = ''
while user_input != 'exit':
    user_input = input('Program Konversi Hari Ke Jam Silahkan masukkan hari \n')
    for list_user_input in user_input.split(','):
        validation_and_excute()

