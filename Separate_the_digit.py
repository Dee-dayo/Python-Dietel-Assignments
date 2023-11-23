num = int(input("Enter a number: "))

num1 = (num // 10000) % 10
num2 = (num // 1000) % 10
num3 = (num // 100) % 10
num4 = (num // 10) % 10
num5 = num % 10

print(f"{num1}   {num2}   {num3}   {num4}   {num5}")
