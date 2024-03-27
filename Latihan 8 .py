rows = 5
pattern = ["S", "O"]

for i in range(rows):
    for j in range(rows - i):
        print(pattern[(i + j) % 2], end=" ")
    print()
