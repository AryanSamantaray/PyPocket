import string
import secrets

l=input("Are letters allowed ? y/n").lower()
num=input("Are numbers allowed ? y/n").lower()
pwd_len=int(input("Enter password length"))
special=input("Are special charecters allowed ? y/n").lower()
any_ex=input("anything you wanna exclude?")

if l in ("yes","y"):
    print("include letters")
if num in ("yes","y"):
    print("include numbers")
if special in ("yes","y"):
    print("include special charecters")
print(f"length of the password is {pwd_len}")

characters = ""

if l in ("yes", "y"):
    characters += string.ascii_letters
if num in ("yes", "y"):
    characters += string.digits
if special in ("yes", "y"):
    characters += string.punctuation

filter_char = ""
for character in characters:
    if character not in any_ex:
        filter_char+=character

characters=filter_char

if not characters:
    print("Error: choose at least one character type and don't exclude everything.")
else:
    pwd = ""
    for i in range(pwd_len):
        pwd += secrets.choice(characters)

    print(pwd)