#!/usr/bin/python3
# https://gis.stackexchange.com/questions/131716/plot-shapefile-with-matplotlib

import argparse
import geopandas
import psycopg2
import matplotlib.pyplot as plt

INCH = 25.4  # mm


def plt_size(string):
    if not string:
        # using default matplotlib dimensions
        return None
    try:
        w, h = string.split("x")
        return float(w) / INCH, float(h) / INCH
    except Exception as e:
        raise argparse.ArgumentTypeError from e


def parse_args():
    parser = argparse.ArgumentParser(
            description='Convert geopackage to an image')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--infile', type=str)
    group.add_argument('--table', type=str)
    parser.add_argument('-o', '--outfile', metavar='<file>', type=str)
    parser.add_argument(
            '--size', type=plt_size, help='Figure size in mm (WWxHH)')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.table:
        conn = psycopg2.connect("host=127.0.0.1 dbname=osm user=osm")
        sql = "SELECT geom FROM %s" % args.table
        f = geopandas.read_postgis(sql, con=conn, geom_col='geom')
    else:
        f = geopandas.read_file(args.infile)
    f.plot(figsize=args.size)
    plt.axis('off')
    plt.margins(0, 0)
    plt.tight_layout(0)
    if args.outfile:
        plt.savefig(args.outfile, bbox_inches=0, dpi=300)
    else:
        plt.show()


if __name__ == '__main__':
    main()
