import unittest #this is the unittest module
from credential import Credential

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviour.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):

        '''
        Set up method to run before each test case.
        '''

    def test_init(self):
        '''
        Test_init test case to test if object are initialize.
        '''

        self.assertEqual(self.credential_list.platform,"Instagram")
if __name__ == '__main__':
    unittest.main()          
