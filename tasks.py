# # assignment 3

# q1
def print_twinkle():
    lines = [
        "Twinkle, twinkle, little star,",
        "                  How I wonder what you are!",
        "                              Up above the world so high,",
        "                              Like a diamond in the sky.",
        "Twinkle, twinkle, little star,",
        "                  How I wonder what you are!",
    ]

    for line in lines:
        print(line)
    print()

print_twinkle()

# #q2
# import sys
# print(sys.version)

# #q3
# from datetime import datetime
# print(datetime.now())

#q4
# import math
# r =float(input("enter : "))
# a = math.pi * r**2
# print(a)

# q5

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{last_name} {first_name}"
print("Reversed name:", full_name)

# q6
num1 = input("enter 1st number: ")
num2= input("enter 2nd number: ")
print(num1+ num2)

# q7


marks = []
total_marks = 0

for i in range(5):
    subject_mark = float(input(f"Enter the marks for subject {i + 1}: "))
    marks.append(subject_mark)
    total_marks += subject_mark

percentage = (total_marks / (5 * 100)) * 100

if percentage >= 90:
    print( "A+")
elif percentage >= 80:
    print("A")
elif percentage >= 70:
    print("B")
elif percentage >= 60:
    print("C")
elif percentage >= 50:
    print("D")
else:
    print("F")
    
grade = calculate_grade(percentage)
print(percentage , grade)

# q8
num = int(input("enter number"))
if num%2==0:
    print("even")
else:
    print("odd")
    

# #q9
list1 = [1,'sd' ,'err' ,True , 89 , 0.9 , False, 50.22,1,True]
# print(len(list1))

# #q10
# sum=0
# for i in list1:
#     if type(i) == int or type(i) == float:
#         sum=i+sum
# print(sum)

# #q11
# list2 = [56,78,1,0,3.5,98.2]
# list2.sort()
# print(list2[-1])

# #q12
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# for i in a:
#     if i<5:
#         print(i)

# #assignment 4


# q1
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

x = int(input("enter number : "))
y = int(input("enter number : "))
op = input("select operator : ")
if op == "+":
    print(add(x,y))
elif op=="-":
    print(subtract(x,y))
elif op=="*":
    print(multiply(x,y))
elif op=="/":
    print(divide(x,y))
elif op=="^":
    print(power(x,y))
else:
    print('error')

# q2
# have_num=False
# for i in list1:
#     if type(i) == int or type(i) == float:
#         have_num =True
# print(have_num)

# #q3
# pet = {'Name' : 'Ken',
#        'Breed' : 'German Shepherd'}
# pet['Age'] = '5'

# #q4
# mixed = {
#     'Name' : 'Mahshid',
#     'English' : 98,
#     'Maths' : 78,
#     'Physics' : 65.5,
#     'Chemistry' : 85
# }
# sum = 0
# for key in mixed:
#     if (type(mixed[key])== int or type(mixed[key])== float):
#         sum = mixed[key] + sum
# print(sum)

#q5

list1 = [1,'sd' ,'err' ,True , 89 , 0.9 , False, 50.22,1,True]
list= [1,'sd' ,'err' ,True , 89 , 0.9 , False, 50.22,1,True]
index=0
for i in list:
    list2 =list1
    del list2[index]
    if i in list2:
        print(str(i) + " has a duplicate")

# q6
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

key_to_check = 'age'

if key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")