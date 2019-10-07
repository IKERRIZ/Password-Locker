!/usr/bin/env python3.6
from password_locker import User, Credentials

def create_user(firstname,password):
    '''
    Function to create a new user
    '''
    new_user = User(firstname, password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
