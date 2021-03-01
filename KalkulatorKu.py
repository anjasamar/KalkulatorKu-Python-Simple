# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:03:07 2021

@author: anjas amar pradana
@lisensi: sumber terbuka
@aliansi: universitas dian nuswantoro
"""

#Menampilkan Pesan Selamat Datang
print ("hello selamat datang di kalkulatorku")

#Definisi atau fungsi pilihan fungsi program, seperti:
    #Fungsi Penambahan
def tambah(x, y):
    return x + y
    #Fungsi Pengurangan
def kurang(x, y):
    return x - y
    #Fungsi Perkalian
def kali(x, y):
    return x * y
    #Fungsi Pembagian
def bagi(x, y):
    return x / y

#Menampilkan tampilan opsi menu saat program di mulai
print("Pilih Operasi Kalkulator")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

#Perulangan fungsi pilihan program dengan definisi yang sudah di buat di atas.
#Ketika perintah benar
while True:
    
    #Tampil metode input atau insert seperti di bawah.
    pilihan = input("Masukan Pilihan 1, 2, 3, dan 4. >>")
    
    #Jika Pilihan input 1<->2<->3<->4 maka
    if pilihan in ('1','2','3','4'):
        
        #Memasukan angka1 ke dalam float input
        angka1 = float(input("Masukan angka awal: "))
        angka2 = float(input("Masukan angka akhir: "))
        
        #Dan jika pilihan di pilih sebelumnya, contoh 1, maka
        if pilihan == '1':
            
            #Menampilkan hasil dengan program: tambah(angka1, angka2), menjadi hasil dari kedua data float angka1 dan angka2.
            print(angka1, "+", angka2, "=", tambah(angka1, angka2))
        elif pilihan == '2':
            print(angka1, "-", angka2, "=", kurang(angka1, angka2))
        elif pilihan == '3':
            print(angka1, "*", angka2, "=", kali(angka1, angka2))
        elif pilihan == '4':
            print(angka1, "/", angka2, "=", bagi(angka1, angka2))
            
            #Jika program selesai1, Maka program akan di hentikan, atau break.
        break
    
    #Jika input pilihan tidak sesuai dengan pilihan di atas (1<->2<->3<->4), Maka akan tampil peringatan di bawah.
    else:
        print("Maaf, tapi fungsi tidak tersedia!")