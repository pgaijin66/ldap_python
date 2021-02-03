# A simple Python program to demonstrate  
# getpass.getpass() to read password 
import getpass 
  
try: 
    p = getpass.getpass() 
except Exception as error: 
    print('ERROR', error) 
else: 
    print('Password entered:', p) 