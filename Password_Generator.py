import random
import string
# must contain special characters
# must contain lower and upper case letters
# must contain digits

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
        print(joined)
        print()
    else:
        print("Invalid Input, make sure to type digits or 'q' to quit")
    return joined

def pass_confirmation():
    confirm = input("Are you satisfied with the password? (y/n) (q to quit): ")
    if confirm.lower() == "n":
        password()
        pass_confirmation()
    elif confirm.lower() == "q":
        print("Exiting...")
        exit()
    elif confirm.lower() == "y":
        pass
    else:
        print("Invalid output, exiting...")
        exit()
    return confirm


def email_confirmation():
    pass_confirm = "y"
    if pass_confirm.lower() == "y":
        email = input("What email did you use? ")
        print()
        print(email)
        print()
        email_confirm = input("Is this email correct? (y/n): ")
        if email_confirm.lower() == "y":
            pass
        else:
            email_confirmation()
        return email


with open("/home/angelo/Documents/passwords.txt","a") as f:
    f.write("=================================")
    f.write("\n")
    f.write(f"Password: {password()}")
    f.write("\n")
    pass_confirmation()
    f.write(f"Email: {email_confirmation()}")
    f.write("\n")
    f.write("=================================")
    f.write("\n")

