from database import store_password,find_user,find_password,delete
import array
import random
import pyperclip
from cryptography.fernet import Fernet  

passw=input('Please provide the master password to start the password manager: ')

if passw=='Password':
    print('Welcome to the password manager')
else:
    print('Incorrect password')
    exit()    


print('-'*40)
print(('-'*18)+'Menu'+('-'*18))
print('1. Create your new password')
print('2. Find a passwoed for a site or app')
print('3. Find all sites and apps connected to an email')
print('4. Delete the information you added')
print('-'*40)

choice=input(': ')
while choice != 'Q':
    if choice =='1':
        print('Please provide the name of the site or app you want to generate a password for: ')
        app_name=input()
        MAX_LEN=(int(input('Enter the length of password: ')))
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        rand_digit=random.choice(DIGITS)
        rand_upper=random.choice(UPCASE_CHARACTERS)
        rand_lower=random.choice(LOCASE_CHARACTERS)
        rand_symbol=random.choice(SYMBOLS)
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        for x in range(MAX_LEN - 4):
	        temp_pass = temp_pass + random.choice(COMBINED_LIST)   
	        temp_pass_list = array.array('u', temp_pass)
	        random.shuffle(temp_pass_list)
        password = ""
        for x in temp_pass_list:
       	    password = password + x
        ans=input("Type -yes- to display passowrd: ")
        if ans =="yes":
            print(password) 
        pyperclip.copy(password)
        spam=pyperclip.paste()
        print('-'*30)
        print('Your password has now been created and copied to your clipboard')
        print('-'*30)  
        user_email=input('Please provide a user email for this app or site: ')
        username=input('Please provide a username for this app: ')
        if username ==None:
            username =''
        url =input('Please provide the url of the site: ')
        store_password (password,user_email,username,url,app_name)
        break
    if choice =='2':
        print('Please provide the name of the site or app you want to find the password: ')
        app_name = input()
        find_password(app_name)
        break     

    if choice =='3':
        print('Please provide the email that you want to find accounts for: ')
        user_email=input()
        find_user(user_email)
        break
    if choice =='4':
        print('Provide the app name you want to delete: ')
        app_name=input()
        delete(app_name)
        break
    else:
        choice=menu()
exit()  

         

