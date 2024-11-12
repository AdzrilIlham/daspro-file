"""Nama : Adzril Ilham Ramadhan
Kelas : 1C-RPL
NIM : 2401263"""

def hitung_volume_tabung(jari_jari, tinggi):
    pi = 3.14159 
    volume = pi * (jari_jari ** 2) * tinggi
    return volume

jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

volume_tabung = hitung_volume_tabung(jari_jari, tinggi)

print(f"Volume tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah: {volume_tabung:.2f}")
