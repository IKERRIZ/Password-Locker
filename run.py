#!/usr/bin/env python3.6
from password_locker import User, Credentials


def create_user(firstname, password):
    '''
    Function to create a new user
    '''
    new_user = User(firstname, password)
    return new_user 

def user_save(user):
    '''
    Function to save a new user
    '''
    user.user_save()
def authenticate_user(firstname, password):
    '''
    Function to authenticate a user
    '''
    authenticated_user = Credentials.check_user_exist(firstname, password)
    return authenticated_user

def create_credential(account_name,user_name,password):
    '''
    Function to create a new credential object
    '''
    new_credential = Credentials(account_name,user_name,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a created credential
    '''
    Credentials.save_credential(credential)
def delete_credential(credential):
    '''
    Function that deletes credentials
    '''
    credential.delete_credential()
def check_credential_exist(account_name):
    '''
    Function that checks if a credential account exist
    '''
    return Credentials.credential_exist(account_name)

def generate_password():
    '''
    Function to randomly generate password
    '''
    password_generate = Credentials.generate_password
    return password_generate

def find_by_account_name( account_name):

    return Credentials.find_by_account_name(account_name)


def display_credential(user_name):
    '''
    Function to display credentials
    '''
    return Credentials.display_credential(user_name)

# def copy_credential(account_name):
#     '''
#     Function to copy a credential to the clipboard
#     '''
#     return Credentials.copy_credential(account_name)

def main():
   print(' ')
   print('Welcome to Password Locker.')
   while True:
       print(' ')
       print("-"*40)
       print('Use these short codes: cr-Create Password-Locker account,  log-Login, ex-Exit')
       short_code = input('Enter short code here: ').lower().strip()
       if short_code == 'ex':
           break
       elif short_code == 'cr':
           print("-"*40)
           print(' ')
           print('To create a new account:')
           firstname = input('Choose a firstname - ').strip()
           password = input('Choose a password - ').strip()
           user_save(create_user(firstname,password))
           print(" ")
           print(f'Your Password-Locker account firstname is : {firstname}  and password is: {(password)}')
       elif short_code == 'log':
           print("-"*40)
           print(' ')
           print('To login:')
           firstname = input('Enter your Password-Locker username - ').strip()
           password = str(input('Enter your password - '))
           user_authenticated = authenticate_user(firstname,password)
           if user_authenticated == firstname:
               print(" ")
               print(f'Welcome {firstname}. You have successfully logged in. Choose short code to continue')
               print(' ')
               while True:
                   print("-"*40)
                   print('Your credentials short codes: c-Create credential, d-Display Credentials, dc-Delete Credential, ex-Exit')
                   short_code = input('Enter short code: ').lower().strip()
                   print("-"*40)
                   if short_code == 'ex':
                       print(" ")
                       print(f'Goodbye {firstname}')
                       break
                   elif short_code == 'c':
                       print(' ')
                       print('Enter your credential account information:')
                       account_name = input('Enter the account name - ').strip()
                       user_name = input('Enter your username - ').strip()
                       password = input('Enter your password - ').strip()
                       while True:
                           print(' ')
                           print("-"*40)
                           print('Select option for entering a password:  e-Enter your own password, g-Generate a password ,ex-Exit')
                           passwrd_select = input('Enter an option: ').lower().strip()
                           print("-"*40)
                           if passwrd_select == 'e':
                               print(" ")
                               password = input('Enter your password: ').strip()
                               break
                           elif passwrd_select == 'g':
                               password = generate_password()
                               break
                           elif passwrd_select == 'ex':
                               break
                           else:
                               print('Incorrect entry. Try again.')
                       save_credential(create_credential(account_name,user_name,password))
                       print(' ')
                       print(f'Credential Created: Account Name: {account_name} - User name: {user_name} - Password: {password}')
                       print(' ')
                   elif short_code == 'd':
                       print(' ')
                       if display_credential(user_name):
                           print('Your credential account list:')
                           print(' ')
                           for credential in display_credential(user_name):
                               print(f'Account Name: {credential.account_name}-User Name: {credential.user_name}-Password: {credential.password}')
                           print(' ')
                       else:
                           print(' ')
                           print("No credential saved")
                           print(' ')
                   elif short_code == 'dc':
                       print(' ')
                       chosen_account_name = input('Enter the account name for the credential  account you want to delete: ')
                       if check_credential_exist(chosen_account_name):
                           delete_credential(find_by_account_name(chosen_account_name))
                       print('')
                       print('Your credential {chosen_account_name} has been deleted succeessfully:')
                   else:
                       print('Incorrect entry.Try again.')
           else:
               print(' ')
               print('Incorrect entry. Try again or Create an Account.')        
       else:
           print("-"*40)
           print(' ')
           print('Incorrect entry. Try again.')
                
if __name__ == "__main__":
   main()

