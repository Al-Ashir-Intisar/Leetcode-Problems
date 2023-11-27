for length in range(5, 0, -1):
    print(length)
    for start in range(5 - length + 1):
        print(start, start + length)