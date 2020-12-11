Countour line generator from LIDAR data
---------------------------------------

Usage:

1. Download contour lines in format `6062999.75,584000.75,88.07`: coordinate
   pair and height (in meters) to `DTM_XX_YY_N.zip` files.
2. Adjust `BOUNDS` in the Makefile.
3. Run `make -j$(nproc) smooth_<X>.gpkg`. This will output a geo-package with
   contour lines every `X` meters. X can be fractional (e.g.
   `smooth_2.5.gpkg`).
4. Optional: you may generate a raster image with `layer2img.py`.

Dependencies:

- postgis
- gdal-bin
- unzip

TODO:

1. Replace `managedb` stack with postgis-over-docker. This will lead to a less
   fragile postgis setup.
2. Accept `BOUNDS` in a way that does not require to change the Makefile.

License
-------

Code in this directory is public domain.
