#!/usr/bin/env python
# coding: utf-8

# # PASSWORD GENERATOR

# In[ ]:


import random
import string

def generate_password(length, complexity):
    if complexity == 'low':
        chars = string.ascii_letters + string.digits
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        return "Invalid complexity level!"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        length = int(input("Enter the length of the password: "))
        complexity = input("Enter the complexity level (low/medium/high): ")

        password = generate_password(length, complexity.lower())
        print("Generated Password:", password)

        another_generation = input("Do you want to generate another password? (yes/no): ")
        if another_generation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




