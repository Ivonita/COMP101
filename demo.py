# run using the button in the right hand side corner
# use the terminal 'python3 demo.py'

# define a variable, name
msg = 'Hello'
# print the content () on the terminal
print(msg)

my_name = 'Nathalie'
my_name = 'Anna'
# print the value of a variable
print(my_name)

# string
print('Ivonita')

# Number: Integer or Float
my_age = 36

# or Float
temp = 2.2

# <class 'int'>
print(type(my_age))

## Calculate the year I was born:
my_birthyear = 2023 - 36

current_year = 2023
my_birthyear = current_year - my_age
print(my_birthyear)

## Data type string, integer, float,
#
#boolean,
mentor = True
mentor = False

# list,
my_hobbies = ['running', 'coding', 'eating', 123, False, [1,2,3] ]

# dictionary (dict)
my_pet = {
    'name': 'Susi',
    'animal': 'cat',
    'age': 2,
    'cute': True,
}

my_tweet = {
    'text': 'Hello',
    'date': '2023.01.23'
}

#conditions
#age = int(input("What is your age?"))
#print(type(age))

age = 80

if age < 18:
    print("no entry")
elif age > 65:
    print("reduced entry, 50 off!")
else:
    print("welcome")

print('conditional is done!')

passwort = "1234_passwort"

if passwort == "1234_passwort":
    print("correct")
elif len(passwort) > 7:
    print("is long enough")
elif len(passwort) < 7:
    print("too short")
else:
    print("not correct")

#function

#guests = 2
#bill = 20
#tip = 10

def calculate_split_bill(bill, tip, guests):
    total_bill = bill + (bill *(tip/100))
    split_bill = total_bill / guests
    return split_bill #output

#call funktion with values, storing the return value in a new variable
result_one = calculate_split_bill(20,10,2)
print(result_one)

input_bill = int(input("What is the bill?"))
input_tip = int(input("What is the tip?"))
input_guests = int(input("What is the guests?"))

result_two = calculate_split_bill(input_bill, input_tip, input_guests)
print(result_two)

#Beispiel

def sum(x):
    res = 0
    for i in range(x):
    #[0,1,2,3]
        res+1=i
    return res

#longer to see result:
result_sum = sum(4)
print(result_sum)
#shorter to see result: 
# print(sum(4))



