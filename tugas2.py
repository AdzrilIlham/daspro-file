"""Nama : Adzril Ilham Ramadhan
Kelas : 1C-RPL
NIM : 2401263"""

USERNAME_TERDAFTAR = "Daspro2023"
PASSWORD_TERDAFTAR = "Latihan"
MAX_mencoba = 3

print("Selamat datang di sistem login Admin SMAN 2 Harapan")
for attempt in range(1, MAX_mencoba + 1):
    username_input = input("Masukkan username: ")
    password_input = input("Masukkan password: ")

    if username_input == USERNAME_TERDAFTAR and password_input == PASSWORD_TERDAFTAR:
        print("Login berhasil! Selamat datang di sistem.")
        break
    else:
        sisa_percobaan = MAX_mencoba - attempt
        print("Username atau password salah.")
        
        if sisa_percobaan > 0:
            print(f"Silakan coba lagi. Sisa percobaan: {sisa_percobaan}")
        else:
            print("Anda telah mencapai batas maksimum percobaan login. Login gagal.")
