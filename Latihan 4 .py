baris = 5
kolom = 5

for i in range(1, baris + 1):
    num = i
    for j in range(kolom):
        print(num, end=" ")
        num += 2
    print()
