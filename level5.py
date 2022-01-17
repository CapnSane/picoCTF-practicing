import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

# with open('dictionary.txt') as f:
#     pos_pw_list = f.readlines()
    
a_file = open("dictionary.txt", "r")

pos_pw_list = []

for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  pos_pw_list.append(line_list)

a_file.close()
flatlist=[]
for sublist in pos_pw_list:
    for element in sublist:
        flatlist.append(element)
pos_pw_list = flatlist
print(pos_pw_list)

def level_5_pw_check():
    for i in pos_pw_list:
        user_pw = i
        user_pw_hash = hash_pw(user_pw)
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        # print("That password is incorrect")



level_5_pw_check()

