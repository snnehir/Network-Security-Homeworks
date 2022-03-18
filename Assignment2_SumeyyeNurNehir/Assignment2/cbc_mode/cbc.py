import numpy as np
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import cv2


BLOCK_SIZE = 16


def encrypt_img(plain_img, key, iv, IMG_SIZE=300):
    col = []
    # Block ciphers in ECB or CBC mode require their input to be an exact multiple of the block length.
    # Any odd bytes need to be padded to the next multiple.
    IMG_SIZE_ROUND = IMG_SIZE + (BLOCK_SIZE - (IMG_SIZE % BLOCK_SIZE))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_img = np.array(range(
        IMG_SIZE_ROUND*IMG_SIZE_ROUND), int).reshape((IMG_SIZE_ROUND, IMG_SIZE_ROUND))

    for i in range(IMG_SIZE):
        img_bytes = bytes(plain_img[i, :].tolist())
        # encrypt
        msg = cipher.encrypt(pad(img_bytes, BLOCK_SIZE))
        for p in msg:
            col += [(p)]
        encrypted_img[i, :] = col[:]
        col = []  # clear list
    cv2.imwrite('cbc_mode/encrypted.png', encrypted_img)
    print("Encryption is completed! Check: cbc_mode/encrypted.png")
    return encrypted_img


def decrypt_img(encrypted_img, key, iv, IMG_SIZE=300):
    col = []
    decrypted_img = np.array(range(IMG_SIZE*IMG_SIZE),
                             int).reshape((IMG_SIZE, IMG_SIZE))
    plain = AES.new(key, AES.MODE_CBC, iv)

    for i in range(IMG_SIZE):
        img_bytes = bytes(encrypted_img[i, :].tolist())
        # decrypt
        msg = unpad(plain.decrypt(img_bytes), 16)
        for p in msg:
            col += [(p)]
        decrypted_img[i, :] = col[:]
        col = []  # clear list
    cv2.imwrite('cbc_mode/decrypted.png', decrypted_img)
    print("Decryption is completed! Check: cbc_mode/decrypted.png")


plain_img = cv2.imread('turtle.png', 0)   # read image (300x300)

key = b'my very secret k'  # 16-byte key
# initialization vector should be randomly selected
iv = Random.new().read(BLOCK_SIZE)

dec_img = encrypt_img(plain_img, key, iv)

decrypt_img(dec_img, key, iv)
