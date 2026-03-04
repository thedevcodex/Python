#Find the largest of three numbers.
a=10
b=20
c=15
if (a>b) and (a>c):
    print("A is Greater:",a)
elif (b>a) and (b>c):
    print("B is Greater:",b)
else:
    print("C is Greater:",c)
print("-------------------------------------------------------")
#Check if a number is between 10 and 50.
num=11
if (num>=10) and (num<=50):
    print(True)
else:
    print(False)
print("-------------------------------------------------------")
'''Grade system:

90+ → A

75–89 → B

50–74 → C

Below 50 → Fail'''
score=45
if (score>=90):
    print("Grade: A")
elif (score>=75) and (score<=89):
    print("Grade: B")
elif (score>=50) and (score<=74):
    print("Grade: C")
else:
    print("Fail")
print("-------------------------------------------------------")
#Check if a number is divisible by both 3 and 5.
num=15
if (num%3==0) and (num%5==0):
    print(num,"is divisible by 3 and 5")
else:
    print(num,"is not divisible by 3 and 5")
print("-------------------------------------------------------")
#Check if a number is divisible by 3 or 5.
num=20
if (num%3==0):
    print("divisible by 3")
elif (num%5==0):
    print("Divisible by 5")
else:
    print("Not divisible by 3 and 5")
print("-------------------------------------------------------")
#Check whether a character is vowel or consonant.
char="b"
vowels="aeiouAEIOU"
if char in vowels:
    print("Vowel")
else:
    print("Consonant")
print("-------------------------------------------------------")
#Simple calculator (+, -, *, / using condition).
num1=10
num2=2
sign="/"
if sign=="+":
    print(num1+num2)
elif sign=="-":
    print(num1-num2)
elif sign=="*":
    print(num1*num2)
else:
    print(num1/num2)
print("-------------------------------------------------------")
#Check if a number is multiple of 7.
num=14
if (num%7==0):
    print("Yes Multiple of 7")
else:
    print("Not Multiple of 7")
print("-------------------------------------------------------")
'''Check if temperature is:

Below 20 → Cold

20–35 → Normal

Above 35 → Hot'''
temp=35
if temp<20:
    print("cold")
elif (temp>=20) and (temp<35):
    print("Normal")
else:
    print("Hot")
print("-------------------------------------------------------")
#Check if a number is two-digit or not.
number=23
final=abs(number)
if (final>=10) and (final<=99):
    print("Two digit")
else:
    print("Not two digit")
