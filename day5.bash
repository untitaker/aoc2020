#!/bin/bash

seat_ids="$(cat day5.input.txt | tr F 0 | tr B 1 | tr R 1 | tr L 0 | xargs -P20 -n1 -I{} bash -c 'echo $((2#{}))' | sort -h)"

echo -n "part 1: "
echo "$seat_ids" | tail -1

echo -n "part 2: "
a=0
for b in $seat_ids; do
    [ $a = $(($b - 2)) ] && echo $(($a + 1))
    a=$b
done
