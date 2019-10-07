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
           save_user(create_user(firstname,password))
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
                   print('Your credentials short codes: c-Create credential, d-Display Credentials, p-Copy Password, ex-Exit')
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
                   elif short_code == 'p':
                       print(' ')
                       chosen_account_name = input('Enter the account name for the credential password to copy: ')
                       copy_credential(chosen_account_name)
                       print('')
                       print('Paste copied account_name password here:')
                       copy = input()
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

