#!/bin/bash
IFS="
"
for i in `ls *.png`; do
     convert $i ${i%.png}.gif
done
