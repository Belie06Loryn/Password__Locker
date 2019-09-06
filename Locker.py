import pyperclip
class Urufunguzo:
    """
    Creating a class to holds new instances 
    """
    user_data = [] #any array for storing users
    def __init__(self,name,fone,names,mail,ibanga):
        """
        Defining all properties that are going to be used
        """
        self.name = name
        self.fone = fone
        self.names = names
        self.mail = mail
        self.ibanga = ibanga

    def bika_user(self):
        """
        This a method to save users into user_data
        """
        Urufunguzo.user_data.append(self)  

    @classmethod 
    def ni_Izina(cls,string):
        """
        This method will search a user according the name that has been entered to search
        """
        for usere in cls.user_data:
            if usere.name == string:
                return usere  

    def siba_user(self):
        """
        This for deleleting a user
        """
        Urufunguzo.user_data.remove(self)    


    @classmethod 
    def reba_user(cls,string):
        """
        This method will check if the user exist
        """
        for usere in cls.user_data:
            if usere.name == string:
                return True
        return False


    @classmethod
    def terura_user(cls,string):
        yabonetse = Urufunguzo.ni_Izina(string)
        pyperclip.copy(yabonetse.mail)      
         

    pass      