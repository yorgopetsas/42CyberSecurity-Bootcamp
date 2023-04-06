from cryptography.fernet import Fernet

with open('key.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('ft_otp.key', 'rb') as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('ft_otp.key', 'wb') as dec_file:
    dec_file.write(decrypted)