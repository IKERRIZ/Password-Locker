import unittest 
from password_locker import User, Credentials


class TestUser(unittest.TestCase):

    #Test that defines test cases for the user class bevaviours

    def setUp(self):
        
     #set up method to run before each test cases

        self.new_user = User("Ikerriz","7995")

    def tearDown(self):
        User.user_list = []

    def test_init(self):

    #Test case to test if the object is initialized properly

        self.assertEqual(self.new_user.user_name,"Ikerriz")
        self.assertEqual(self.new_user.password, "7995")

    def test_user_save(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.user_save()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    Test that define test cases for credentials.
    """
    def check_user_exist(self):
        '''
        Method to test check user functionility.
        '''
        self.new_user = User('faith','7995')
        self.new_user.save_user()
        user2 = User('jane', 'abc301')
        user2.save_user()
        for user in User.user_list:
            if user.firstname == user2.firstname and user.password == user2.password:
                current_user = user.firstname
                return current_user
        self.assertEqual(current_user, Credentials.check_user_exist(user2.password, user2.firstname))
    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credentials('twitter','faith','7995')
    def test__init__(self):
        '''
        test__init__ test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name,'twitter')
        self.assertEqual(self.new_credential.user_name,'faith')
        self.assertEqual(self.new_credential.password,'7995')

    def test_save_credential(self):
        '''
        Test to confirm if the new credential is saved to the credentials list
        '''
        self.new_credential.save_credential()
        instagram = Credentials('Instagram','faith','7995')
        instagram.save_credential()
        self.assertEqual(len(Credentials.credential_list),7)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.Credential_list = []
        User.user_list = []

    def test_display_credential(self):
        '''
        Test to check if credentials display method displays
        '''
        self.new_credential.save_credential()
        instagram = Credentials('Instagram','faith','7995')
        instagram.save_credential()
        facebook = Credentials('Facebook','neymar','far785')
        facebook.save_credential()
        self.assertEqual(len(Credentials.display_credential(instagram.user_name)), 2)

    def test_find_by_account_name(self):
        '''
        Test method for finding a credential user_name
        '''
        self.new_credential.save_credential()
        instagram = Credentials('Instagram','faith','7995')
        instagram.save_credential()
        credential_exists = Credentials.find_by_account_name('Instagram')

    # def test_copy_credential(self):
    #     '''
    #     Test method for copy credential functionality
    #     '''
    #     self.new_credential.save_credential()
    #     instagram = Credentials('Instagram','faith','7995')
    #     instagram.save_credential()
    #     find_credential = None
    #     for credential in Credentials.user_credential_list:
    #         find_credential =Credentials.find_by_account_name(credential.account_name)
    #         return pyperclip.copy(find_credential.password)
    #         Credentials.copy_credential(self.new_credential.account_name)
    #     self.assertEqual('7995',pyperclip.paste())
    #     print(pyperclip.paste())

    



if __name__ == '__main__':
    unittest.main()
