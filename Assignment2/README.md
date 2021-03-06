# Assignment 2

Aim of this assignment is to understand the difference between ECB and CBC mode.

I selected this grayscale picture for reference.

![demo_image](https://github.com/snnehir/CENG474-Hw/blob/master/Assignment2/turtle.png)


## Project setup

### You should have Python version 3+ installed

https://www.python.org/downloads/release/python-3911/


### In command prompt go to project directory
```
cd Assignment2
```

### Install required packages
```
pip3 install -r requirements.txt
```

### 1- To run ecb.py in terminal
```
python ecb_mode/ecb.py
```

### Encrypted image obtained with ECB mode
![encrypted_image_ecb](https://github.com/snnehir/CENG474-Hw/blob/master/Assignment2/results/encrypted_ecb.png)

Encryption using ECB mode is not secure since we can see the outline of the original image.


### 2- To run cbc.py
```
python cbc_mode/cbc.py
```

### Encrypted image obtained with CBC mode
![encrypted_image_cbc](https://github.com/snnehir/CENG474-Hw/blob/master/Assignment2/results/encrypted_cbc.png)

Encryption using CBC is more secure since we cannot guess the plain image from encrypted image.

*Encrypted and decrypted images can be found under each folder.

#

&nbsp;

## Project setup for working with virtual environment in VSCode (optional)

### Create Python virtual environment
```
cd Assignment2
python -m venv my_venv 
```

### Activate virtual environment
```
 & my_venv/Scripts/Activate.ps1  
```

### Install required packages
```
pip3 install -r requirements.txt
```
