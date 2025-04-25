from cryptography.fernet import Fernet
import os

# Generate a key
key = Fernet.generate_key()

# Specify the directory and file name
directory = '/home/bin2k2/code/ransomware/local'  # Change this to your desired path
file_path = os.path.join(directory, 'thekey.key')

# Write the key to the specified file
with open(file_path, 'wb') as thekey:
    thekey.write(key)