#!/usr/bin/env bash

for i in {245..450}; do
    touch touchfiles/something$i
    git add -A .
    git commit --date "$i days ago" -m "test"
    touch touchfiles/somethinga$i
    git add -A .
    git commit --date "$i days ago" -m "test"
done
