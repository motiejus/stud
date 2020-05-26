#!/usr/bin/python
from math import pi
from pyproj import CRS
import numpy as np
import geopandas as gpd
from shapely.geometry import LineString

INTERVAL = 0.1
TAIL_LEN = 4
SINE_LEN = 7

TAILS = np.zeros(int(TAIL_LEN / INTERVAL))


def main():
    sin_range = np.arange(-pi/4, SINE_LEN, INTERVAL)
    amplitude = np.sin(sin_range * pi / 2) + 1
    y = np.concatenate([TAILS, amplitude, TAILS])
    x = np.arange(-TAIL_LEN - pi/4, SINE_LEN + TAIL_LEN, INTERVAL)
    geom = LineString(zip(x, y))
    df = gpd.GeoDataFrame(crs=CRS(3346))
    df['geometry'] = None
    df.loc[0, 'geometry'] = geom
    df.to_file("sinewave.json", driver='GeoJSON')


if __name__ == '__main__':
    main()
