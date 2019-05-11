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

    def delete_credential(self):

        Credential.credential_list.remove(self)

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):

        gen_pass=''.join(random.choice(char) for _ in range(size))

        return gen_pass

    @classmethod
    def find_by_email(cls,number):

        for credential in cls.credential_list:
            if credential.email == number:
                return credential

    @classmethod
    def display_credential(cls):

        return cls.credential_list               
