import re
from fuzzy_logic import feq


class Node:
    """ The node class
    
        Used to create the individual elements of the graph
    """
    def __init__(self):
        self.states = 0
        self.cur_state = 0
        self.inputs = dict()
        self.inhibitors = dict()
        self.outputs = []
        self.logic = []

    def eval_log(self, num, ins):
        """ Takes the state of all the other nodes and determine the next state """
        replace_logic = self.logic[num]
        for i in ins:
            replace_logic = replace_logic.replace(i, str(ins[i]))
        res = eval(replace_logic)
        if res == [False]:
            res = res[0]
        return res

    def call(self, ins):
        """ Logic for state change """
        if self.states > 0: # not an input layer
            self.cur_state = 0 # by default will reset to 0
            for i in range(len(self.logic)): # checks each logic
                if self.eval_log(i, ins):
                    self.cur_state=i+1 # since i is zero indexed
        else:
            self.cur_state = ins[0] # input layers will be fed their value
        return self.cur_state

    def replace(self, x):
        """ A character mapping from logic to python logic """
        if x == ':':
            return ' |feq| '
        elif x == '!':
            return 'not '
        elif x == '&':
            return ' and '
        elif x == '|':
            return ' or '
        elif x == '[':
            return ' ( '
        elif x == ']':
            return ' ) '
        elif x == '(':
            return ' ( '
        elif x == ')':
            return ' ) '
        else:
            return x

    def add_state(self, logic):
        """ Takes in logic for a new state and adds it to the node
        
            Records any inputs for the first state
        """
        
        # the logic for an input is simple
        if 'input' in logic:
            self.states = 0
            return
        self.states +=1
        # first recombine all the logic into one string
        new_log = ''.join(logic)
        
        # for the first state being added the input nodes must be determined
        if (not self.inputs):
            ins = set(re.findall('[A-Z]\w+(?:)', new_log))
            inhibs = set(re.findall('(?<=!)\w+', new_log))
            self.inputs = list(ins - inhibs)
            self.inhibitors = list(inhibs)

        # convert the string into one that can be evaluated
        new_log = [self.replace(x) for x in new_log]
        self.logic.append(''.join(new_log))

    def __repr__(self):
        """ Used to be able to print the node in a readable manner"""
        return str(self.cur_state) + ' : ' + str(self.states)
