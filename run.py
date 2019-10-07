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
def authenticate_user(firstname, password):
    '''
    Function to authenticate a user
    '''
    authenticated_user = Credential.check_user_exist(firstname, password)
    return authenticated_user

def create_credential(account_name,user_name,password):
    '''
    Function to create a new credential object
    '''
    new_credential = Credential(account_name,user_name,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a created credential
    '''
    Credential.save_credential(credential)
def generate_password():
    '''
    Function to randomly generate password
    '''
    password_generate = Credential.generate_password
    return password_generate
def display_credential(user_name):
    '''
    Function to display credentials
    '''
    return Credential.display_credential(user_name)

def copy_credential(account_name):
    '''
    Function to copy a credential to the clipboard
    '''
    return Credential.copy_credential(account_name)

