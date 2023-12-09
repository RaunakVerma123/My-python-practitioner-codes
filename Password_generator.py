import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','*','(',')','+']

nr_letters=int(input("How many letters would you like to have in your password?\n"))
nr_numbers=int(input("How many numbers would you like to have in your password?\n"))
nr_symbols=int(input("How many symbols would you like to have in your password?\n"))

pw_letters=[]
pw_numbers=[]
pw_symbols=[]

for letter in range(nr_letters):
    random_letter=random.choice(letters)
    pw_letters.append(random_letter)

for number in range(nr_numbers):
    random_numbers=random.choice(numbers)
    pw_numbers.append(random_numbers)

for symbol in range(nr_symbols):
    random_symbols=random.choice(symbols)
    pw_symbols.append(random_symbols)

combination=pw_letters+pw_numbers+pw_symbols
password_list=random.sample(combination,len(combination))

password=''
for i in password_list:
    password+=i

print(password)