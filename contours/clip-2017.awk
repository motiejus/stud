#!/usr/bin/awk -f
#
# this file works with SEZP circa ~2017 where y coordinate (the 7-digit one) is
# first, and the field separator is ','
BEGIN {
    FS = ","
}

$1 > ymin && $1 < ymax && $2 > xmin && $2 < xmax {
    print $2 "," $1 "," $3
}
