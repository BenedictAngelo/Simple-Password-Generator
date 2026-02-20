import os
import random
import string
# must contain special characters
# must contain lower and upper case letters
# must contain digits
file_path = "./passwords.txt"

def password(character_number = input("How many characters do you want? (q to quit): ")):
    input_check = character_number.isdigit()
    ascii = string.printable
    ascii_split = list(ascii[:-6])

    if character_number.lower() == "q":
        exit()
    else:
        pass

    if input_check:
        int_convert = int(character_number)
        generator = random.choices(ascii_split, k=int_convert)
        joined = "".join(generator)
        print()
        print(f"Password generated: {joined}")
        print()
    else:
        print("Invalid Input, make sure to type digits or 'q' to quit")
        print("Program now exiting...")
        exit()
    output = joined
    return output

def pass_confirmation():
    confirm = input("Are you satisfied with the password? (y/n) (q to quit): ")
    print("")
    if confirm.lower() == "n":
        password()
        pass_confirmation()
    elif confirm.lower() == "q":
        confirm = "Canceled"
        print("Exiting....")
        pass
    elif confirm.lower() == "y":
        confirm = ""
        pass
    else:
        confirm = "Canceled"
        print("Invalid output, exiting....")
        pass
    return confirm


def email_confirmation():
    pass_confirm = "y"
    if pass_confirm.lower() == "y":
        email = input("What email did you use?: ")
        print()
        print(f"Email generated: {email}")
        print()
        email_confirm = input("Is this email correct? (y/n): ")
        if email_confirm.lower() == "y":
            pass
        else:
            email_confirmation()
        output = email
        return output


def txt_file_append():
    with open(file_path,"a") as f:
        f.write(f"Password: {password()}")
        f.write("\n")
        if pass_confirmation() == "Canceled":
            f.write("Cancelled^^^^^^^^^^^^^^^\n")
            exit()
        else:
            pass
        f.write(f"Email: {email_confirmation()}")
        f.write("\n")
        f.write("=================================")
        f.write("\n")
    return 

def txt_file_write():
    with open(file_path,"w") as f:
        f.write(f"Password: {password()}")
        f.write("\n")
        if pass_confirmation() == "Canceled":
            f.write("Cancelled^^^^^^^^^^^^^^^\n")
            exit()
        else:
            pass
        f.write(f"Email: {email_confirmation()}")
        f.write("\n")
        f.write("=================================")
        f.write("\n")
    return 



if os.path.exists(file_path):
    txt_file_append()
    print(".")
    print(".")
    print(".")
    print("Successfully added a password, check 'password.txt' at the root directory")
else:
    txt_file_write()
    print(".")
    print(".")
    print(".")
    print("Successfully created 'password.txt' at root directory")
    print(".")
    print(".")
    print(".")
    print("Successfully added a password, check 'password.txt' at the root directory")
    


