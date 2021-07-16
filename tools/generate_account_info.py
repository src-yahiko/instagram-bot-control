import random
import string
from create_mailbox import generate as generate_email
from randomuser import RandomUser

def generate_password():
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(12))  

def generate():
    user = RandomUser({'nat':'ca'})
    username = user.get_first_name()[0:2][::-1] + user.get_username()
    return({
        "fullname" : user.get_full_name(),
        "username" : username,
        "password" : generate_password(),
        "email"    : generate_email(username)
    })

if __name__ == '__main__':
    print(generate())
    exit(0)