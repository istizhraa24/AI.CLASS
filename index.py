#Input Nilai Index Nya
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
#input Nilai Yang Ingin Ditampilkan
x = 5

#Logika Progran nya
if x in A:
    count = A.count(x)
    indices = [index for index, value in enumerate(A) if value == x]

#Output Dari Input dan Logika Yang Digunakan Sebelumnya
    print(f"Variabel x ({x}) muncul {count} kali dalam list A.")
    print(f"Indeks kemunculan nilai x ({x}): {indices}")
else:
    print(f"Variabel x ({x}) tidak ditemukan dalam list A.")