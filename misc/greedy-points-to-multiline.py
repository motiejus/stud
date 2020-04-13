#!/usr/bin/env python3
"""
This script takes a point layer and connects them all in a "greedy" way: it
will take a random point, connect its closest one, and repeat the loop until
all of the points are connected.

This is useful if you have point area boudnaries and want to make a real
connected polygon.
"""

import sys
import rtree
import os
from osgeo import ogr


def main():
    driver = ogr.GetDriverByName('gpkg')

    inDataSource = driver.Open(sys.argv[1], 0)
    inLayer = inDataSource.GetLayer()
    srs = inLayer.GetSpatialRef()
    outDataSource = driver.CreateDataSource(sys.argv[2])
    outLayerName, _ = os.path.splitext(os.path.basename(sys.argv[2]))
    outLayer = outDataSource.CreateLayer(
            outLayerName,
            srs,
            geom_type=ogr.wkbLineString
    )

    points = extract_layer_points(inLayer)
    path = greedy_path(points)
    write_path(srs, outLayer, path)

    inDataSource.Destroy()
    outDataSource.Destroy()


def extract_layer_points(layer):
    """Extracts points from layer in a format:
        dict(
          i : int
          points: (x, y : int)
        )
    """
    points = {}
    for (i, pt) in enumerate(layer):
        p = pt.GetGeometryRef().GetPoint()
        points[i] = (p[0], p[1])
    return points


def greedy_path(points):
    """Given a dict of points, return a "greedy" path between them.

    It will start with a random point, and keep navigating to the closest one,
    until all the points have been visited.
    """
    idx = rtree.index.Index(interleaved=False)
    for (i, pt) in points.items():
        idx.insert(i, pt)

    def _bounds(_pts):
        return (_pts[0], _pts[0], _pts[1], _pts[1])

    ret = [0]
    idx.delete(0, _bounds(points[0]))
    while len(ret) < len(points):
        pt = _bounds(points[ret[-1]])
        nearest = next(idx.nearest(pt))
        ret.append(nearest)
        idx.delete(nearest, _bounds(points[nearest]))
    ret.append(0)
    return [points[point] for point in ret]


def write_path(srs, outLayer, path):
    "writes the linestring (path) to the outLayer."
    line = ogr.Geometry(ogr.wkbLineString)
    for point in path:
        line.AddPoint(point[0], point[1])

    outFeature = ogr.Feature(outLayer.GetLayerDefn())
    outFeature.SetGeometry(line)
    outLayer.CreateFeature(outFeature)


if __name__ == '__main__':
    main()
