from ast import Index, Return
from random import random
from turtle import update



List_Data_Talent = [
    {
        'Code' : 1,
        'Posisi' : 'Sales',
        'Jumlah' : 10,
        'Gaji' : 12,
        'PIC' : 'Andi'

    },
    {
        'Code' : 2,
        'Posisi' : 'Legal',
        'Jumlah' : 12,
        'Gaji' : 13,
        'PIC' : 'Miki'
        },
     {
        'Code' : 3,
        'Posisi' : 'Sound',
        'Jumlah' : 13,
        'Gaji' : 14,
        'PIC' : 'Geraldo'
     }
]

cart = []

# Fungsi sendiri untuk menanyakan YES/NO 
def YESNO() :
    YESNO_Menu = input('''
    Apakah anda yakin dengan pilihan ini? (Y/N)
    ''')

    return YESNO_Menu



# Main Menu
def MainMenu() :
    while True :
        PilihanMenu = input('''
        DATA TALENT SIAP KERJA

        List Menu :
        1. Menampilkan List Data Talent
        2. Menambahkan Data Talent
        3. Mengubah Data Talent
        4. Menghapus Data Talent
        5. Exit Program

        Masukkan angka menu yang ingin dijalankan : ''')
        if(PilihanMenu == '1') :
            Menampilkan_DataTalent_SiapKerja()
        elif(PilihanMenu == '2') :
            Menambahkan_Data_Talent()
        elif(PilihanMenu == '3') :
            Mengubah_Data()
        elif(PilihanMenu == '4') :
            MenghapusDataTalent()
        elif(PilihanMenu == '5') :
            print(''' \n\tThank You For Using Our Services
                See You Next Time\n''')
            break
       
        else :
            print('\nPilihan yang anda masukkan salah')
            break



# Menu 1 (Read Data)

def Menampilkan_DataTalent_SiapKerja() :

# Sub Menu
    while True :
        print(''' 
        1. Menampilkan Semua Talent
        2. Menampilkan Talent Tertentu
        3. Kembali Ke Menu Utama

        ''')
        SubMenu = input('''Masukkan angka submenu yang ingin dijalankan : ''')
        if (SubMenu == '1') :
            print('''
            LIST DATA TALENT SIAP KERJA

            Index   | Code  | Posisi | Jumlah | Gaji | PIC\n''')

            for i in range(len(List_Data_Talent)) :
                print('\t\t{}   | {}\t    | {}  | {}     | {}   | {}'.format(i,List_Data_Talent[i]['Code'], List_Data_Talent[i]['Posisi'], List_Data_Talent[i]['Jumlah'], List_Data_Talent[i]['Gaji'], List_Data_Talent[i]['PIC'])) 
            Menampilkan_DataTalent_SiapKerja()
        
        elif (SubMenu == '2') :
            JobCode = int(input('Masukkan Job Code : '))
            find = False
            for i in range(len(List_Data_Talent)) :
                if List_Data_Talent[i]['Code'] == JobCode :
                    print('''
            Index   | Code  | Posisi | Jumlah | Gaji | PIC''')
                    print('\t\t{}   | {}\t    | {}  | {}     | {}   | {}'.format(i,List_Data_Talent[i]['Code'], List_Data_Talent[i]['Posisi'], List_Data_Talent[i]['Jumlah'], List_Data_Talent[i]['Gaji'], List_Data_Talent[i]['PIC'])) 
                    find = True
                    break

            if find == False:
                print('\nJob Code tidak ditemukan')
                # Menampilkan_DataTalent_SiapKerja()
        elif (SubMenu == '3') :
            MainMenu()
        else :
            print('''
Pilihan yang anda masukkan salah
            ''')

# Menu 2 (Add Data)

def Menambahkan_Data_Talent() :
# Sub Menu
    while True :
        print('''  
            1. Menambahkan Data 
            2. Kembali ke Menu Utama
            ''') # Semua menu harus dibikin sub menu seperti ini
        SubMenu = input('''Masukkan angka submenu yang ingin dijalankan : ''')
        if (SubMenu == '1') :
            JobCode = int(input('Masukkan Job Code Talent : '))
            find = False
            for i in range(len(List_Data_Talent)):
                if JobCode == List_Data_Talent[i]['Code']:
                    print('Data sudah ada')
                    find = True
                    break
            if find == False :
                PosisiTalent = input('Masukkan Posisi Talent : ')
                Jumlah = int(input('Masukkan Jumlah Talent : '))
                GajiTalent = int(input('Masukkan Gaji Talent : '))
                PICTalent = input('Masukkan Nama PIC : ')
                List_Data_Talent.append({
                    'Code' : JobCode,
                    'Posisi': PosisiTalent,
                    'Jumlah': Jumlah,
                    'Gaji': GajiTalent,
                    'PIC' : PICTalent
                    })
                variable = YESNO()
                if variable == "Y":
                    print('Data telah tersimpan')
                elif variable =="N":
                    Menambahkan_Data_Talent()
        elif (SubMenu == '2') :
            MainMenu()
        else :
            Menambahkan_Data_Talent()

