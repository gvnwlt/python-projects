# regex.py 
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

gwalt.com

321-555-4321
123.555.1234

Mr. Anderson 
Mr Smith 
Ms Davis
Mrs. Robison
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# raw string : r  <-- will ignore meta or escap chars when used
#print(r'\tTab')


# re compile : allows to separate patterns into a variable
#
# example 1 : search through a raw string for 'abc' ; pattern represents pattern to look for in a string 
#pattern = re.compile(r'abc')

# '.' is a special character in regex: have to use \. to treat it like a regular '.'  
pattern = re.compile(r'end$')

matches = pattern.finditer(sentence) # finditer() will make an iterator to loop through a string looking for 'abc'

for match in matches:
	print(match)

# string slice to reveal what was disovered in the match 
#print(text_to_search[1:4])