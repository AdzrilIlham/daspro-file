"""Nama : Adzril Ilham Ramadhan
Kelas : 1C-RPL
NIM : 2401263"""

nilai_input = input("Masukkan nilai-nilai, dipisahkan dengan koma: ")
nilai_list = [float(nilai.strip()) for nilai in nilai_input.split(",")]

if len(nilai_list) > 0:
    rata_rata = sum(nilai_list) / len(nilai_list)
    print(f"Rata-ratanya adalah: {rata_rata}")
else:
    print("Tidak ada nilai yang dimasukkan.")
