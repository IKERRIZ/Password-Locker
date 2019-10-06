import unittest 
from password_locker import User 

class TestUser(unittest.TestCase):

    #Test that defines test cases for the user class bevaviours

    def setUp(self):

     #set up method to run before each test cases

        self.new_user = User("Ikerriz","Kpasloc11","ikerriz@gmail.com")

    def test_init(self):

    #Test case to test if the object is initialized properly

        self.assertEqual(self.new_user.user_name,"Ikerriz")
        self.assertEqual(self.new_user.password, "Kpasloc11")
        self.assertEqual(self.new_user.email, "ikerriz@gmail.com")

    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)



    def test_save_multiple_user(self):
        '''
        Test to check whether we can save multiple user objects.
        '''
        
        self.new_user.user_save()
        test_user = User("Faith","0727995270","faith@gmail.com")
        test_user.user_save()
        self.assertEqual(len(User.user_list),2) 
        self.assertEqual(len(User.user_list),2)


    def test_display_users(self):
        self.assertEqual(User.test_display_users(),User.user_list)


class TestCredentials(unittest.TestCase):
    """
    Test that define test cases for credentials.
    """
    def setUp(self):
        """ 
        set up method to run before each test cases
        """
        self.new_credential = Credentials("facebook","usher.junior", "usr24")
        self.new_credential = Credentials("instagram","junior ashley", "547368")

    def test_init(self):
        """
        Test case to test if the object is initialized properly.
        """

        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.account_username,"usher.junior")
        self.assertEqual(self.new_credential.account_password,"usr24")
        self.assertEqual(self.new_credential.account_name,"instagram")
        self.assertEqual(self.new_credential.account_username,"junior ashley")
        self.assertEqual(self.new_credential.account_password,"547368")




if __name__ == '__main__':
    unittest.main()
