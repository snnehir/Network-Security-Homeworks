
## Assignment 3

Aim of this assignment is to understand password cracking cases.


### Project setup
*  You should have Python version 3+ installed:  
    
    https://www.python.org/downloads/release/python-3911/


*  Required packages: None

### To run ```main.py``` in terminal:
```
python main.py
```


### More explanation about assignment:
-  We are assuming passwords in our system consist of 6-digit numbers only. (000000 to 999999)
-  Our system consist of 32 users
-  The attacker (a.k.a. Trudy) has password dictionary that contains 1024 passwords.

-  Four cases for password cracking:  

    1. Trudy wants to determine Alice's password (perhaps Alice is the administrator). Trudy does not use her dictionary of likely passwords. 

    2. Trudy wants to determine Alice's password. Trudy does use her dictionary of common passwords. 

    3. Trudy will be satisfied to crack any password in the password file, without using her dictionary. 

    Case 4- Trudy wants to find any password in the hashed password file, using 
    her dictionary.

 I wrote 4 functions to crack the password in each case and calculated the time needed to crack the password.

 I used MD5 algorithm since it's faster to calculate but MD5 should not be used in real life because it's not secure anymore.

