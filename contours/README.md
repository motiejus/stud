Countour line generator from LIDAR data
---------------------------------------

This accepts two kinds of contour data:

**2017 variant**: y, x, z, separated by commas:
```
6062999.75,584000.75,88.07
```

Recommended whenever available. It is more dense, gridded (thus much faster),
but not available outside major cities.

**2009 variant**: x, y, z, separated by one or more spaces:
```
 501991.670  6150000.000  57.689
```

2009 variant is less dense, non-gridded, therefore significantly slower
(`gdal_grid` must be used as an extra step, which is slow). This variant is
less robust, but available throughout the country.

Usage
-----

1. Download contour lines to zip files in this directory.
2. Adjust `BOUNDS` and `VARIANT` in `config.mk`.
3. Run `make -j$(nproc) smooth_<X>.gpkg`. This will output a geo-package with
   contour lines every `X` meters. X can be fractional (e.g.
   `smooth_2.5.gpkg`).
4. Optional: you may generate a raster image with `layer2img.py`.

Dependencies for a Linux system:

- docker
- psql (client only)
- gdal-bin
- unzip
- awk

Example
-------

![Užupis](https://github.com/motiejus/stud/blob/master/contours/example.jpg?raw=true)

License
-------

Code in this directory is public domain.
