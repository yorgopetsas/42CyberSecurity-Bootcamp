import argparse
import os
import hmac
import time
import hashlib
import struct
from cryptography.fernet import Fernet

def yz_encript_file(filez):
	key = Fernet.generate_key()

	with open('.key', 'wb') as filekey:
	    filekey.write(key)
	with open('.key', 'rb') as filekey:
	    key = filekey.read()
	fernet = Fernet(key)
	with open(filez, 'rb') as file:
	    original = file.read()
	encrypted = fernet.encrypt(original)
	with open(filez, 'wb') as encrypted_file:
	    encrypted_file.write(encrypted)


def yz_code_gen():
	with open('.key', 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)

	eta_time = int(time.time() // 30)
	eta_time_b = struct.pack(">Q", eta_time)

	hash_b = hmac.digest(key, eta_time_b, hashlib.sha1)

	offset = hash_b[19] & 15

	code = struct.unpack('>I',  hash_b[offset:offset + 4])[0]
	code = (code & 0x7FFFFFFF) % 1000000

	return "{:06d}".format(code)


def yz_file_checker():
	file = 'ft_otp.key'
	check_file = os.path.exists(file)
	if check_file:
		# Clean data in file
		file_to_clean = open(file,'w')
		file_to_clean.close()
		return(file)

	else:
		# Create file
		file_to_create = open(file, 'x')
		file_to_create.close()
		# Return error if file was not created for some reason
		check_file = os.path.exists(file)
		if not check_file:
			return(0)
		return(file)


def yz_key_reg(key):
	file = yz_file_checker()
	if file:
		print(file)

	file_to_write = open(file, 'w')
	file_to_write.write(key)
	file_to_write.close()
	yz_encript_file(file)


# Check if provided key is hexidecimal
def yz_chk_hex(key):
	hex = "0123456789abcdefABCDEF"
	for i in key:
		if i not in hex:
			return(0)
	return(key)


def cli_scan():
	scan = argparse.ArgumentParser()

	scan.add_argument("-g", help="", type=str)
	scan.add_argument("-k", help="", type=str)

	return scan.parse_args()


if __name__ == "__main__":
	global key

	args = cli_scan()
	if args.g and len(args.g) > 63:
		key = args.g
		if yz_chk_hex(key) != 0:
			yz_key_reg(key)

	gen = args.k
	if gen:
		#ft_otp -k ft_otp.key
		print(yz_code_gen())

	