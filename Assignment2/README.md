# Assignment 2

Aim of this assignment is to understand the difference between ECB and CBC mode.

"Write a block cipher that encrypts a grayscale image."


## Project setup

### Create virtual environment
```
python -m venv my_venv 
```

### Install required packages
```
pip3 install -r requirements.txt
```


## About Assignment

I selected this grayscale picture for reference.

![demo_image](https://github.com/snnehir/CENG474-Hw/blob/master/Assignment2/turtle.png)


### 1- To run ecb.py in terminal
```
cd Assignment2
python ecb_mode/ecb.py
```

### Encrypted image obtained with ECB mode
![encrypted_image_ecb](https://github.com/snnehir/CENG474-Hw/blob/master/Assignment2/ecb_mode/encrypted.png)

Encryption using ECB mode is not secure since we can see the outline of the original image.


### 2- To run cbc.py in terminal
```
cd Assignment2
python cbc_mode/cbc.py
```

### Encrypted image obtained with CBC mode
![encrypted_image_cbc](https://github.com/snnehir/CENG474-Hw/blob/master/Assignment2/cbc_mode/encrypted.png)

Encryption using CBC is more secure since we cannot guess the plain image from encrypted image.

For more information: https://www.ubiqsecurity.com/blog/ecb-vs-cbc-block-cipher-mode-differences/
