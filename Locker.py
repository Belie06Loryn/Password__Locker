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

    pass      