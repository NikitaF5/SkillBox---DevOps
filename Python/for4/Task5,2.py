for row in range(1, 6):
    for col in range(1, 6):
        if col <= row:
            print(row, end = '\t')
    print()