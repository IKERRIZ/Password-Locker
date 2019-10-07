import random
import string




class User:

 #Class that generates new instances of the user

  user_list = [] # empty list
  def __init__(self, user_name, password):
      self.user_name = user_name
      self.password = password


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
        Credentials.credential_list.append(self)

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
    def generate_password (self,size=5, char=string.ascii_lowercase+string.ascii_uppercase+string.digits):
            '''
            function to generate random password
            
            '''
            password_generate = "".join(random.choice(char) for _ in range(size))
            return password_generate

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Function that finds a credential based on the site_name
        '''
        for credential in cls.credential_list:
            if credential.account_name ==  account_name:
                return credential
    # @classmethod
    # def copy_credential(cls,account_name):
    #     '''
    #     Function that copies a credential
    #     '''
    #     find_credential = Credentials.find_by_account_name(account_name)
    #     return pyperclip.copy(find_credential.password)
    

                

