def collatz(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        n = n / 2
        return 1 + collatz(n)
    else:
        n = n * 3 + 1
        return 1 + collatz(n)


while True:
    num = int(input("Enter number to be evaluated: "))
    print("Number of iterations: {}".format(collatz(num)))