import random
import string



class User:

 #Class that generates new instances of the user

  user_list = [] # empty list
  def __init__(self, user_name, password, email):
      self.user_name = user_name
      self.password = password
      self.email = email

  def user_save(self):
       '''
      Function to save a newly created user instance
       '''
       User.user_list.append(self)

class Credentials:
     # class that defines user credential

    credential_list = []
    user_credential_list = []

    @classmethod
    def check_user_exist(cls,user_name,password):
        '''
        method to check if the user exist from user list
        '''
        for user in User.user_list:
            if user_name == user_name and user.password == password:
                current_user =user_name
            return current_user
    def __init__(self, account_name, user_name, password):
        '''
        method to define the properties for user object
        '''
        self.account_name = account_name
        self.user_name = user_name
        self. password = password

    def save_credential (self):
        '''
        a method  to save user object to user_list
        '''
        Credential.credential_list.append(self)

     @classmethod
    def display_credential(cls, user_name):
        '''
        function to diplay saved account
        '''
        user_credential_list = []
        for  credential in cls.credential_list:
            if credential.user_name == user_name:
                user_credential_list.append(credential)
        return user_credential_list   
