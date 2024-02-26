#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
#Collecting Characters using for loop
for char in range (1, nr_letters + 1):
  password_list.append(random.choice(letters))
for char in range (1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for char in range (1, nr_numbers + 1):
  password_list.append(random.choice(numbers))
# shuffle the characters to randomize the order.
random.shuffle(password_list)
#Converting a list to a String use  ''.join():
password = ''.join(password_list)
print(f"Your password is: {password}")


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#password = ""
# for loop to pick randomly the letters
#for char in range(1, nr_letters +1):
  # we can skip this inter-level and skip it > #random_char = random.choice(letters)
 # password += random.choice(letters)
#for loop to pick randomly the symbols
#for char in range(1, nr_symbols + 1):
 # password += random.choice(symbols)
#for loop to pick randomly the numbers
#for char in range(1, nr_letters):
 # password += random.choice(numbers)
# now we can print the password
#print (password)