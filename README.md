# CENG474-Hw
This repository includes assignments given in CENG474 Communication and Network Security course.

## Project setup

### Create virtual environment
```
python -m venv venv 
```

### Install required packages
```
pip3 install -r requirements.txt
```


## About Assignment
Aim of this assignment is to understand the difference between ECB and CBC mode.
Goal: Write a block cipher that encrypts a grayscale image.

I selected this grayscale picture for reference.

![demo_image](https://github.com/snnehir/CENG474-Hw/blob/master/turtle.png)


### 1- To run ecb.py in terminal
```
python ecb_mode/ecb.py
```

### Encrypted image obtained with ECB mode
![encrypted_image_ecb](https://github.com/snnehir/CENG474-Hw/blob/master/ecb_mode/encrypted.png)

Encryption using ECB mode is not secure since we can see the outline of the original image.


### 2- To run cbc.py in terminal
```
python cbc_mode/cbc.py
```

### Encrypted image obtained with CBC mode
![encrypted_image_cbc](https://github.com/snnehir/CENG474-Hw/blob/master/cbc_mode/encrypted.png)

Encryption using CBC is more secure since we cannot have any idea about the plain image.
