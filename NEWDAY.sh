#!/usr/bin/env bash
if [ $1 -lt 10 ]; then
    D="0$1";
else
    D="$1";
fi
mkdir day$D; cd day$D
touch sample;
cp ../template main.py
curl -o puzzle-input -b 'session=?' https://adventofcode.com/2022/day/$1/input
