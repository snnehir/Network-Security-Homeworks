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


## Assignment Detail
Aim of this assignment is to understand the difference between ECB and CBC mode.
I selected this grayscale picture for reference.

![demo_image](https://github.com/snnehir/CENG474-Hw/blob/master/turtle.png)


### To run the code in terminal
```
python ecb_mode/ecb.py
```

### Encrypted image obtained with ECB mode
![encrypted_image](https://github.com/snnehir/CENG474-Hw/blob/master/ecb_mode/encrypted.png)

Encryption using ECB mode is not secure since we can see the outline of the original image.
