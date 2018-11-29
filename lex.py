#!usr/bin/env python2
#The above line is a shebang line.
#----------------------------------------------------------------------------------------
#lex.py
#
#The following is the source code for a very simple lexical analyser for ProbLog syntax.
#----------------------------------------------------------------------------------------

import ply.lex as lex
#ply is an implementation of the traditional lex and yacc tools, for Python, in Python.

tokens = ['CONSTANT',
		  'VARIABLE',
		  'NUMBER',
		  'PERIOD',
		  'COMMA',
		  'LEFT_PARENTHESIS',
		  'RIGHT_PARENTHESIS',
		  'IMPLICATION',
		  'QUERY',
		  'COLON',
		  'CERTAINTY']
#This is the list of tokens to be recognised.
#It is also used by the yacc.py module to identify terminals.

#Regular expressions then specify the above-mentioned tokens.
t_PERIOD = r'\.'
t_COMMA = r'\,'
t_IMPLICATION = r'\:\-'
t_QUERY = r'\?'
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_CONSTANT = r'[a-z][a-zA-Z0-9\_]*'
t_VARIABLE = r'[A-Z][A-Za-z0-9\_]*'
t_COLON = r'\:'


def t_CERTAINTY(t):
	r'[0-9]\.[0-9]+'
	t.value = float(t.value)
	return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t
#If some kind of actions needs to be perfromed, a token rule can be specified as a function.
#For instance, the above rule matches numbers and converts the string into a Python integer.

def t_COMMENT(t):
	r'[ ]*\%.*(\n)?'
	pass
	# No value is returned and token is discarded.
#To discard a token, such as a comment, we can simply define a token rule that returns no value.

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
#This rule is defined so that we can track the line numbers in the source code to be analysed.

t_ignore = ' \t'
#A string containing characters to be ignored, whitespace in this context, is assinged to the t_ignore special decalartion.

def t_error(t):
	print("Illegal caharacter '%s'" % t.value[0])
	t.lexer.skip[1]
#This is the error handling rule.

lexer = lex.lex()
#The lexer is built!

data = '''% generate problem of size 10
reachable(X,Y) :- edge(X,Y) : 0.5.
reachable(X,Y) :- edge(X,Z), reachable(Z,Y) : 0.5.
same_clique(X,Y) :- reachable(X,Y), reachable(Y,X) : 0.5.
edge(0, 1) : 0.5.
edge(1, 2) : 0.5.
edge(2, 3) : 0.5.
edge(3, 4) : 0.5.
edge(4, 5) : 0.5.
edge(5, 0) : 0.5.
edge(5, 6) : 0.5.
edge(6, 7) : 0.5.
edge(7, 8) : 0.5.
edge(8, 9) : 0.5.
edge(9, 10) : 0.5.
edge(10, 7) : 0.5.
'''

lexer.input(data)
#The lexer receives the input designated to be lexically analysed.

#Let the tokenisation begin!
while True:
	token = lexer.token()
	if not token:
		break
		#No more input is left to be tokenised.
	#print  token
