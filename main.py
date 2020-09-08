def my_function(a, b, c):
    print(a, b, c)
    x = a + b
    print('the sum of a and b:', x)
    if x > c:
        print('a + b > c')
    else:
        print('a + b <= c')


print('Please, enter three numbers below')
n1 = int(input('Number1: '))
n2 = int(input('Number2: '))
n3 = int(input('Number3: '))

my_function(n1, n2, n3)
