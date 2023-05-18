# Code for QTCS Algorithm

This repository contains a reference implementation of the algorithms for the paper:

Fast Query-Centered Temporal Community Search


## Environment Setup

Codes run on Python 3.7 or later. [PyPy](http://pypy.org/) compiler is recommended because it can make the computations quicker without change the codes.


## Dateset description
We focus on mining the temporal network so each edge is associated with a timestamp. Temporal edges are stored at the raw data in which each line is one temporal edge.
 
| from_id | \t  | to_id    | \t  |  timestamps  |
| :----:  |:----: | :----:   |:----:   | :----: |


## Running example
python qtcs.py  facebook-wall.txt.anon_day
