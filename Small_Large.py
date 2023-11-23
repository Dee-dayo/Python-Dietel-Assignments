num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum = num1 + num2 + num3
average = sum / 3
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print("The sum of three number is: ", sum) 
print("Average is: ", average)
print("Maximum number is: ", largest)
print("Minimum number is: ", smallest)