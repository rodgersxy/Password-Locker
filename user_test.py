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
