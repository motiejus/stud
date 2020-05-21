#!/usr/bin/python3
# https://gis.stackexchange.com/questions/131716/plot-shapefile-with-matplotlib

import argparse
import fiona
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description='Convert layer to a nice PDF')
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('layer', type=str)
    parser.add_argument('-o', metavar='OUTFILE', type=argparse.FileType('w'))
    args = parser.parse_args()

if __name__ == '__main__':
    main()
