n=9
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' '),
    print('*'),
    if 1 < i <= n - 1:
        for k in range(1,2*i - 2):
            print(' '),
        print('*'),
    elif i == n:
        for k in range(1,2*i - 1):
            print('*'),
    print()