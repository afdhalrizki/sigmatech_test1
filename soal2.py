print('\n')
print('Input:')
print('\n')
total = int(input('Total belanja seorang customer: '))
jumlah_bayar = int(input('Pembeli membayar: '))
print('\n')
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
jumlah_pecahan = {}
kembalian = jumlah_bayar - total
print('Output:')
print('\n')

if kembalian < 0:
    print('False, kurang bayar')
else:
    print('Kembalian yang harus diberikan kasir: {}'.format(kembalian))
    print('\n')
    for pecahan in uang_pecahan:
        if kembalian < pecahan:
            continue
        banyak_pecahan = int(kembalian / pecahan)
        kembalian = kembalian - (pecahan * banyak_pecahan)
        if pecahan == 200 or pecahan == 100:
            print('{} koin {}'.format(banyak_pecahan, pecahan))
        else:
            print('{} lembar {}'.format(banyak_pecahan, pecahan))

print('\n')