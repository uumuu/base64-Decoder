"""
Case-check base64 decoder.
uumuu
"""

import base64
import itertools
import os
import time

def get_input():
	"""
	Gets code input from user, checks if it is the correct length (mult. of 3)
	if not, adds '='' padding until it is
	"""
	input_str = input('What do you want to decode?\n')
		if (len(input_str) % 3) != 0:
			print("Input not in correct format, adding padding.\n")
			time.sleep(2)
			while (len(input_str) %3) != 0:
				input_str += '='
		print('New input is: %s' %input_str)
		return input_str

def decode(s):
	"""
	base64 decodes the input code.
	Checks for any errors and if they are they will not make it to the append
	block in main()
	"""
	try:
		b = base64.b64decode(s).decode('utf-8')
		return b
	except (base64.binascii.Error, UnicodeDecodeError, UnicodeEncodeError):
		return 'no'

def main():
	"""
	Applies lower, upper functions in every possible way, using product and zip funcs
	then each unique and eligible string is appended to the string_list and printed 
	to screen.
	"""
	input_str = get_input()
	s = (''.join(t) for t in itertools.product(*zip(input_str.lower(), input_str.upper())))
	string_list = []
	for n in s:
		decoded = decode(n)
		if decoded not in string_list and decoded != 'no':
			print(decoded)
			string_list.append(decoded)

main()