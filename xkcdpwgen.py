import sys
import argparse
import os
import random

#defining variables 

wordlist_loc = "wordlist_corncob.txt"
list_of_words=''
all_words=''
GeneratedPass = []
numberstobeincluded = range(0,9)
symbolslist = ["@","!","#", "$","&", "%", "*","^", ";","~,","+","|"] 
randomisecapsloc = []

#RAND_WORDS = open(wordlist_loc).read().splitlines()

with open(wordlist_loc,"r") as file:
	all_words = file.read()
	list_of_words = list(map(str,all_words.split('\n')))
	


#creating parser
my_parser = argparse.ArgumentParser(prog='xkcdpwgen',formatter_class=argparse.RawDescriptionHelpFormatter,description='''\
		Generate a secure, memorable password using the XKCD method
				--------------------------------
				''')
my_parser.set_defaults(no_args='no argument passed')

my_parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0',)

my_parser.add_argument('-w','--words',type=int,default=4,metavar='WORDS',help='include WORDS words in the password (default=4)')

my_parser.add_argument('-c','--caps',type=int,default=0,metavar='CAPS',help='capitalize the first letter of CAPS random words (default=0)')

my_parser.add_argument('-n','--numbers',type=int,default=0,metavar='NUMBERS',help='insert NUMBERS random numbers in the password (default=0)')

my_parser.add_argument('-s','--symbols',type=int,default=0,metavar='SYMBOLS',help='insert SYMBOLS random symbols in the password (default=0)')

args = my_parser.parse_args()



words=4
caps=0
numbers=0
symbols=0
y=0

for arg in range(len(sys.argv)):
	y=0
	if arg+1 < len(sys.argv):		# fix the conversion of sys.argv[arg+1]  to int
		try:
			y= int(sys.argv[arg+1])  
		except Exception as e:
			y=0

		

	if sys.argv[arg] == '-w' or sys.argv[arg] == '--words':
		words=y
	elif sys.argv[arg] == '-c' or sys.argv[arg] == '--caps':
		caps=y
	elif sys.argv[arg] == '-n' or sys.argv[arg] == '--numbers':
		numbers=y
	elif sys.argv[arg] == '-s' or sys.argv[arg] == '--symbols':
		symbols=y


#print(str(sys.argv))


#defining action for words 

for numofwords in range(words):
	GeneratedPass.append(random.choice(list_of_words))


#defining action for caps 
try:
	randomisecapsloc = random.sample(range(0,len(GeneratedPass)),caps)
except Exception as e:
	print("Error : capitalizing words cannont be larger than number of words\n")

for numofcaps in randomisecapsloc:
	GeneratedPass[numofcaps] = GeneratedPass[numofcaps].capitalize()



#defining action for inserting numbers in password

for numofnums in range(numbers):
	GeneratedPass.insert(random.randint(0,len(GeneratedPass)),str(random.choice(numberstobeincluded)))



#defining action for symbol flag	
for numofsymbols in range(symbols):
	#print(symbols)
	GeneratedPass.insert(random.randint(0,len(GeneratedPass)),str(random.choice(symbolslist)))





print("".join(GeneratedPass))

