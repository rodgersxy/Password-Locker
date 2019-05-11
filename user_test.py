import unittest #import the unittest module
from user import User #user Class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.user_list = User("Rodgers","Nyakundi","0726746234","rodgersny99@gmail.com","password")


    def test_init(self):
        '''
        test_init test case to test if the object is properly initialized
        '''

        self.assertEqual(self.user_list.first_name,"Rodgers")
        self.assertEqual(self.user_list.last_name,"Nyakundi")
        self.assertEqual(self.user_list.phone_number,"0726746234")
        self.assertEqual(self.user_list.email,"rodgersny99@gmail.com")
        self.assertEqual(self.user_list.password,"password")
if __name__ == '__main__':
    unittest.main()        
