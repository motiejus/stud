#!/usr/bin/awk -f

# Beginning of a section ("part") starts with:
# \partNUMBER{
# where NUMBER := (one | two | three | four). The ^ and $ signify line's
# beginning and end marks. When section begins, assign `idx` to its number.
/^\\partone\{$/   { idx=1; }
/^\\parttwo\{$/   { idx=2; }
/^\\partthree\{$/ { idx=3; }
/^\\partfour\{$/  { idx=4; }

# Section ends with "}" as a sole character in the line.
/^\}$/ { idx=0; }

# If idx != 0 (we are in part1,2,3 or 4), increase part's counter by the number
# of characters in the line.
idx != 0 {
    part[idx] += length($0);
}

# End of the script: we have part[idx], where idx := [1,4], and the
# value is the number of characters.
END {
    printf("number of characters in part1: %d\n", part[1]);
    printf("number of characters in part2: %d\n", part[2]);
    printf("number of characters in part3: %d\n", part[3]);
    printf("number of characters in part4: %d\n", part[4]);
}
