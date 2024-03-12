import random

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialchar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '\\', ':', ';', '\'', '"', '<', '>', '.', '?', '/', '~', '`']

characterslist = uppercase + lowercase + digits + specialchar

password = []

while True:
    try:
        length = int(input("> Enter the length of password: "))
        break
    except:
        print("> Enter valid length.")
        continue

for i in range(length):
    randomchar = random.choice(characterslist)
    password.append(randomchar)

print("\n> Generated password: " + "".join(password))
    

