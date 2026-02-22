import random
import string

file_path = "./passwords.txt"

def password(max_char = input("How many characters do you want? (q to quit): ")):
    ascii = string.printable
    ascii_split = list(ascii[:-6])

    match max_char.lower():
        case "q":
            print("Exiting....")
            return exit()
        case _:
            match max_char.isdigit():
                case True:
                    generator = random.choices(ascii_split, k=int(max_char))
                    joined = "".join(generator)
                    print(f"\nPassword generated: {joined}\n")
                case _:
                    print("Invalid Input, make sure to type digits or 'q' to quit")
                    print("Program now exiting...")
                    return exit()
    output = joined
    return output

def pass_confirmation():
    confirm = input("Are you satisfied with the password? (y/n) (q to quit): ")
    match confirm.lower():
        case "n":
            password()
            pass_confirmation()
        case "q":
            confirm = "Cancelled"
            print("Program Cancelled. Exiting....")
            return confirm
        case "y":
            confirm = ""
            return confirm
        case _:
            confirm = "Cancelled"
            print("Invalid output. Exiting....")
            return confirm
    output = confirm
    return output


def enter_email():
    email = input("What email did you use? (q to quit): ")
    match email:
        case "q":
            email = "Cancelled"
            pass
        case "Q":
            email = "Cancelled"
            pass
        case _:
            print(f"\nEmail: {email}\n")
            return email
    output = email
    return output

def email_confirmation():
    confirm = input("Is this Email correct? (y/n) (q to quit): ")
    match confirm.lower():
        case "y":
            confirm = ""
            return confirm
        case "n":
            enter_email()
            email_confirmation()
        case "q":
            confirm = "Cancelled"
            return confirm
    output = confirm
    return output

def file_write():
    with open(file_path, "a") as f:
        f.write("\n")
        f.write(f"Password: {password()}")
        if pass_confirmation() == "Cancelled":
            f.write("\n")
            f.write("^^^^^^CANCELLED^^^^^^")
            exit()
        else:
            pass
        f.write("\n")
        f.write(f"Email: {enter_email()}")
        if email_confirmation() == "Cancelled":
            f.write("\n")
            f.write("^^^^^^CANCELLED^^^^^^")
            exit()
        else:
            pass
        f.write("\n")
        f.write("====================================")

file_write()
print(".")
print(".")
print(".")
print("Successfully created password, check in 'password.txt' in root directory")
