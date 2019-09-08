#!/usr/bin/env python3.6
from Locker import Urufunguzo
from Credentials import Credential
import pyperclip
#Functions for Creating User
def hanga_user(name,fone,names,mail,ibanga):
    '''
    Function to create a new user
    '''
    user = Urufunguzo(name,fone,names,mail,ibanga)
    return user

def save_users(Locker):
    '''
    Function to save user
    '''
    Locker.bika_user()

def delete_user(Locker):
    '''
    Function to delete user
    '''
    Locker.siba_user()

def search_user(string):
    '''
    Function that searchs user
    '''
    return Urufunguzo.ni_Izina(string)     

def check_existing_user(string):
    '''
    Function that check if user exists
    '''
    return Urufunguzo.reba_user(string)

def display_user():
    '''
    Function that returns all the saved user
    '''
    return Urufunguzo.user_bose()


def copy_user(Locker):
    '''
    Function to copy user
    '''
    Locker.terura_user()    




#Functions for Creating Accounts
def rema_konti(konti,username,password):
    '''
    Function to create a new credential
    '''
    account = Credential(konti,username,password)
    return account

def save_credential(Credentials):
    '''
    Function to save credential
    '''
    Credentials.bika_konti()

def delete_user(Credentials):
    '''
    Function to delete credential
    '''
    Credentials.delete_konti()

def search_credential(string):
    '''
    Function that searchs credential
    '''
    return Credential.search_konti(string)     

def check_existing_credentials(string):
    '''
    Function that check if credential exists
    '''
    return Credential.genzura_neza_konti(string)

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.konti_zose() 

def copy_credential(string):
    '''
    Function to copy credential
    '''
    Credentials.terura_konti()                



#Main function for Creating user
def main():
    print("*"*29)
    print("WELCOME TO OUR APPLICATION.")
    print("*"*29)
    print(" What is your name?")
    user_name = input()
    print(f"So {user_name}. Enjoy Your Choice Using This Short Codes")
    print('\n')
    while True:
            print("#"*19)
            print("1 - Create Account")
            print("2 - Display User")
            print("3 - Search User")
            print("4 - Copy User")
            print("5 - Delete a User")
            print("6 - Exit")
            print("#"*19)
            Code = input()
            if Code == '1':
                    print("New User")
                    print("="*10)
                    print ("Full Name:")
                    name = input()
                    print("Phone Number:")
                    fone = input()
                    print("UserName:")
                    names = input()
                    print("Email Address:")
                    mail = input()
                    print("Password:")
                    ibanga = input()
                    save_users(hanga_user(name,fone,names,mail,ibanga))
                    print ('\n')
                    print(f"New User {name} Created")
                    print ('\n')
            elif Code == '2':
                    if display_user():
                            print("="*10)
                            print("List of Users")
                            print("="*10)
                            print('\n')
                            for user in display_user():
                                    print(f"{user.name}  {user.fone} {user.names} {user.mail}")
                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any users saved yet")
                            print('\n')
            elif Code == '3':
                    print("Enter The Name You Want To Search For:")
                    search = input()
                    if check_existing_user(search):
                            user_search= search_user(search)
                            print('.' * 20)
                            print(f"Full Name:{user_search.name}") 
                            print(f"UserName:{user_search.names}")
                            print(f"Phone Number:{user_search.fone}")
                            print(f"Email Address:{user_search.mail}")
                            print('.' * 20)
                            print ('\n')
                    else:
                            print("The User Doesn't Exist")
            elif Code == '5':
                    print('Enter The Name:')
                    search = input()
                    if check_existing_user(search):
                            user_search= search_user(search)
                            print('.' * 20)
                            print(f"Full Name:{user_search.name}") 
                            print(f"UserName:{user_search.names}")
                            print(f"Phone Number:{user_search.fone}")
                            print(f"Email Address:{user_search.mail}")
                            print('.' * 20)
                            print ('\n')
                            user_search.siba_user()
                            print('User Deleted')
                    else:
                            print("The User Doesn't Exist")
            elif Code == '4':
                    print('Enter The Name:')
                    search = input()
                    if check_existing_user(search):
                            user_search= search_user(search)
                            print('.' * 20)
                            print(f"Full Name:{user_search.name}") 
                            print(f"UserName:{user_search.names}")
                            print(f"Phone Number:{user_search.fone}")
                            print(f"Email Address:{user_search.mail}")
                            print('.' * 20)
                            print ('\n')
                            user_search.terura_user(search)
                            print('User Copied.')
                    else:
                            print("The User Doesn't Copied")
                            print ('\n')
            elif Code == "6":
                    print("Thank you")
                    break
            else:
                    print("PLZ!! You Number To Choose!")





if __name__ == '__main__':

    main()                            





