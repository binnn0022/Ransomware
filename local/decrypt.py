import os
from cryptography.fernet import Fernet

def decrypt(directory,decryptkey):
    
    #switch to desire dir
    os.chdir(directory)
    
    #grabs file names into a list
    files = []
    for file in os.listdir():
        if file == 'ransomware.py' or file == 'thekey.key' or file == 'decrypt.py' or file == 'generate_key.py':
            continue
        if os.path.isfile(file):
            files.append(file)
    
    #decrypt the files
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        decrypted_content = Fernet(decryptkey).decrypt(contents)

        with open(file, 'wb') as thefile:
            thefile.write(decrypted_content)
            


path = '/home/bin2k2/code/ransomware/local'
#path = r'C:\Users\admin\important data'
decryptkey =b"cAC6jfAbQmFUKZguwlggHDwUH4i5Pcc_TToY_yc7aj0="
decrypt(path, decryptkey)


