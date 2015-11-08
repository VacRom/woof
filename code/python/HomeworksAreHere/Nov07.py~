def hs(n):
    # First we look to filter out all 'bad' inputs for n.
    if n == 0 or n < 0 or n != int(n) or not isinstance(n, int):
        print("Error: Must be a positive non-zero integer.")
        exit()
    # Our length counter will be l. Set at 1, since the base length it itself.
    l = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l = l + 1
        print(n)
    print(l)
    print("None")
