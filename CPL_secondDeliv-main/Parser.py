"""
program : Top-down recursive descent parser
description : This parser is implemented for a small subset of the SCL language
Authors : Jonathan Hardy, Zach Keener, Andy Kenmoe, Vincent Kipchoge

"""
# Import from Scanner class
from Scanner import Lexier
from Scanner import Token

# Parser class
class Parser:
	lexier = Lexier()
	token = Token()
	nextToken = None

	#def __init__(self, lexemeList):

	#Compile function
	def begin(self, inputString):
		self.lexier.analyzer(inputString)
		self.getNextToken()
		self.expr()

	# Expr function
	def expr(self):
		print("Enter <expr>")
		self.term()
		# Checks for addition operator and subtraction operator
		while(self.nextToken.TYPE == self.lexier.ADD_OP or self.nextToken.TYPE == self.lexier.SUB_OP):
			self.getNextToken()
			self.term()
		print("Exit <expr>")


	# Term function
	def term(self):
		print("Enter <term>")
		self.factor()
		# Checks for multiplier operator, division operator, and assignment (equal) operator
		while(self.nextToken.TYPE == self.lexier.MULT_OP or self.nextToken.TYPE == self.lexier.DIV_OP or self.nextToken.TYPE == self.lexier.ASSIGN_OP):
			self.getNextToken()
			self.factor()
		print("Exit <term>")


	# Factor function
	def factor(self):
		print("Enter <factor>")
		# Check for indents or integer literals
		if(self.nextToken.TYPE == self.lexier.IDENT or self.nextToken.TYPE == self.lexier.INT_LIT):
			self.getNextToken()
		else:
			# Check for left parenthesis
			if(self.nextToken.TYPE == self.lexier.LEFT_PAREN):
				self.getNextToken()
				self.expr()
				# Check for right parenthesis (after finding the left parenthesis)
				if(self.nextToken.TYPE == self.lexier.RIGHT_PAREN):
					self.getNextToken()
				else:
					self.error()
		print("Exit <factor>")


	# Get next token
	def getNextToken(self):
		self.nextToken = self.lexier.getNext()


	# Function to print error
	def error(self):
		print("Syntax error")



# "Main" Function that runs code:
parser = Parser()
fileName = input("Please enter file name: ")
# Reads line-by-line from the file
with open(fileName) as file:
	for line in file:
		line = line.strip()
		parser.begin(line)
		print("")
# Close file
file.close()