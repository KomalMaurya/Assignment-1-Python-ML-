#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q10 : Write a python program that converts a string to uppercase.
# Ans :
string =input("Enter the String : ")
string=string.upper()
print(string)


# Q11 : Write a python program that generates the first n numbers in the fibonacci sequence.
# Ans :
n1=0
n2=1
n=int(input("How many numbers you want to print : "))
print(n1,n2,end=' ')
for i in range(n-2):
    n3=n1+n2
    print(n3,end=' ')
    n1=n2
    n2=n3


# Q12 : Write a program program that calculates the sum of the digits of a given number.
# Ans :
num=int(input("Enter the number : "))
sum=0
while(num>0):
    rem=num%10
    sum+=rem
    num=num//10
print(sum)