import pyperclip
import unittest
from Locker import Urufunguzo
from Credentials import Credential


#Test for Creating User
class Genzura(unittest.TestCase):
    """
    this class it gona check if application behaviour are driven as how it surppose to be driven
    """

    def setUp(self):
        self.user = Urufunguzo("Aline","078112","Alibebe","alib@gmail.com","123")

    def test_init(self):
        self.assertEqual(self.user.name,"Aline")
        self.assertEqual(self.user.fone,"078112")
        self.assertEqual(self.user.names,"Alibebe")
        self.assertEqual(self.user.mail,"alib@gmail.com")
        self.assertEqual(self.user.ibanga,"123")

    def test_bika_user(self):
        """
        this method test if the user that you have entered has bee saved into database
        """
        self.user.bika_user()
        self.assertEqual(len(Urufunguzo.user_data),1) 

    def tearDown(self):
        Urufunguzo.user_data = []


    def test_bika_benshi_user(self):
        """
        this method check if we can save more than one users
        """
        self.user.bika_user()
        user_s = Urufunguzo("Brenda","078883078","Mwiza","brenda@gmail.com","1234")
        user_s.bika_user()
        self.assertEqual(len(Urufunguzo.user_data),2)

    def test_shaka_user(self):
        """
        this method is for searching any user by name
        """
        self.user.bika_user()
        user_s = Urufunguzo("Brenda","078883078","Mwiza","brenda@gmail.com","1234")
        user_s.bika_user()

        shaka_user = Urufunguzo.ni_Izina("Brenda") 
        self.assertEqual(shaka_user.mail,user_s.mail) 

    def test_siba_user(self):
        """
        This is for testing if delete function can delete a user
        """
        self.user.bika_user()
        user_s = Urufunguzo("Brenda","078883078","Mwiza","brenda@gmail.com","1234")
        user_s.bika_user()

        self.user.siba_user()
        self.assertEqual(len(Urufunguzo.user_data),1)          


    def test_niba_user(self):
        """
        This is for testing if the user exists
        """
        self.user.bika_user()
        user_s = Urufunguzo("Brenda","078883078","Mwiza","brenda@gmail.com","1234")
        user_s.bika_user()

        arimo = Urufunguzo.reba_user("Aline")
        self.assertTrue(arimo)             
        

    def test_login(self):

        self.user.bika_user()
        user_s = Urufunguzo("Brenda","078883078","Mwiza","brenda@gmail.com","1234")
        user_s.bika_user()

        arimo = Urufunguzo.login("Alibebe","123")
        self.assertTrue(arimo)


    def test_terura_user(self):
        """
        Test to confirm the copy action
        """
        self.user.bika_user()
        Urufunguzo.terura_user("Aline")

        self.assertEqual(self.user.mail,pyperclip.paste())

    def test_user_bose(self):
        '''
        test to check if we can view our user that has been created
        '''
        self.assertEqual(Urufunguzo.user_bose(), Urufunguzo.user_data)
    




#################################################################################################################
#Test for Creating Credentials
class Genzura_konti(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behavious
    """
    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.urugero = Credential("Instagram", "Alibebe", "112") #create credential object


    def test_init(self):
        """
        test_init test case to test if the object is instantiated properly
        """
        self.assertEqual(self.urugero.konti,"Instagram")
        self.assertEqual(self.urugero.username,"Alibebe")
        self.assertEqual(self.urugero.password,"112")


    def tearDown(self):
            Credential.credo_data = []

    def test_save_konti(self):
        """
        test case to test if the credential object is saved into the credential list
        """
        self.urugero.bika_konti() #saving new account
        self.assertEqual(len(Credential.credo_data),1)


    def test_konti_zose(self):
        '''
        test to check if we can view our accounts that has been created
        '''
        self.assertEqual(Credential.konti_zose(), Credential.credo_data)


    def test_siba_konti(self):
        """
        Test if we can remove a user from our credential list
        """
        self.urugero.bika_konti()
        urugero_2 = Credential("Twitter","Mwiza","1234")
        urugero_2.bika_konti()
        self.urugero.delete_konti()
        self.assertEqual(len(Credential.credo_data),1)


    def test_search_konti(self):
        """
        this method is for searching any account
        """
        self.urugero.bika_konti()
        urugero_2 = Credential("Twitter","Mwiza","1234")
        urugero_2.bika_konti()
        shaka_konti = Credential.search_konti("Mwiza")
        self.assertEqual(shaka_konti.username,urugero_2.username)


    def test_terura_konti(self):
        """
        this metod justfy that the copy has made
        """
        self.urugero.bika_konti()
        Credential.terura_konti("Alibebe")
        self.assertEqual(self.urugero.username,pyperclip.paste())


    def test_genzura_neza_konti(self):
        """
        this method is going to test if account exists 
        """
        self.urugero.bika_konti()
        urugero_2 = Credential("Twitter","Mwiza","1234")
        urugero_2.bika_konti()
        exists = Credential.genzura_neza_konti("Alibebe")
        self.assertTrue(exists)    


if __name__ == '__main__':
    unittest.main()
