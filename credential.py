import pyperclip
import string
import random
class Credential:
    """
    Class that generate new instances of credentials.
    """
    pass

    credential_list = [] #empty credential_list

    def save_credential(self):

        Credential.credential_list.append(self)
