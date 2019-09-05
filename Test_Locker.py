import unittest
from Locker import Urufunguzo

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




if __name__ == '__main__':
    unittest.main()
