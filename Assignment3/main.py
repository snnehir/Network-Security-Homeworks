# password format: 6-digit numbers only (from 000000 to 999999)
import hashlib
import random
import time


NUMBER_OF_USERS = 32
SALT = "$2b$12$04kvO35Qm7nEPTGFSSI43e"  # constant non-secret value


# helper function to convert plain password into hashed password
def get_hashed_salted_password(plain_password):
    pw = str(plain_password).zfill(6)   # 123 -> 000123 (6 digits)
    salted_pw = bytes(pw + SALT, "utf-8")
    hashed_pw = hashlib.md5(salted_pw).hexdigest()
    return hashed_pw


# construct attacker's dictionary (finding matching passwords in Case4 was so hard when passwords ind dictionary are generated randomly.)
# suppose Alice's password is in the attacker's dictionary
def create_dictionary(dictionary_size, alices_plain_password=None):
    attackers_dictionary = []

    if alices_plain_password is not None:
        dictionary_size -= 1
        attackers_dictionary.append(alices_plain_password)

    for i in range(dictionary_size):
        password = str(i).zfill(6)
        # do not include same passwords
        if password == alices_plain_password:
            password = str(dictionary_size).zfill(6)
        attackers_dictionary.append(password)

    random.shuffle(attackers_dictionary)
    return attackers_dictionary


# create passwords for n users
def create_users_password():
    passwords = []
    # choose random passwords
    for i in range(NUMBER_OF_USERS):
        # small range is used for finding matching passwords in Case4
        # (otherwise it's almost infeasible to find matching passwords because attacker's dictionary size is too small)
        hashed_password = get_hashed_salted_password(random.randint(0, 1500))
        passwords.append(hashed_password)

    return passwords


#   CASE FUNTIONS

# brute forcing. attacker is not using her dictionary
def case1_cracking(alices_password):
    start_time = time.time()
    for i in range(1000000):
        hashed_pw = get_hashed_salted_password(i)
        if hashed_pw == alices_password:
            time_to_crack = time.time() - start_time
            print(
                f"[Case 1] Alice's password {i} is cracked in {time_to_crack} seconds.")


# attacker uses her dictionary
def case2_cracking(alices_password, dictionary_size, alices_plain_password):
    is_found = False
    start_time = time.time()

    # if you want to assume that Alice's password is in the dictionary, use this line and comment line 75:
    # attackers_dictionary = create_dictionary(dictionary_size, alices_plain_password)

    # if you do not want to assume Alice's password is in the dictionary, use this line instead of above line:
    attackers_dictionary = create_dictionary(dictionary_size)

    for pw in attackers_dictionary:
        hashed_pw = get_hashed_salted_password(pw)
        if hashed_pw == alices_password:
            time_to_crack = time.time() - start_time
            print(
                f"[Case 2] Alice's password {pw} is cracked in {time_to_crack} seconds.")
            is_found = True
            break

    # if Alice's password is not in attacker's dictionary, use brute force
    if not is_found:
        print("Alice's password is not found in dictionary. Brute forcing...")
        for i in range(1000000):
            hashed_pw = get_hashed_salted_password(i)
            if hashed_pw == alices_password:
                time_to_crack = time.time() - start_time
                print(
                    f"[Case 2] Alice's password {i} is cracked in {time_to_crack} seconds.")


def case3_cracking():
    passwords = create_users_password()
    start_time = time.time()
    for i in range(1000000):
        hashed_pw = get_hashed_salted_password(i)
        # looking each password for any matching password
        if hashed_pw in passwords:
            time_to_crack = time.time() - start_time
            print(
                f"[Case 3] Password {str(i).zfill(6)} is cracked in {time_to_crack} seconds.")
            break


def case4_cracking(dictionary_size):
    passwords = create_users_password()
    start_time = time.time()
    attackers_dictionary = create_dictionary(dictionary_size)
    is_found = False

    for attacker_pw in attackers_dictionary:
        hashed_pw = get_hashed_salted_password(attacker_pw)
        # looking each password for any matching password
        if hashed_pw in passwords:
            time_to_crack = time.time() - start_time
            print(
                f"[Case 4] Password {attacker_pw} is cracked in {time_to_crack} seconds.")
            is_found = True
            break

    if not is_found:
        print("[Case 4] No matching password found from dictionary")

#  END OF CASE FUNCTIONS


alices_plain_password = "148513"
alices_pw = get_hashed_salted_password(alices_plain_password)
dictionary_size = 1024

print("\nSalt key used: ", SALT)
print("\nAlice's password: ", alices_plain_password)
case1_cracking(alices_pw)
print()
print("Alice's password: ", alices_plain_password)
case2_cracking(alices_pw, dictionary_size, alices_plain_password)
print()
case3_cracking()
print()
case4_cracking(dictionary_size)
print()
