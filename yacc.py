#!usr/bin/env python2
#The above line is a shebang line.
#------------------------------------------------------------------------------------#
#yacc.py								             #
#										     #
#The following is the source code for a very simple parser for ProbLog syntax.       #
#The production rules are written according to the BNF grammar.			     #
#------------------------------------------------------------------------------------#

import ply.yacc as yacc
#ply is an implementation of the traditional lex and yacc tools, for Python, in Python.

from lex import tokens, data
#The token map is required and thus, imported from the lexer.

from model import Rule, Fact, Predicate

error_list = list()

def p_empty(p):
	'''empty :'''
	pass
#The above rule handles empty productions.

def p_program(p):
	'''program : statement_list'''
	p[0] = p[1]
def p_program_empty(p):
	'''program : empty'''
	p[0] = p[1]
#Here to use the empty production, we simply used 'empty' as a symbol.
#A program is a sequence of zero or more statements.

def p_statement_list(p):
	'''statement_list : statement statement_list'''
	p[0] = [p[1]] + p[2]
def p_statement_list_unit(p):
	'''statement_list : statement'''
	p[0] = [p[1]]
#statement_list denotes a list of statements.

def p_statement_assertion(p):
	'''statement : assertion'''
	p[0] = p[1]
def p_statement_query(p):
	'''statement : query'''
	p[0] = p[1]
#A statement is an assertion, a retraction, or a query.
#A retraction is a clause followed by a tilde, and it removes the clause from the database.
#We have not included retractions in our producion rules, since our prototype implements basic Datalog,
#i.e. Datalog with no negation.

def p_assertion(p):
	'''assertion : clause'''
	p[0] = p[1]
#An assertion is a clause followed by a period, and it adds the clause to the database if it is safe. 

def p_query(p):
	''' query : literal QUERY'''
	p[0] = Query(p[1])
#A query is a literal followed by a question mark.

def p_clause_fact(p):
	'''clause : fact'''
	p[0] = p[1]
def p_clause_rule(p):
	'''clause : rule'''
	p[0] = p[1]

def p_fact(p):
	'''fact : literal COLON CERTAINTY PERIOD'''
	p[0] = Fact(p[1], p[3])

def p_rule(p):
	'''rule : literal IMPLICATION body COLON CERTAINTY PERIOD'''
	p[0] = Rule(p[1], p[3], p[5])

def p_body_unit(p):
	'''body : literal'''
	p[0] = [p[1]]
def p_body(p):
	'''body : literal COMMA body'''
	p[0] = [p[1]] + p[3] 

def p_literal_unit(p):
	'''literal : CONSTANT'''
	p[0] = p[1]
def p_literal_empty(p):
	'''literal : CONSTANT LEFT_PARENTHESIS RIGHT_PARENTHESIS'''
	p[0] = Predicate(p[1])
def p_literal(p):
	'''literal : CONSTANT LEFT_PARENTHESIS terms RIGHT_PARENTHESIS'''
	p[0] = Predicate(p[1], p[3])

def p_terms_unit(p):
	'''terms : term'''
	p[0] = [p[1]]
def p_terms(p):
	'''terms : term COMMA terms'''
	p[0] = [p[1]] + p[3] 

def p_term_NUMBER(p):
	'''term : NUMBER'''
	p[0] = p[1]
def p_term_VARIABLE(p):
	'''term : VARIABLE'''
	p[0] = p[1]
def p_term_CONSTANT(p):
	'''term : CONSTANT'''
	p[0] = p[1]

def p_error(p):
	error_list.append("Syntax error in input! " + str(p) + "\n")

out = open('program.txt', 'w')
parser = yacc.yacc(start='program', write_tables=False, debug=False)
parsed_program = parser.parse(data)
#print (parsed_program)