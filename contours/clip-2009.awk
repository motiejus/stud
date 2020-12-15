#!/usr/bin/awk -f

# this file works with SEZP from circa 2009, where x coordinate (the 6-digit one)
# is first, and the field separator is ' ' or more spaces.
$1 > xmin && $1 < xmax && $2 > ymin && $2 < ymax {
    print $1 "," $2 "," $3
}
