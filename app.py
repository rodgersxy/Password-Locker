#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(fname,lname,phone,email,password):

    new_user = User(fname,lname,phone,email,password)
    return new_user



if __name__ == '__main__':
    main()
