# es-tm.py : Expert System Tool Managaer 
# To create, read, update, and delete files from a knoweledge base consisting of: (refer to doc)
import sys
import time
import fire

#CURSOR_UP_ONE = '\033[F'
#ERASE_LINE = '\033[K'

#display
class Tool(object):
	"""T==0===0===L------------------------------------------------88--------------------------------------M==A==N==A==G==E==R"""
	#print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	#print("c|reate  r|read  u|pdate  d|elete  e|xecute\n")
	# while True:
	# 	command = input("")
	# 	if command == 'c':
	# 		print ("Still working on it!", end='\r')
	# 	elif command == 'r':
	# 		print("Still working on it!")
	# 	elif command == 'u':
	# 		print("Still working on it!")
	# 	elif command == 'd':
	# 		print("Still working on it!")
	# 	elif command == 'e':
	# 		command = input("Enter \'q\' to exit:")
	# 	if command == 'q':
	# 		return

# def main():
# 	view()

# #run 
# main()

if __name__ == '__main__':
	fire.Fire(Tool)
