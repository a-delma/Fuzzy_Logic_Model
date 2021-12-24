from Node import Node
import networkx as nx
import matplotlib.pyplot as plt
import sys
from os import listdir
from os.path import isfile, join, splitext
from fuzzy_logic import feq

def color_map(i):
    """ Returns a mapping for terinary states """
    if i == 0:
        return 0.
    elif i == 1:
        return 0.5
    else:
        return 1.0

class Model:
    """ Defines the basic model for a pathway
    
        Takes a .mod file to definet the archetecture
    """
    def __init__(self, infile, graphing):

        # intializastion of the variables
        self.G = nx.MultiGraph()
        self.nodes = {}
        self.inputs = {}
        self.black_edges = []
        self.red_edges = []
        # sadly i could not get them to work with states because of how the color map works
        # self.one_states = [] 
        # self.two_states = [] 

        # marks if a graph should be output
        # outputs a graph to /img/ for each step of the iteration
        self.graphing=graphing 

        # inititalization of the nodes + graph
        self.parse_input(infile)
        self.make_graph()

    def get_states(self):
        """ Returns a list of the current node states """
        states = {}
        for i in self.nodes:
            states[i] = self.nodes[i].cur_state
        return states

    def sim(self, in_file, out_file):
        """ Function for simulation of inputs and prints the final state"""
        self.init(in_file)
        self.run(15) # most states should finsish after 15 updates
        self.output(out_file)

    def init(self, infile):
        """ Takes file containing the inputs and updates states of the nodes """
        for i in self.nodes: # resets the current nodes if they already exist
            self.nodes[i].cur_state=0
        with open(infile) as f: # reading in the interaction logic
            lines = f.readlines()
        
        # mostly just string processing
        lines = [i.replace('\n', '').split(',') for i in lines]
        inputs_states = {}
        for i in lines:
            for j in i:
                j = j.replace(',', '')
                j = j.strip()
                if j != '':
                    if j[-3:] == '(2)':
                        inputs_states[j[:-4]] = 2
                    else:
                        inputs_states[j] = 1
        self.draw_graph(0)
        for i in inputs_states: # Assigns the new states to the nodes
            self.nodes[i].cur_state = inputs_states[i]
        self.draw_graph(1)

    def run(self, dur=15):
        """ A function that iteratively updates the states of each node """
        for i in range(dur):
            states = self.get_states()
            for j in self.nodes:
                if j not in self.inputs:
                    self.nodes[j].call(states)
            # print("Step %d: " % (i), self.nodes)
            self.draw_graph(i+2)

    def output(self, outfile):
        """ Takes a file and print the active nodes to it"""
        f = open(outfile, "w")
        # print(self.nodes)
        for i in self.nodes:
            if self.nodes[i].cur_state == 1:
                f.write('%s\n' % (i))
            elif self.nodes[i].cur_state == 2:
                f.write('%s (2)\n' % (i))
        f.close()
        
    def parse_input(self, infile):
        """ Takes in a mod file and constructs the model from its logic """
        with open(infile) as f:
            lines = f.readlines()
        
        # goes line by line and adds each new node or state
        for line in lines:
            units = line.split()
            if units[2] == 'input': # input nodes
                inNode = Node()
                inNode.add_state('input')
                self.nodes[units[0]] = inNode
                self.inputs[units[0]] = inNode
            elif units[1] == '2': # addding an additional state to a previous node
                innerNode = self.nodes[units[0]]
                innerNode.add_state(units[2:])
            else: # adding a new inner node
                innerNode = Node()
                innerNode.add_state(units[2:])
                self.nodes[units[0]] = innerNode

    def make_graph(self):
        """ Function for creating the networkx graph """
        self.G.add_nodes_from(self.nodes)
        for i in self.nodes:
            self.black_edges += [(x, i, 1) for x in self.nodes[i].inputs]
            self.red_edges += [(x, i, 1) for x in self.nodes[i].inhibitors]
            if self.nodes[i].states == 2:
                self.two_states.append(i)
            else:
                self.one_states.append(i)
        self.G.add_weighted_edges_from(self.black_edges)
        self.G.add_weighted_edges_from(self.red_edges)

    def draw_graph(self, ind):
        """ Prints the current state of the model to matplotlib using networkx """

        if not self.graphing:
            return

        pos = nx.spring_layout(self.G, k=0.55, seed=9)

        # print(self.one_states)

        # getting the color map for each node
        # one_colors = [color_map(self.nodes[i].cur_state) for i in self.one_states]
        # two_colors = [color_map(self.nodes[i].cur_state) for i in self.two_states]
        colors = [color_map(self.nodes[i].cur_state) for i in self.nodes]

        # for (idk, s) in enumerate(self.one_states):
        #     print(one_colors[idk],s)
        # for (idk, s) in enumerate(self.two_states):
        #     print(two_colors[idk],s)

        nx.draw_networkx_labels(self.G, pos)
        # nx.draw_networkx_nodes(self.G, pos, cmap=plt.get_cmap('cool'), node_color=one_colors, node_size=500, alpha=0.5, node_shape='o', nodelist=self.one_states) 
        # nx.draw_networkx_nodes(self.G, pos, cmap=plt.get_cmap('cool'), node_color=two_colors, node_size=500, alpha=0.5, node_shape='s', nodelist=self.two_states) 
        nx.draw_networkx_nodes(self.G, pos, cmap=plt.get_cmap('cool'), node_color=colors, alpha=0.5)
        nx.draw_networkx_edges(self.G, pos, edgelist=self.black_edges, edge_color='k', arrows=True)
        nx.draw_networkx_edges(self.G, pos, edgelist=self.red_edges,   edge_color='r', arrows=True)
        
        # currently set to plot, but comments can be changed to print to a file instead
        # plt.show()
        plt.savefig("img/graph-%03d.png" % (ind), format="PNG")
        # plt.savefig("img/models/%s.png" % (ind), format="PNG")
        plt.clf()
