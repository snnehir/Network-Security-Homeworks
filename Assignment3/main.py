# generate password file that is contain 6-digit numbers only (from 000000 to 999999)
import hashlib
import random
import time

passwords = []
number_of_users = 32
attackers_dictionary = []
dictionary_size = 1024
salt_key = "saltkey123"  # should be randomly generated


def get_salted_hashed_password(plain_password, salt_key):
    pw = str(plain_password).zfill(6)   # 123 -> 000123 (6 digits)
    salted_pw = bytes(pw + salt_key, "utf-8")
    hashed_pw = hashlib.md5(salted_pw).hexdigest()
    return hashed_pw


# construct attacker's dictionary (1024)
# suppose Alice's password is in the attacker's dictionary
def create_dictionary(dictionary_size, alices_password=None):
    attackers_dictionary = []

    if alices_password is not None:
        dictionary_size -= 1
        attackers_dictionary.append(alices_password)

    for i in range(dictionary_size):
        pw = str(random.randint(0, 999999)).zfill(6)
        attackers_dictionary.append(pw)

    random.shuffle(attackers_dictionary)
    return attackers_dictionary


def create_users_password(number_of_users, salt_key):
    passwords = []
    # choose random passwords
    for i in range(number_of_users):
        hashed_pw = get_salted_hashed_password(
            random.randint(0, 999999), salt_key)
        passwords.append(hashed_pw)
    return passwords


# brute forcing without using dictionary
def case1_cracking(alices_password, salt_key):
    start_time = time.time()
    for i in range(1000000):
        hashed_pw = get_salted_hashed_password(i, salt_key)
        if hashed_pw == alices_password:
            time_to_crack = time.time() - start_time
            return f"[Case 1] Alice's password {i} is cracked in {time_to_crack} seconds."


# attacker uses her dictionary
def case2_cracking(alices_password, salt_key, dictionary_size, alices_plain_password):
    start_time = time.time()
    attackers_dictionary = create_dictionary(
        dictionary_size, alices_plain_password)

    for i in range(dictionary_size):
        hashed_pw = get_salted_hashed_password(
            attackers_dictionary[i], salt_key)
        if hashed_pw == alices_password:
            time_to_crack = time.time() - start_time
            return f"[Case 2] Alice's password {attackers_dictionary[i]} is cracked in {time_to_crack} seconds."


def case3_cracking():
    pass


def case4_cracking():
    pass


######################################### Main section #########################################

alices_plain_password = "923576"
alices_pw = get_salted_hashed_password(alices_plain_password, salt_key)

print("Alice's pw: ", alices_pw)
print()
print(case1_cracking(alices_pw, salt_key))

print("\n-------------------------\n")
print(case2_cracking(alices_pw, salt_key, 1024, alices_plain_password))
