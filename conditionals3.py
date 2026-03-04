"""Check if a person can donate blood:

Age ≥ 18

Weight ≥ 50"""
from anyio import current_effective_deadline

age=20
weight=55
if (age>=18) and (weight>=50):
    print("eligible to donote")
else:
    print("Not Eligible to donote")
print("-------------------------------------------------------------------------")
#Check if three sides can form a triangle.
a,b,c=5,8,5
if (a+b>c) and (a+c>b) and (b+c>a):
    print("form Triange")
else:
    print("Not Form Triangle")
print("-------------------------------------------------------------------------")
#Find the smallest of three numbers.
a,b,c=2,3,4
if (a<=b) and (a<=c):
    print("A is small",a)
elif (b<=a) and (b<=c):
    print("B is small",b)
else:
    print("C is small",c)
print("-------------------------------------------------------------------------")
#Check if a number is palindrome (like 121).
num=123
if str(num)==str(num)[::-1]:
    print("Palindrome")
else:
    print('not palindrome')
print("-------------------------------------------------------------------------")
#Check if a number is Armstrong (3-digit).
num=154
original=num
total=0
digits=len(str(num))
while num>0:
    digit=num%10
    digit=digit**digits
    total=total+digit
    num=num//10
if original==total:
    print("Armstrong")
else:
    print("Not Armstrong")
print("-------------------------------------------------------------------------")
'''ATM withdrawal:

Balance check

Sufficient funds

Print remaining balance'''
current_balance=5000
withdraw=1000
sign=2 # 1 means Balance check 2 means withdraw
if sign==1:
    print("Current Balance",current_balance)
elif sign==2:
    if current_balance>=withdraw:
        current_balance-=withdraw
        print("withdraw successfull")
        print("remaining Balance:",current_balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid option")
print("-------------------------------------------------------------------------")
'''Login system:

Username and password check'''
u_name="sam"
p_word="spidey"
username=input("Enter Username:")
password=input("Enter password:")
if u_name==username and p_word==password:
    print("Login sucessfull")
else:
    print("invalid username or password")
print("-------------------------------------------------------------------------")
#Check if a number is positive even.
num=15
if num>0 and num%2==0:
    print("Positive Even")
else:
    print('Not Positive Even')
print("-------------------------------------------------------------------------")
'''Electricity bill calculation:

First 100 units → ₹5/unit

Next 100 → ₹7/unit

Above 200 → ₹10/unit'''
unit=350
if unit<=100:
    bill=unit*5
    print(bill)
elif 100<unit<=200:
    bill=(100*5)+((unit-100)*7)
    print(bill)
else:
    bill=(100*5)+(100*7)+((unit-200)*10)
    print(bill)

#Check if a number is leap year (proper condition).
year=int(input("Enter Year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"Leap Year")
        else:
            print(year,"Not Leap Year")
    else:
        print(year,"Leap Year")
else:
    print(year,"Not Leap Year")
