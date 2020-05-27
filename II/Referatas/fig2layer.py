#!/usr/bin/python
import argparse

from math import pi
from pyproj import CRS
import numpy as np
import geopandas as gpd
from shapely.geometry import LineString, MultiLineString

BOUNDS = ('xmin', 'ymin', 'xmax', 'ymax')


def write_file(args, geom):
    df = gpd.GeoDataFrame(crs=CRS(3346))
    df['geometry'] = None
    df.loc[0, 'geometry'] = geom
    df.to_file(args.outfile, driver='GPKG')


def sinewave(args):
    INTERVAL = 0.1

    if args.numwaves == 2:
        TAIL_LEN, SINE_LEN = 7, 7
        TAILS = np.zeros(int(TAIL_LEN / INTERVAL))
        sin_range = np.arange(-pi/4, SINE_LEN, INTERVAL) * pi / 2
        amplitude = (np.sin(sin_range)+1)*2
    else:
        TAIL_LEN, SINE_LEN = 3.5, 3.5
        TAILS = np.zeros(int(TAIL_LEN / INTERVAL))
        sin_range = np.arange(-pi/4, SINE_LEN - pi/8, INTERVAL) * pi / 2
        amplitude = np.sin(sin_range) + 1

    y = np.concatenate([TAILS, amplitude, TAILS])
    x = np.arange(-TAIL_LEN - pi/4, SINE_LEN + TAIL_LEN, INTERVAL)
    lines = LineString(zip(x*10, y*10))
    geom = MultiLineString([lines])
    write_file(args, geom)


def rectangle(args):
    line = LineString((
        (args.bounds[0], args.bounds[1]),
        (args.bounds[0], args.bounds[3]),
        (args.bounds[2], args.bounds[3]),
        (args.bounds[2], args.bounds[1]),
        (args.bounds[0], args.bounds[1]),
    ))
    write_file(args, MultiLineString([line]))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outfile', metavar='<file>', required=True)
    subparsers = parser.add_subparsers()
    sine = subparsers.add_parser('sine', help='Sine wave')
    sine.add_argument('--numwaves', choices=[1, 2], type=int, help='Number of waves')
    sine.set_defaults(func=sinewave)
    rect = subparsers.add_parser('rect', help='Rectangle')
    rect.add_argument('--bounds', type=float, nargs=4, metavar=BOUNDS)
    rect.set_defaults(func=rectangle)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    args.func(args)
