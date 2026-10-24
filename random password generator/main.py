l=input("Are letters allowed ? y/n").lower()
num=input("Are numbers allowed ? y/n").lower()
pwd_len=int(input("Enter password length"))
if l in ("yes","y"):
    print("include letters")
if num in ("yes","y"):
    print("include numbers")
print(f"length of the password is {pwd_len}")