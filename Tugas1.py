"""Nama : Adzril Ilham Ramadhan
Kelas : 1C-RPL
NIM : 2401263"""

def fibonacci(n):
    deret = []
    a, b = 0, 1
    for _ in range(n):
        deret.append(a)
        a, b = b, a + b
    return deret

N = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))

if N > 0:
    deret_fibonacci = fibonacci(N)
    print(f"Deret Fibonacci sebanyak {N} bilangan adalah: {deret_fibonacci}")
else:
    print("Masukkan bilangan positif yang valid.")
