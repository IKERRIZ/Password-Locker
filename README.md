## PASSWORD_LOCKER
An application that allows users to generate and store passwords for various accounts.
### Created by Faith Okoth
### Description
An application that allows us to generate and store passwords for various accounts. Password Locker stores a user's password for their various accounts. It also allows the user to generate random password and various credentials and stores them. This ensures that a user's password is strong enough and stored safely for easy retrieval.


### User Specifications
* In order to create an account with a user's details,log in and input password
* Store user,s login credentials
* Generate a password for a new account

### Behaviours
|Behaviour   | Input    | Output  |
|------------|----------|---------|
|Create user account | User_name and password|Your password-locker (name)  and (password)|
|Display input prompt for login|User_name and password| Welcome (name) successfully logged in. Choose short code to continue|
|Display codes for credentials |Successfully logged in|Select short code: ccd - create credential, dc - display Credentials, dl - delete credential, cp - copy credential, ex - exit|
|Display input prompt for creating a credential|Type in ccd short code and enter the site name, site-account username and password|Displays the site name, site-account-username and password|
|Display a list of credentials| Type dc short code |Displays a list of saved account credentials|
|Display input prompt for which credential account to delete|Type  dl short code |Deletes the selected credential account|
|Display input prompt for which credential to copy|Type  cp short code|Copies the credential|
|Exit application|Type in ex short code|Exit in current location|

## SetUp Requirement

# Prerequisites
* Pyperclip
* Xclip
 ## Technologies used
 Python3.6

 ## Cloning
* In your terminal:

  $ git clone https://github.com/IKERRIZ/Password-Locker/
  $ cd Password-Locker
 ## Running the Application
* To run the application, in your terminal:

  $ chmod +x run.py
  $ ./run.py
## Testing the Application
* To run the tests for the classes

  $ python3.6 user_credential_test.py

## Support and contact details
If you run into any issues or have questions, ideas or concerns contact okothfaith94@gmail.com

License
MIT Copyright (c) 2019 IKERRIZ
