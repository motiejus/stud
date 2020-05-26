#!/usr/bin/python
from pyproj import CRS
import numpy as np
import geopandas as gpd
from shapely.geometry import LineString

INTERVAL = 0.5
TAIL_LEN = 4
SINE_LEN = 7


def main():
    tails = np.zeros(int(TAIL_LEN / INTERVAL))
    amplitude = np.sin(np.arange(0, SINE_LEN, INTERVAL))
    y = np.concatenate([tails, amplitude, tails])
    x = np.arange(-TAIL_LEN, SINE_LEN+TAIL_LEN, INTERVAL)
    geom = LineString(zip(x, y))
    df = gpd.GeoDataFrame(crs=CRS(3346))
    df['geometry'] = None
    df.loc[0, 'geometry'] = geom
    df.to_file("sinewave.json", driver='GeoJSON')


if __name__ == '__main__':
    main()
