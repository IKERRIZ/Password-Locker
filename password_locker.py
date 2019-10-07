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
    def check_user_exist(cls,user_name,password)
    '''
    method to check if the user exist from user list
    '''
    for user in User.user_list:
            if user_name == user_name and user.password == password:
                current_user =user_name
        return current_user
