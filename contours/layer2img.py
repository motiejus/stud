#!/usr/bin/python3
import argparse
import geopandas
import psycopg2
import matplotlib.pyplot as plt

INCH = 25.4  # mm
BROWN = '#d15c00'  # CMYK: 0_56_100_18


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
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('--infile')
    group1.add_argument('--table')
    parser.add_argument('-o', '--outfile', metavar='<file>')
    parser.add_argument(
            '--dpi', type=int, help='Dots per inch', default=300)
    parser.add_argument(
            '--size', type=plt_size, help='Figure size in mm (WWxHH)')

    return parser.parse_args()


def read_layer(maybe_table, maybe_file):
    if maybe_table:
        conn = psycopg2.connect("host=127.0.0.1 dbname=osm user=osm")
        sql = "SELECT geom FROM %s" % maybe_table
        return geopandas.read_postgis(sql, con=conn, geom_col='geom')
    elif maybe_file:
        return geopandas.read_file(maybe_file)


def plot_layer(layer, ax, color):
    layer.plot(ax=ax, color=BROWN, linewidth=.5)


def main():
    args = parse_args()
    layer = read_layer(args.table, args.infile)

    fig, ax = plt.subplots()
    if args.size:
        fig.set_size_inches(args.size)

    plot_layer(layer, ax=ax, color=BROWN)

    ax.axis('off')
    ax.margins(0, 0)
    fig.tight_layout(0)
    if args.outfile:
        fig.savefig(
            args.outfile, bbox_inches=0, dpi=args.dpi,
            pil_kwargs={'compression': 'tiff_deflate'},
        )
    else:
        plt.show()


if __name__ == '__main__':
    main()
