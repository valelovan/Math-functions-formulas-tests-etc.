# Pascal's triangle row calculator



def pascals_row(n):

    # Calculate n! recursively
#    def fact(n):
#        if n == 0:
#            return 1
#        else:
#            return n * fact(n - 1)

    # Calculate n! iteratively
    def fact(n):
        product = 1 
        for i in range(1,n + 1):
            product *= i
        return product

    # Calculate Cominatorial of nCr
    def combination(n, r):
        return fact(n) / (fact(r) * fact(n-r))
    
    # Create entries for the row
    row = []
    for i in range(n):
        row.append(int(combination(n - 1, i)))
    return row



while True:

    n = int(input('Enter a Pascal\'s triangle row to be evaluated: '))

    print(pascals_row(n))