#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q22 : Write a python program that returns the maximum and minimum values in a list of numbers.
# Ans :
list1=list(eval(input("Enter the list of numbers : ")))
max=list1[0]
min=list1[0]
for i in list1:
    if i>max:
        max=i
    if i<min:
        min=i
print("The maximum number in the list :",max)
print("The minimum number in the list :",min)


# Q23 : Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
# Ans :
temp=float(input("Enter the temperature : "))
str1=input("Temp. to be converted in which C/F? : ")
temp_f=0
if str1=="F" or str1=='f':
    temp_f=((9/5)*temp)+32
    if temp_f>=32:
        print(temp_f,": temperature in Fahrenheit")
    
elif str1=="C" or str1=='c':
    temp_c=(temp-32)*(5/9)
    if temp_c>=-273:
        print(temp_c,": temperature in Celsius")

else:
    print("Enter valid character : ")


# Q24 : Write a program that acts as a simple calculator. It should take two numbers and an operator(+,-,*,/) as input and print the result.
# Ans :
num1=int(input("Enter the number 1 : "))
num2=int(input("Enter the number 2 : "))
op=input("Enter the operator (+,-,*,/) : ")

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Enter valid operator!!")
