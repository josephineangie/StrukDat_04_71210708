import json
from tracemalloc import stop

data = None

with open('mahasiswa.json', 'a+') as datafile:
    data = datafile.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].strip()

jumlah_maba = int(input("Masukkan jumlah mahasiswa baru : "))
for i in range(0, jumlah_maba):
    nama = input("Masukkan nama Anda : ")
    data.append(nama + "\n")
    jumlah_hobi = int(input("Masukkan jumlah hobi : "))
    for j in range(1, jumlah_hobi, 1):
        hobi = input("Masukkan hobi ke-" + str(j) + " :")
        data.append(hobi + "\n")
        if j == jumlah_hobi:
            return nama

    print("=== Data berhasil ditambahkan ===")

with open("mahasiswa.json", "w") as datafile:
    for line in data:
        datafile.write(line + "\n")
