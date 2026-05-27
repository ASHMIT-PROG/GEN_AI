import math

'''
Simple Calculator
'''

a=float(input("Enter value of a : "))
b=float(input("Enter value of b : "))

print("Choose Operator")

print("""
+  = Addition
-  = Subtraction
*  = Multiplication
/  = Division
// = Floor Division
** = Power
""")

operator=input("Enter operator : ")

if(operator=="+"):
    print(f"Addition = {a+b}")

elif(operator=="-"):
    print(f"Subtraction = {a-b}")

elif(operator=="*"):
    print(f"Multiplication = {a*b}")

elif(operator=="/"):
    if(b!=0):
        print(f"Division = {a/b}")
    else:
        print("Division by zero not possible")

elif(operator=="//"):
    if(b!=0):
        print(f"Floor Division = {a//b}")
    else:
        print("Division by zero not possible")

elif(operator=="**"):
    print(f"{a} to the power {b} = {a**b}")

else:
    print("Invalid Operator")
    