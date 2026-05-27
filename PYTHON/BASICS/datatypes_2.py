import math 

"""
| Category | Data Types              |
| -------- | ----------------------- |
| Numeric  | int, float, complex     |
| Sequence | str, list, tuple, range |
| Mapping  | dict                    |
| Set      | set, frozenset          |
| Boolean  | bool                    |
| Binary   | bytes, bytearray        |
| Special  | NoneType                |


| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor division |
| `%`      | Modulus        |
| `**`     | Power          |

STRING 

#STRING SLICING IN PYTHON

text="PYTHON"

#string[start:end:step]

#start->kaha se start
#end->kaha tak(exclude hota hai)
#step->kitne gap se move

print(text[0:4])
#PYTH

print(text[:4])
#start automatically 0

print(text[2:])
#end automatically last tak

print(text[:])
#puri string copy

print(text[::1])
#har character

print(text[::2])
#PTO
#har 2nd character

print(text[::3])
#PH
#har 3rd character

print(text[1:6:2])
#YHN

print(text[::-1])
#NOHTYP
#reverse string

print(text[::-2])
#NHY
#reverse+skip

#IMPORTANT RULES

#end index exclude hota hai
#default step=1
#negative step=reverse
#step 0 nahi ho sakta
#slicing new string banati hai

--------------------------------------------------------------------------------

#STRING METHODS IN PYTHON

text="python programming"

#upper()->sab uppercase
print(text.upper())
#PYTHON PROGRAMMING

#lower()->sab lowercase
print(text.lower())

#title()->har word ka first letter capital
print(text.title())
#Python Programming

#capitalize()->sirf first letter capital
print(text.capitalize())
#Python programming

#swapcase()->upper ko lower aur lower ko upper
print(text.swapcase())
#PYTHON PROGRAMMING

#replace(old,new)->word replace
print(text.replace("python","java"))
#java programming

#find()->index batata hai
print(text.find("pro"))
#7

#index()->find jaisa but error deta hai agar na mile
print(text.index("pro"))
#7

#count()->kitni baar aaya
print(text.count("m"))
#2

#startswith()->starting check
print(text.startswith("python"))
#True

#endswith()->ending check
print(text.endswith("ing"))
#True

#strip()->extra spaces remove
name="  ash  "
print(name.strip())
#ash

#lstrip()->left spaces remove
print(name.lstrip())

#rstrip()->right spaces remove
print(name.rstrip())

#split()->string ko list me todta hai
print(text.split())
#['python','programming']

#join()->list ko string banata hai
words=["hello","world"]
print(" ".join(words))
#hello world

#isalpha()->sirf alphabets?
print("python".isalpha())
#True

#isdigit()->sirf digits?
print("123".isdigit())
#True

#isalnum()->alphabets+numbers?
print("python123".isalnum())
#True

#isspace()->sirf spaces?
print("   ".isspace())
#True

#islower()->sab lowercase?
print("python".islower())
#True

#isupper()->sab uppercase?
print("PYTHON".isupper())
#True


"""

text = "python"
print(type(text))   

# ------------------------------------------------------

# TYPECONVERSION 
# user input humesha string me aata hai 
# implicit type conversion 
'''
a=5
b=2.5

c=a+b

print(c)
print(type(c))

output : 7.5
<class 'float'>



B) int() Cannot Convert Decimal String Directly
x="5.6"

int(x) - error ayega 

x="5.6"

y=float(x)

z=int(y)

print(z)

'''
#------------------------
# floor 
print (math.floor (5.9))
# output  = 6
print (math.floor(5.2))
#  output = 5
# ================================
# FLOAT FORMATTING IN PYTHON
# ================================

num=12.98765

# 1 digit after decimal
print(f"{num:.1f}")

# 3 digits after decimal
print(f"{num:.3f}")



# ================================
# EXPLANATION
# ================================

# :.1f
# :
# formatting start

# .1
# decimal ke baad 1 digit

# f
# float formatting


# ================================
# MORE EXAMPLES
# ================================

price=99.45678

print(f"{price:.2f}")   # 2 decimal places
print(f"{price:.4f}")   # 4 decimal places



# ================================
# ROUNDING CONCEPT
# ================================

num=5.6789

print(f"{num:.2f}")

# Output:
# 5.68

# Because next digit is 8
# so 7 becomes 8



# ================================
# MULTILINE FORMATTING
# ================================

print("""
Hello
Welcome
Python
""")



# ================================
# MULTILINE WITH VARIABLES
# ================================

name="Ashmit"
age=20
course="Python"

print(f"""
----- STUDENT DETAILS -----

Name   : {name}
Age    : {age}
Course : {course}
""")



# ================================
# RECEIPT PROJECT
# ================================

item="Pizza"
price=299.99
qty=2

print(f"""
------ RECEIPT ------

Item     : {item}
Quantity : {qty}
Price    : ₹{price:.2f}

Total    : ₹{price*qty:.2f}
""")



# ================================
# ALIGNMENT FORMATTING
# ================================

name="Python"

# Left align
print(f"{name:<10}")

# Right align
print(f"{name:>10}")

# Center align
print(f"{name:^10}")



# ================================
# LEADING ZEROS
# ================================

num=7

print(f"{num:03}")

# Output:
# 007



# ================================
# WIDTH FORMATTING
# ================================

num=25

print(f"{num:5}")

# spaces add hoti hain



# ================================
# ESCAPE CHARACTERS
# ================================

print("Hello\nWorld")

print("Name\tAge")



# ================================
# PRACTICE
# ================================

pi=3.14159

print(f"{pi:.2f}")
print(f"{pi:.3f}")

marks=85

print(f"{marks}%")

#------------------------------------

# DICTIONARY 
# =========================
# DICTIONARY IN PYTHON
# =========================

student={
    "name":"Ashmit",
    "age":20,
    "course":"Python"
}

print(student)



# =========================
# ACCESS VALUE
# =========================

print(student["name"])



# =========================
# UPDATE VALUE
# =========================

student["age"]=21

print(student)



# =========================
# ADD NEW KEY
# =========================

student["city"]="Delhi"

print(student)



# =========================
# DELETE KEY
# =========================

del student["course"]

print(student)



# =========================
# LOOP IN DICTIONARY
# =========================

for key in student:
    print(key,student[key])



# =========================
# METHODS
# =========================

print(student.keys())

print(student.values())

print(student.items())

print(student.get("name"))



# =========================
# NESTED DICTIONARY
# =========================

data={
    "user":{
        "name":"Ashmit",
        "age":20
    }
}

print(data["user"]["name"])




