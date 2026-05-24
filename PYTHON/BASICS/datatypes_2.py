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




"""