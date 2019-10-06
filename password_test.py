import unittest 
from password_locker import User, Credentials

class TestUser(Unittest.TestCase):

    #Test that defines test cases for the user class bevaviours

    def setUp(self):

        #set up method to run before each test cases

        self.new_user = User("Ikerriz","Kpasloc11","ikerriz@gmail.com")

    def test_init(self)

      #Test case to test if the object is initialized properly

        self.assertEqual(self.new_user.user_name,"Ikerriz")
        self.assertEqual(self.new_user.password, "Kpasloc11")
        self.assertEqual(self.new_user.email, "ikerriz@gmail.com")

if __name__ == '__main__':
    unittest.main()
