import pyperclip
class Credential:
    """
    This class is gona hold institance for accounts
    """
    credo_data = [] #any array for storing users
    def __init__(self,konti,username,password):
        """
        Defining all properties that are going to be used
        """
        self.konti = konti
        self.username = username
        self.password = password


    def bika_konti(self):
        """
        This a method to save account 
        """
        Credential.credo_data.append(self) 


    @classmethod
    def konti_zose(cls):
        """
        This for displaying all accounts
        """
        return cls.credo_data


    @classmethod
    def search_konti(cls,string):
        """
        This method will search a credentials according the username that has been entered to search
        """
        for usere in cls.credo_data:
            if usere.username == string:
                return usere


    @classmethod
    def terura_konti(cls,string):
        yabonetse = Credential.search_konti(string)
        pyperclip.copy(yabonetse.username)


    @classmethod
    def genzura_neza_konti(cls,string):
        """
        this method is for see if the account exists
        """
        for usere in cls.credo_data:
            if usere.username == string:
                return True
        return False

    def delete_konti(self):
        """
        This for deleleting an account
        """
        Credential.credo_data.remove(self)    