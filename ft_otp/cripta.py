from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('key.key', 'wb') as filekey:
    filekey.write(key)

# Open Key
with open('key.key', 'rb') as filekey:
    key = filekey.read()

# Use Key
fernet = Fernet(key)

# Open original file to ecript
with open('ft_otp.key', 'rb') as file:
    original = file.read()

# Encript the file
encrypted = fernet.encrypt(original)

# Open file and write encripted data
with open('ft_otp.key', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
