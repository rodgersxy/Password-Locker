#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(fname,lname,phone,email,password):

    new_user = User(fname,lname,phone,email,password)
    return new_user

def create_credential(email,platform,password):

    new_credential =  Credential(email,platform,password)
    return new_credential

def generate_password():
    '''
    Function to genrate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def save_users(user):

    user.save_user()

def save_credential(credential):

    credential.save_credential()

def del_user(user):

    user.delete_user()

def delete_credential(credential):

    credential.delete_credential()

def find_user(number):

    return User.find_by_number(number)

def find_credential(number):

    return Credential.find_by_email(number)

def check_existing_users(number):

    return User.user_exist(number)

def check_existing_credential(number):

    return Credential.credential_exist(number)

def display_users():

    return User.display_users()

def display_credential():

    return Credential.display_credential()

def test_copy_email():

    return User.copy_email()

def test_copy_email():

    return Credential.copy_email()


def main():

    print("Heeey Hallo welcome to your user list. What is your name?")

    user_name = input()                    






if __name__ == '__main__':
    main()
