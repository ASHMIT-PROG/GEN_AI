print('''
------ UNIT CONVERTER ------

a. KM to Meter
b. Meter to KM
c. KG to Gram
d. Celsius to Fahrenheit
''')

value=float(input("Enter value: "))
operator=input("Enter operator: ")

if(operator=="a"):
    print(f"{value} KM = {value*1000} Meter")

elif(operator=="b"):
    print(f"{value} Meter = {value/1000} KM")

elif(operator=="c"):
    print(f"{value} KG = {value*1000} Gram")

elif(operator=="d"):
    print(f"{value} Celsius = {(value*9/5)+32} Fahrenheit")   

else:
    print("Invalid Operator")