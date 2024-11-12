# Pengaturan awal
kanan = ['P1', 'I1', 'P2', 'I2', 'P3', 'I3'] 
kiri = []

def menyeberang(siapa, arah):
    if arah == 'kiri':
        for orang in siapa:
            if orang in kanan:
                kiri.append(orang)
                kanan.remove(orang)
    elif arah == 'kanan':
        for orang in siapa:
            if orang in kiri:
                kanan.append(orang)
                kiri.remove(orang)

    print(f"Kiri: {kiri}, Menyeberang: {siapa}, Kanan: {kanan}")

if __name__ == "__main__":
    print(f"Posisi awal - Kiri: {kiri}, Kanan: {kanan}")

    menyeberang(['I1', 'P1'], 'kiri')    
    menyeberang(['I1'], 'kanan')         
    menyeberang(['I2', 'P2'], 'kiri')    
    menyeberang(['P1'], 'kanan')         
    menyeberang(['I1', 'P1'], 'kiri')   
    menyeberang(['I1'], 'kanan')         
    menyeberang(['I3', 'P3'], 'kiri')    
    menyeberang(['P1'], 'kanan')         
    menyeberang(['I1', 'P1'], 'kiri')    
