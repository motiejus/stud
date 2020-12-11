#!/usr/bin/awk -f
BEGIN {
    FS = ","
}

$1 > ymin && $1 < ymax && $2 > xmin && $2 < xmax {
    print $2 "," $1 "," $3
}
