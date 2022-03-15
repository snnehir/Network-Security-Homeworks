import numpy as np
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import cv2 # opencv for using read/write image operations

BLOCK_SIZE = 16 
IMG_SIZE = 300
IMG_SIZE_ROUND = IMG_SIZE + (BLOCK_SIZE - (IMG_SIZE% BLOCK_SIZE))


def encrypt_img(plain_img, key):
    L2 = []
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_img= np.array(range(IMG_SIZE_ROUND * IMG_SIZE_ROUND), int).reshape((IMG_SIZE_ROUND, IMG_SIZE_ROUND))
    for i in range(IMG_SIZE):
        img_bytes= bytes(plain_img[i,:].tolist())
        # encrypt
        msg =  cipher.encrypt(pad(img_bytes, BLOCK_SIZE))
        for p in msg:
            L2 += [(p)]
        encrypted_img[i,:]=L2[:]
        L2=[]
    cv2.imwrite('ecb_mode/encrypted.png', encrypted_img)
    
    return encrypted_img


def decrypt_img(encrypted_img, key):
    L2=[]
    decrypted_img= np.array(range(IMG_SIZE*IMG_SIZE), int).reshape((IMG_SIZE,IMG_SIZE))
    plain = AES.new(key, AES.MODE_ECB)
    for i in range(IMG_SIZE):
        img_bytes=bytes(encrypted_img[i,:].tolist())
        # decrypt
        msg = unpad(plain.decrypt(img_bytes), BLOCK_SIZE)
        for p in msg:
            L2 += [(p)]
        decrypted_img[i,:]=L2[:]
        L2=[]
    cv2.imwrite('ecb_mode/decrypted.png', decrypted_img)
    

plain_img = cv2.imread('turtle.png', 0)   # read grayscale image 2D array (300X300)

key = b'very secret key!' # 16-byte key

dec_img = encrypt_img(plain_img, key)
decrypt_img(dec_img, key)
