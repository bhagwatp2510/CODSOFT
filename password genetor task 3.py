import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
  
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# prompt user for desired password length
length = int(input("Enter the desired lrngth of yur  password : "))

# generate password and display on screen
password = generate_password(length)
print("Password you asked is: ", password)