fib = [0, 1]
n = int(input("Masukkan jumlah angka Fibonacci: "))

# Mencetak jumlah bintang sesuai dengan angka Fibonacci
for i in range(n):
    if i < 2:
        print('*')
    else:
        fib.append(fib[-1] + fib[-2])
        print('*' * fib[i])
