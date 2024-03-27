rows = 5
pattern = ["A", "B"]

for i in range(rows):
    for j in range(rows):
        print(pattern[(i+j) % 2], end=" ")
    print()
