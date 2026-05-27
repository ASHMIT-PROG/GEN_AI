# ====================================
# CONDITIONAL STATEMENTS IN PYTHON
# ====================================

# ------------------------------------
# 1. if STATEMENT
# ------------------------------------

age=20

if age>=18:
    print("Eligible to vote")


# ------------------------------------
# 2. if-else STATEMENT
# ------------------------------------

num=7

if num%2==0:
    print("Even")

else:
    print("Odd")


# ------------------------------------
# 3. if-elif-else STATEMENT
# ------------------------------------

marks=85

if marks>=90:
    print("Grade A")

elif marks>=75:
    print("Grade B")

elif marks>=50:
    print("Grade C")

else:
    print("Fail")


# ------------------------------------
# 4. NESTED if
# ------------------------------------

age=20
citizen=True

if age>=18:

    if citizen:
        print("Can Vote")

    else:
        print("Not Citizen")

else:
    print("Underage")
    '''

    Outer if
│
├── True → Inner if
│          │
│          ├── True  → Can vote
│          └── False → Not citizen
│
└── False → Underage
'''

# ------------------------------------
# COMPARISON OPERATORS
# ------------------------------------

print(5==5)
print(5!=3)
print(10>5)
print(2<5)
print(5>=5)
print(3<=5)


# ------------------------------------
# LOGICAL OPERATORS
# ------------------------------------

# and
print(5>2 and 10>5)

# or
print(5>10 or 10>5)

# not
print(not 5>2)


# ------------------------------------
# LOGIN SYSTEM
# ------------------------------------

username="admin"
password="1234"

if username=="admin" and password=="1234":
    print("Login Successful")

else:
    print("Invalid Credentials")


# ------------------------------------
# POSITIVE / NEGATIVE / ZERO
# ------------------------------------

num=-5

if num>0:
    print("Positive")

elif num<0:
    print("Negative")

else:
    print("Zero")


# ------------------------------------
# LARGEST NUMBER
# ------------------------------------

a=10
b=25

if a>b:
    print("a is greater")

else:
    print("b is greater")


# ------------------------------------
# AGE CHECK
# ------------------------------------

age=16

if age>=18:
    print("Adult")

else:
    print("Minor")


# ------------------------------------
# PASS / FAIL
# ------------------------------------

marks=35

if marks>=40:
    print("Pass")

else:
    print("Fail")


# ------------------------------------
# DIVISIBLE BY 5
# ------------------------------------

num=25

if num%5==0:
    print("Divisible by 5")

else:
    print("Not divisible by 5")


# ------------------------------------
# MULTIPLE CONDITIONS
# ------------------------------------

x=10

if x>5 and x<20:
    print("Inside Range")

else:
    print("Outside Range")


# ------------------------------------
# BOOLEAN CONDITIONS
# ------------------------------------

is_logged_in=True

if is_logged_in:
    print("Welcome User")

else:
    print("Please Login")


# ------------------------------------
# IMPORTANT RULES
# ------------------------------------

# 1. Colon (:) compulsory
# 2. Indentation compulsory
# 3. Use == for comparison
# 4. if condition True -> code runs
# 5. else runs when condition False