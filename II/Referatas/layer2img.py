#!/usr/bin/python3
# https://gis.stackexchange.com/questions/131716/plot-shapefile-with-matplotlib

import argparse
import geopandas
import psycopg2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    parser.add_argument(
            '--clip', type=float, nargs=4,
            metavar=('xmin', 'ymin', 'xmax', 'ymax'))
    parser.add_argument(
            '--rect', type=float, nargs=4, help="Overlay a rectangle",
            metavar=('xmin', 'ymin', 'xmax', 'ymax'))
    return parser.parse_args()


def main():
    args = parse_args()
    if args.table:
        conn = psycopg2.connect("host=127.0.0.1 dbname=osm user=osm")
        sql = "SELECT geom FROM %s" % args.table
        f = geopandas.read_postgis(sql, con=conn, geom_col='geom')
    else:
        f = geopandas.read_file(args.infile)
    fig, ax = plt.subplots()
    f.plot(ax=ax, figsize=args.size)
    if c := args.clip:
        ax.set_xlim(left=c[0], right=c[2])
        ax.set_ylim(bottom=c[1], top=c[3])
    if r := args.rect:
        w, h = r[2] - r[0], r[3] - r[1]
        rect = patches.Rectangle(
                (r[0], r[1]),
                w, h,
                linewidth=1,edgecolor='r',facecolor='none')
        ax.add_patch(rect)

    ax.axis('off')
    ax.margins(0, 0)
    fig.tight_layout(0)
    if args.outfile:
        fig.savefig(args.outfile, bbox_inches=0, dpi=600)
    else:
        plt.show()


if __name__ == '__main__':
    main()
