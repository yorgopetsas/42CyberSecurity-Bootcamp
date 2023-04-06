import argparse
import os
from cryptography.fernet import Fernet

# def yz_encript_file(file):


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
		# cifrar fichero
		# yz_encript_file(file)
		return(file)


def yz_key_reg(key):
	file = yz_file_checker()
	if file:
		print(file)

	file_to_write = open(file, 'w')
	file_to_write.write(key)
	file_to_write.close()


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
		
		# yz_to_hex(key)

		if yz_chk_hex(key) != 0:
			yz_key_reg(key)
		
		# print(key)

	gen = args.k
	if gen:
		print(gen)


# Convert str to hexdecimal. Not Working
# def yz_to_hex(key):
# 	key_int = int(key)
# 	key_hex = hex(key_int)
# 	print(key_hex)

# if not re.match(r'^[0-9a-fA-F]{64,}$', clave):
#     print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
# Expresión regular:
# ^           : límite inicial de la acotación de la cadena.
# [0-9a-fA-F] : cualquier caracter hexadecimal (números, o letras desde 'a' hasta 'f' o desde 'A' hasta 'F').
# {64,}       : cuantificador que indica longitud de 64 hasta ilimitados caracteres.
# $           : límite final de la acotación de la cadena.
	