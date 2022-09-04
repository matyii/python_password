import string
import random
file = open('password.txt','x')

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


length = int(input("Enter password length: "))
random.shuffle(characters)
password = []
for i in range(length):
	password.append(random.choice(characters))
random.shuffle(password)
print("".join(password))
file.write('password',password)
file.close()

#genpw()