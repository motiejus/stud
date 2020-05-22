#!/usr/bin/python3
# https://gis.stackexchange.com/questions/131716/plot-shapefile-with-matplotlib

import argparse
import geopandas
import matplotlib.pyplot as plt

INCH = 25.4 # mm

def plt_size(string):
    if not string:
        return None
    try:
        w, h = string.split("x")
        return float(w) / INCH, float(h) / INCH
    except Exception as e:
        raise argparse.ArgumentTypeError from e

def parse_args():
    parser = argparse.ArgumentParser(description='Convert layer to an image')
    parser.add_argument('infile', type=str)
    parser.add_argument('layer', type=str)
    parser.add_argument('-o', '--output', metavar='<file>', type=str)
    parser.add_argument('--size', type=plt_size, help='Figure size in mm (WWxHH)')
    return parser.parse_args()

def main():
    args = parse_args()
    f = geopandas.read_file(args.infile)
    f.plot(figsize=args.size)
    plt.axis('off')
    plt.margins(0, 0)
    plt.tight_layout(0)
    if args.output:
        plt.savefig(args.output, bbox_inches=0, dpi=300)
    else:
        plt.show()

if __name__ == '__main__':
    main()
