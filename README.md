# Code for QTCS Algorithm

This repository contains a reference implementation of the algorithms for the paper:

QTCS: Efficient Query-Centered Temporal Community Search


## Environment Setup

Codes run on Python 3.7 or later. [PyPy](http://pypy.org/) compiler is recommended because it can make the computations quicker without changing the codes.


## Dataset description
We focus on mining the temporal network so each edge is associated with a timestamp. Temporal edges are stored at the raw data in which each line is one temporal edge.
 
| from_id | \t  | to_id    | \t  |  timestamps  |
| :----:  |:----: | :----:   |:----:   | :----: |

Rmin can be downloaded from http://konect.cc/networks/mit/

Lyon and Thiers can be downloaded from http://www.sociopatterns.org/datasets/co-location-data-for-several-sociopatterns-data-sets/

Facebook can be downloaded from  http://konect.cc/networks/facebook-wosn-wall/

Twitter can be downloaded from http://snap.stanford.edu/data/higgs-twitter.html

Enron can be downloaded from http://konect.cc/networks/enron-rm/

Lkml can be downloaded from http://konect.cc/networks/lkml-reply/

DBLP can be downloaded from http://konect.cc/networks/dblp_coauthor/ or https://dblp.uni-trier.de/xml/ 

## Running example
python qtcs.py  facebook-wall.txt.anon_day

