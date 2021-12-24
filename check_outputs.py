from os import listdir
from os.path import isfile, join, splitext


""" A script for comparing the output of our model with the given models

    Compares the files in Outputs/'graph'/*.out to TrueValues/'graph'/*.out
"""


graph = 'FGF'
out = 'Outputs/' + graph
true = 'TrueValues/' + graph

# out = 'Inputs/EGF'

onlyfiles = [f for f in listdir(out) if isfile(join(out, f))]
for f in onlyfiles:
    with open(join(out, f)) as r:
        lines = r.readlines()
    lines = [l.replace('\n', '') for l in lines]
    lines.sort()
    my_lines = set(lines)
    with open(join(true, f[:-4])) as r:
            lines = r.readlines()
    true_out = {}
    lines = [i.replace('\n', '').split(',') for i in lines]
    lines = [item.strip() for sublist in lines for item in sublist if item != '']
    lines.sort()
    true_lines = set(lines)
    print("Checking: ", f)
    print("M: ", my_lines)
    print("T: ", true_lines)