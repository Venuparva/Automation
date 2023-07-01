import os

def print_pwd():
	return os.popen('pwd').read()
