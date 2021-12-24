from Model import Model
import argparse

def main(args):
    model = Model(args.m, args.graph)
    model.sim(args.i, args.o)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Main script to run the simulations')
    parser.add_argument('-i', help='input file', type=str, default='Inputs/EGF/NoLigand')
    parser.add_argument('-o', help='output dir', type=str, default='Outputs/EGF/NoLigand.out')
    parser.add_argument('-m', help='model file', type=str, default='Models/CoreModels/EGF.mod')
    parser.add_argument('-graph', help='out a graph', type=bool, default=False)

    args = parser.parse_args()
    main(args)