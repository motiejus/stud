#!/usr/bin/env python3

import sys
import rtree
import os
from osgeo import ogr

def main():
    infile = sys.argv[1]
    driver = ogr.GetDriverByName('gpkg')
    inDataSource = driver.Open(infile, 0)
    inLayer = inDataSource.GetLayer()
    srs = inLayer.GetSpatialRef()

    points = get_points(inLayer)
    path = greedy_path(points)

    outDataSource = driver.CreateDataSource(sys.argv[2])
    outLayerName, _ = os.path.splitext(os.path.basename(sys.argv[2]))
    outLayer = outDataSource.CreateLayer(outLayerName, srs, geom_type=ogr.wkbLineString)

    line = ogr.Geometry(ogr.wkbLineString)
    for point in path:
        line.AddPoint(point[0], point[1])

    outFeature = ogr.Feature(outLayer.GetLayerDefn())
    outFeature.SetGeometry(line)
    outLayer.CreateFeature(outFeature)

    inDataSource.Destroy()
    outFeature.Destroy()
    outDataSource.Destroy()

def get_points(layer):
    points = {}
    for (i, pt) in enumerate(layer):
        p = pt.GetGeometryRef().GetPoint()
        points[i] = (p[0], p[1])
    return points

def greedy_path(points):
    "Given a dict of points, return a localized short path between them."
    idx = rtree.index.Index(interleaved = False)
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
        

if __name__ == '__main__':
    main()
