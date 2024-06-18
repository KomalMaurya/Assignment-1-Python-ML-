#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q1 : Write a program that takes two numbers as input and prints their sum.
# Ans:
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
sum=num1+num2
print(sum)


# Q2 : Write a python program that checks whether a given number is even or odd.
# Ans:
num=int(input("Enter the number : "))
if(num%2==0):
    print(num," is an even number.")
else:
    print(num," is an odd number.")


# Q3 : Write a python program that calculates the factorial of a given number.
# Ans:
n=int(input("Enter the number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
