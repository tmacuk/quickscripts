#!/bin/bash

python case.py $1 | sed 's/\,/\n/g' | tr -d "'" | tr -d " " | tr -d "[" | tr -d "]"

