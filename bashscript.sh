#!/usr/bin/env bash

for i in {1..5}; do
    touch touchfiles/something$i
    git add -A .
    git commit --date "$i days ago" -m "test"
done
