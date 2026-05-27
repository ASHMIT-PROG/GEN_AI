# =========================
# ARITHMETIC OPERATORS
# =========================

a=10
b=3

# Addition
print(a+b)

# Subtraction
print(a-b)

# Multiplication
print(a*b)

# Division
print(a/b)

# Floor Division
print(a//b)

# Modulus
print(a%b)

# Exponent
print(a**b)



# =========================
# EVEN ODD CHECK
# =========================

num=8

print(num%2)



# =========================
# OPERATOR PRECEDENCE
# =========================

print(2+3*4)

print((2+3)*4)



# =========================
# FLOAT OPERATIONS
# =========================

print(5+2.5)



# =========================
# USER INPUT CALCULATOR
# =========================

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

print(f"Addition       : {x+y}")
print(f"Subtraction    : {x-y}")
print(f"Multiplication : {x*y}")
print(f"Division       : {x/y}")
print(f"Floor Division : {x//y}")
print(f"Modulus        : {x%y}")
print(f"Power          : {x**y}")

# -  - - - - - - - - - - - - -----------------------------------------------------------------------------------
# =========================
# ASSIGNMENT OPERATORS
# =========================

x=10

print(x)



# =========================
# +=
# =========================

x+=5

print(x)



# =========================
# -=
# =========================

x-=3

print(x)



# =========================
# *=
# =========================

x*=2

print(x)



# =========================
# /=
# =========================

x/=4

print(x)



# =========================
# //=
# =========================

x//=2

print(x)



# =========================
# %=
# =========================

x%=3

print(x)



# =========================
# **=
# =========================

x=2

x**=3

print(x)



# =========================
# MULTIPLE ASSIGNMENT
# =========================

a,b,c=10,20,30

print(a,b,c)



# =========================
# SAME VALUE
# =========================

p=q=r=100

print(p,q,r)



# =========================
# VARIABLE SWAP
# =========================

a=10
b=20

a,b=b,a

print(a,b)



# =========================
# COUNTER EXAMPLE
# =========================

score=0

score+=10

print(score)



# =========================
# LOOP SUM
# =========================

total=0

for i in range(1,6):
    total+=i

print(total)

# ----------------------------------------------------------
# =========================
# COMPARISON OPERATORS  (TRUE / FALSE == OUTPUT)
# =========================

print(5==5)

print(5!=3)

print(10>5)

print(2<5)

print(5>=5)

print(3<=5)



# =========================
# VARIABLES
# =========================

age=18

print(age>=18)



# =========================
# STRING COMPARISON
# =========================

print("apple"=="apple")

print("apple"=="Apple")

print("b">"a")



# =========================
# BOOLEAN TYPE
# =========================

print(type(5>3))



# =========================
# CHAINED COMPARISON
# =========================

x=5

print(1<x<10)



# =========================
# LOGIN CHECK
# =========================

password="python123"

print(password=="python123")



# =========================
# ELIGIBILITY CHECK
# =========================

marks=75

print(marks>=40)


# =========================
# LOGICAL OPERATORS
# =========================

# AND
print(5>2 and 10>5)

print(5>2 and 10<5)



# =========================
# OR
# =========================

print(5>10 or 10>5)

print(5<2 or 10<5)



# =========================
# NOT
# =========================

print(not True)

print(not False)

print(not 5>2)



# =========================
# LOGIN SYSTEM
# =========================

username="admin"
password="1234"

print(username=="admin" and password=="1234")



# =========================
# AGE CHECK
# =========================

age=20

print(age>=18 and age<=60)



# =========================
# MULTIPLE CONDITIONS
# =========================

x=10

print(x>5 and x<20 and x!=15)



# =========================
# ELIGIBILITY
# =========================

marks=85
sports=True

print(marks>90 or sports)



# =========================
# STUDENT RESULT
# =========================

marks=75
attendance=85

print(marks>=40 and attendance>=75)



# =========================
# BOOLEAN TYPE
# =========================

print(type(True))
print(type(False))



