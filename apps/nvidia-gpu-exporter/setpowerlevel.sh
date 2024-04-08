#!/bin/bash

if ! test -f $1; then
  exit 0
fi

count=$(yq '.limits | length' $1)
eval "$(yq -o=shell $1)"

for i in $(seq 0 $((count-1)));
do
    pl=limits_$i
    nvidia-smi -i $i -pl ${!pl}
done

sleep infinity
