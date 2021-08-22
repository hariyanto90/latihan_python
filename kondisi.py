# membuat program discount barang minimal belanja Rp. 200.000




def calculate():
    try:
        user_input_number = int(user_input)
        if user_input_number >= 200000:
            print('Selamat Anda mendapatkan potongan harga 8%')
            hitung_discount = user_input_number * 8//100
            bayar = user_input_number - hitung_discount
            print(f'anda hanya membayar {bayar}')
        else:
            print(f'Total bayar {user_input}')
    except:
        print('anda memasukkan text')


user_input = ''

while user_input != 'exit' :
    user_input = input('Masukkan Total Pembelian Barang: ')
    calculate()
print('Terima Kasih sudah menggunakan program kami')