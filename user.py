import pyperclip
class User:
    """
    Class that generates new instances of usersself.
    """
    pass

    user_list = [] #Empty user lists

    def save_user(self):

        User.user_list.append(self)

    def delete_user(self):

        User.user_list.remove(self)    
