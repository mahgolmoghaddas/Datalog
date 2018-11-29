import copy
import sys
import os


from model import Fact, Predicate, Rule
import yacc
from lex import tokens, data

parser = yacc.parser
program = parser.parse(data)
fact=[]
p=[]
k=[]
k1=[]
p1=[]
EDB=[]
predicate=[]
rule=[]
fact_dict={}
store=[]
new_name=[]
new_certainty=[]
fact_dict=dict()
for i in program:
    if i.type=='fact':
        fact.append(i)
    if i.type=='predicate':
        predicate.append(i)
    if i.type=='rule':
        rule.append(i)

print(rule[1].body[1].name)
#print(fact[1].fact)
dict_name={}
dict_name=Predicate()

def rename(name, name1):
    name1 = name
    return name1


def certainty(certainty, certainty1):
    return certainty*certainty1


def conj(certainty, certainty1):
    return min(certainty1,certainty)


def updateEDB():

    p.append(copy.deepcopy(Fact(dict_name,new_certainty,type='fact')))
    return p








for i in range (0, len(fact)):
        if len(fact[i].fact.terms)==len(rule[0].body[0].terms) :
            if fact[i].fact.name==rule[0].body[0].name:
                        new_name=rename(rule[0].head.name,rule[0].body[0].name)
                        new_certainty=(certainty(fact[i].certainty,rule[0].certainty))
                        dict_name.terms=fact[i].fact.terms
                        new_name=rename(rule[0].head.name,rule[0].body[0].name)
                        new_certainty=(certainty(fact[i].certainty,rule[0].certainty))
                        dict_name.terms=fact[i].fact.terms
                        dict_name.name=new_name
                        dict_name.type='predicate'
                        updateEDB()


fact=p+fact


for i in range (0, len(rule[1].body)):
    for j in range (0, len(rule[1].head.terms)):

        if rule[1].head.terms[0]==rule[1].body[i].terms[j] or rule[1].head.terms[1]==rule[1].body[i].terms[j]:
            for k in range (0,len(fact)):

                if fact[k].fact.name==rule[1].body[i].name:
                    store.append(copy.deepcopy(fact[k].fact))
