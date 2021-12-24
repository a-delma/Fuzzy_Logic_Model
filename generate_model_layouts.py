from Model import Model
from os import listdir
from os.path import isfile, join, splitext

def generate_model_layouts():
    """ Generates the base model image for each pathway """
    in_dir = 'Models/CoreModels/'
    onlyfiles = [f for f in listdir(in_dir) if isfile(join(in_dir, f))]


    for i in onlyfiles:

        print("processing:", i)
        name = i[:-4]
        EGFModel = Model('./Models/CoreModels/%s.mod' % (name), True)
        # EGFModel.init('./Inputs/EGF/aopGain')
        # EGFModel.run(15)
        EGFModel.draw_graph(name)

if __name__ == "__main__":
    generate_model_layouts()