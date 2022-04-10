import datetime

print('\n')
print('Input:')
print('\n')

jmlh_cuti_bersama = int(input('Jumlah cuti bersama (kurang dari atau sama dengan 14 hari): '))
tgl_join = input('Tanggal join karyawan (yyyy-mm-dd): ')
tgl_start_cuti = input('Tanggal rencana cuti (yyyy-mm-dd): ')
durasi_cuti = int(input('Durasi cuti (maksimal 3 hari): '))

print('\n')
print('Output:')
print('\n')

if jmlh_cuti_bersama < 14 and durasi_cuti <= 3:

    cuti_kantor = 14
    jmlh_cuti_pribadi = cuti_kantor - jmlh_cuti_bersama

    join_year =  int(tgl_join.strip().split('-')[0])
    join_month =  int(tgl_join.strip().split('-')[1])
    join_day =  int(tgl_join.strip().split('-')[2])
    join_date = datetime.date(join_year, join_month, join_day)

    start_cuti_year = int(tgl_start_cuti.strip().split('-')[0])
    start_cuti_month =  int(tgl_start_cuti.strip().split('-')[1])
    start_cuti_day =  int(tgl_start_cuti.strip().split('-')[2])
    start_cuti_date = datetime.date(start_cuti_year, start_cuti_month, start_cuti_day)

    lama_kerja = (start_cuti_date - join_date).days

    if lama_kerja > 180:
        last_day_of_year = datetime.date.max.replace(year = start_cuti_year)
        _180days = datetime.timedelta(days=180)
        min_start_cuti_date = join_date + _180days

        jmlh_hari = (last_day_of_year - min_start_cuti_date).days
        cuti_yg_bisa_diambil = int(jmlh_hari/365 * jmlh_cuti_pribadi)

        if durasi_cuti > cuti_yg_bisa_diambil:
            print('False')
            print('Alasan: Karena hanya boleh mengambil {} hari cuti'.format(cuti_yg_bisa_diambil))
        else:
            print('True')

    else:
        print('False')
        print('Alasan: Karena belum 180 hari sejak tanggal join karyawan')

else:
    if jmlh_cuti_bersama >= 14:
        print("Cuti bersama lebih besar dari atau sama dengan 14 hari!")
        print("Jumlah cuti bersama yang dimasukkan: {}".format(jmlh_cuti_bersama))
    if durasi_cuti > 3:
        print("Durasi cuti lebih besar dari 3 hari!")
        print("Durasi cuti yang diinginkan: {}".format(durasi_cuti))

print('\n')