# Menu 3 (Update Data)

def Mengubah_Data() :
    # Sub Menu
    while True :
        print('''
        1. Mengubah List Data Talent
        2. Kembali Ke Menu Utama
        ''')
        SubMenu = input(' Masukkan angka submenu yang ingin dijalankan : ')
        if (SubMenu == '1') :
            JobCode = int(input('Masukkan Job Code : '))
            index = 0
            find = False
            for i in range(len(List_Data_Talent)) :
                if List_Data_Talent[i]['Code'] == JobCode :
                    print('''
            Index   | Code  | Posisi | Jumlah | Gaji | PIC''')
                    print('\t\t{}   | {}\t    | {}  | {}     | {}   | {}'.format(i,List_Data_Talent[i]['Code'], List_Data_Talent[i]['Posisi'], List_Data_Talent[i]['Jumlah'], List_Data_Talent[i]['Gaji'], List_Data_Talent[i]['PIC'])) 
                    find = True
                    break
                else :
                    index+=1
                    break
            if find == False :
                print('\nJob Code tidak ditemukan')
                continue
            check = input('Apakah ada data yang ingin diubah?(Y/N) ').upper()
            if check == 'Y' :
                UbahKolom = input('Masukkan kolom yang ingin diubah : ').capitalize()
                if UbahKolom == 'Posisi' :
                    a = (input('Posisi = ')).capitalize()
                    check = input('Apakah data ini akan disimpan? (Y/N) ').upper()
                    if check == 'Y':
                        List_Data_Talent[index]['Posisi'] = a
                        print('Data telah disimpan')
                    else :
                        print('Data belum disimpan')
                elif UbahKolom == 'Jumlah' :
                    b = int(input('Jumlah = ')).capitalize()
                    if b != int :
                        print('Masukkan data berupa angka!')
                    check = input('Apakah data ini akan disimpan? (Y/N)').upper()
                    if check =='Y' :
                        List_Data_Talent[index]['Jumlah'] = b
                        print('Data telah disimpan')
                    else :
                        print('Data belum disimpan')
                elif UbahKolom == 'Gaji' :
                    c = int(input('Gaji = '))
                    if c != int :
                        print('Masukkan data berupa angka!')
                    check = input('Apakah data ini akan disimpan? (Y/N)').upper()
                    if check == 'Y' :
                        List_Data_Talent[index]['Gaji'] = c
                        print('Data telah disimpan')
                    else :
                        print('Data belum disimpan')
                elif UbahKolom == 'PIC' :
                    d = (input('PIC = ')).capitalize()
                    check = input('Apakah data ini akan disimpan? (Y/N)').upper()
                    if check == 'Y' :
                        List_Data_Talent[index]['PIC'] = d
                    else :
                        print('Data belum disimpan')
        else :
            break



# Menu 4 (Hapus Data)

def MenghapusDataTalent() :
    # Sub Menu
    while True :
        print('''
        1. Menghapus Data Talent
        2. Kembali Ke Menu Utama 
        ''')
        SubMenu = input('''Masukkan angka submenu yang ingin dijalankan : ''')
        if (SubMenu == '1') :
            JobCode = int(input('Masukkan Job Code Talent yang ingin dihapus : '))
            Index = 0
            find = False
            for i in range(len(List_Data_Talent)) :
                if List_Data_Talent[i]['Code'] == JobCode :
                    print('''
            Index   | Code  | Posisi | Jumlah | Gaji | PIC''')
                    print('\t\t{}   | {}\t    | {}  | {}     | {}   | {}'.format(i,List_Data_Talent[i]['Code'], List_Data_Talent[i]['Posisi'], List_Data_Talent[i]['Jumlah'], List_Data_Talent[i]['Gaji'], List_Data_Talent[i]['PIC'])) 
                    find = True
                    break
                else:
                    Index+=1
            if find == False :
                print('\nJob Code tidak ditemukan')
                continue
            variable = YESNO()
            if variable == "Y":
                del List_Data_Talent[JobCode]
                print('Data telah terhapus')
            elif variable =="N":
                print('Data belum dihapus')
                MenghapusDataTalent()
            else :
                break
        else :
            break

MainMenu()
