import random
import string

file_path = "./passwords.txt"

class Answer:
    def __init__ (self, reply, repeat):
        self.reply = reply
        self.repeat = repeat

    def confirmation(self):
        match self.reply.lower():
            case "y":
                print("Test yes")
                pass
            case "n":
                match self.repeat:
                    case Password.password:
                        print("Generating new password...")
                        Password.password()
                        Password.confirmation()
                    case Email.email:
                        Email.enter_email()
                        Email.confirmation()
            case "q":
                print("Exiting...")
                exit()

class Password(Answer):
    def __init__ (self, max_char, reply, repeat):
        super().__init__(reply,repeat)
        self.max_char = max_char

    def password(self):
        ascii = string.printable
        ascii_split = list(ascii[:-6])

        match self.max_char.lower():
            case "q":
                print("Exiting....")
                return exit()
            case _:
                match self.max_char.isdigit():
                    case True:
                        generator = random.choices(ascii_split, k=int(self.max_char))
                        joined = "".join(generator)
                        print(f"\nPassword generated: {joined}\n")
                    case _:
                        print("Invalid Input, make sure to type digits or 'q' to quit")
                        print("Program now exiting...")
                        return exit()
        output = joined
        return output

class Email(Answer):
    def __init__ (self, email, reply, repeat):
        super().__init__(reply,repeat)
        self.email = email

    def enter_email(self):
        match self.email:
            case "q":
                self.email = "Cancelled"
                pass
            case "Q":
                self.email = "Cancelled"
                pass
            case _:
                print(f"\nEmail: {self.email}\n")
                return self.email
        output = self.email
        return output

password_generate = Password(max_char = input("How many characters in password? (q to quit): "),
                             reply = input("Are you satisfied with the result? (y/n) (q to quit): "),
                             repeat = Password.password)

password_generate.password()

create_email = Email(email = input("What email did you use? (q to quit): "),
                     reply = input("Is this email correct? (y/n) (q to quit): "),
                     repeat = Email.enter_email)
create_email.enter_email()
