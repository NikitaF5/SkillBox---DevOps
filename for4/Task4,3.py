n = int(input("Введите число: "))
for start in range(n + 1):
    for number in range(start, n + 1):
        print(number, end='\t')
    print()