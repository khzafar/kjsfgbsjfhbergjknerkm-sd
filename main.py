n = int(input("Son kirit: "))
m = n % 3
z = 0
while n > 1 and m == 0 or n == 1:
    if n == 1:
        print(f'bu son 3 ning {z} - darajasi')
        break
    z += 1
    m = n % 3
    n = n / 3
if n < 1 and m != 0 or n != 1:
    print('bu son 3 ning darajasi emas')
