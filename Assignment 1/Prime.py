n = int(input("Enter number: "))
if n == 0 or n == 1:
    print(n, "is neither prime nor composite number.")

elif n > 1:
    for i in range(2, int(n // 2) + 1):
        if (n % i) == 0:
            print(n, "is not a prime number.")
            break
    else:
        print(n, "is a prime number.")

else:
    print(n, "is not a prime number.")
