n = int(input())
binary = 0
count = 0
while (n != 0):
    rem = n % 2
    power = pow(10, count)
    binary += rem * power
    n //= 2
    count += 1
print(binary)
