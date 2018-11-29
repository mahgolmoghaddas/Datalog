#!usr/bin/env python2
#The above line is a shebang line.
#------------------------------------------------------------------------------------#
#model.py

#The following is the model for the data structures to be used
#in the parser and the inference engine.
#------------------------------------------------------------------------------------#

class Rule(object):
    def __init__(self, head={}, body={}, certainty = float(), type="rule"):
        self.head = head
        self.body = body
        self.type = type
        self.certainty = certainty
    def __repr__(self):
        return "%r" % (self.__dict__)
    def __gettype__(self):
        return self.type

class Query(object):
    def __init__(self, query, type = "query"):
        self.query = query
        self.type = type
    def __repr__(self):
        return "%r" % (self.__dict__)

class Fact(object):
    def __init__(self, fact, certainty = float(), type = "fact"):
        self.fact = fact
        self.type = type
        self.record = set()
        self.certainty = certainty

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "%r" % (self.__dict__)

class Predicate(object):
    def __init__(self, name="", terms=[], type = "predicate"):
        self.name = name
        self.terms = terms
        self.type = type

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "%r" % (self.__dict__)