#Task 1---------------------------------

from asyncio import Task


print("Hello World")
print("Okolie Chijioke Henry")

#Task 2------------------------------------



my_var = 12.6
print(my_var)

number = 200
print(number)

my_name = "Okolie Chijioke Henry"
print(my_name)


#Task 3---------------------------------------

# Declaring a raw string #Task 3

name = r"I am Okolie\n Henry\n\tChijioke\b"
print(name)

first_name = "Henry"
surname = "Okolie"
add_name = first_name + ' ' + surname
print(add_name)

#Task 4--------------------------------------

number1 = 54
number2 = 50
add_value = number1 + number2
print(add_value)

number1 = 54
number2 = 50
add_value = number1 - number2
print(add_value)

number1 = 54
number2 = 50
add_value = number1 / number2
print(add_value)

#Task 5---------------------------------------

number = 3
if number == 2:
    print("Number is Two")
else:
    print("Number is not Two")


#Task 6--------------------------------------

number1 = 70
number2 = 75

if number1 > 50 and number2 < 100:
    print("Evaluation is True")


if number1 > 50 and number2 < 100:
    print("Evaluation is True")
else:
    print("Evaluation is False")


name = "python"
if name == "Testify":
    print("Yay!! The string is a Testify Python")

#Task 7---------------------------------------

number = 11

for i in range(number):
    print("Hello World", i)



#Task 8---------------------------------------


number = 10
for i in range(number):
    if i == 2:
        continue
    print("for: number:", i)

for i in range(number):
    if i == 8:
        break
    print("Number:", i)

# Week two

# Task 9

def name():
    print("Hello World")

def test_case():
    pass

name()
test_case()


# Task 10

def invoke(cb):
    cb("Hello world")

hello = lambda : print("Hello world")
hello()

invoke(lambda x: print(x))


# Task 11
def add(numb1, numb2):
    result = numb1+numb2
    print("result", result)

def print_value(name1, name2):
    result = name1 + name2
    return result

abc = print_value("Testify" ' ', "python")
print(abc)


add(20, 25)

# TASK 12
language = "Python"

def greet():
    language = "Java"
    print("language:", language)


greet()

#TASK 13

def reduce(x):

    if x == 1:
        return 1


num = 3
print("Hello world")



# Task14

my_value = "testify"
upper_value = my_value.upper()

print("Upper:", upper_value)



# TASK15

list = ["Fish", "Meat", "Egg", "Butter", "Fruit", "Cheese", "Hem", "Oil"]
print(list)
list.sort()
print(list)

# Task16

books = {
    "Lolita": "Vladimir Nabokov",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "In Search of Lost Time": " by Marcel Proust",
    "Ulysses": "James Joyce"
}
print(books)
books.update({"Pale Fire": "Vladimir Nabokov"})
print("update:", books)

