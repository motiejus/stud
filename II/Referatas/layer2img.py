#!/usr/bin/python3
# blue: #377eb8

import argparse
import geopandas
import psycopg2
import matplotlib.pyplot as plt

from matplotlib import rc, patches

INCH = 25.4  # mm
BOUNDS = ('xmin', 'ymin', 'xmax', 'ymax')


def plt_size(string):
    if not string:
        return None
    try:
        w, h = string.split("x")
        return float(w) / INCH, float(h) / INCH
    except Exception as e:
        raise argparse.ArgumentTypeError from e


def parse_args():
    parser = argparse.ArgumentParser(
            description='Convert geopackage to an image')
    ingroup = parser.add_mutually_exclusive_group(required=True)
    ingroup.add_argument('--infile')
    ingroup.add_argument('--table')
    parser.add_argument('-o', '--outfile', metavar='<file>')
    parser.add_argument(
            '--size', type=plt_size, help='Figure size in mm (WWxHH)')
    parser.add_argument( '--clip', type=float, nargs=4, metavar=BOUNDS)

    overlay = parser.add_mutually_exclusive_group()
    overlay.add_argument('--overlay-infile', type=str)
    overlay.add_argument('--overlay-table', type=str)
    return parser.parse_args()


def read_layer(maybe_table, maybe_file):
    if maybe_table:
        conn = psycopg2.connect("host=127.0.0.1 dbname=osm user=osm")
        sql = "SELECT geom FROM %s" % maybe_table
        return geopandas.read_postgis(sql, con=conn, geom_col='geom')
    elif maybe_file:
        return geopandas.read_file(maybe_file)


def main():
    args = parse_args()
    primary = read_layer(args.table, args.infile)
    overlay = read_layer(args.overlay_table, args.overlay_infile)

    rc('text', usetex=True)
    fig, ax = plt.subplots()
    if args.size:
        fig.set_size_inches(args.size)
    primary.plot(ax=ax, color='#4daf4a')
    if c := args.clip:
        ax.set_xlim(left=c[0], right=c[2])
        ax.set_ylim(bottom=c[1], top=c[3])

    if overlay is not None:
        overlay.plot(ax=ax, color='#e41a1c')

    ax.axis('off')
    ax.margins(0, 0)
    fig.tight_layout(0)
    if args.outfile:
        fig.savefig(args.outfile, bbox_inches=0, dpi=600)
    else:
        plt.show()


if __name__ == '__main__':
    main()
