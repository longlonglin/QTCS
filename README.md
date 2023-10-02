# Code for QTCS Algorithm

This repository contains a reference implementation of the algorithms for the paper:

QTCS: Efficient Query-Centered Temporal Community Search


## Environment Setup

Codes run on Python 3.7 or later. [PyPy](http://pypy.org/) compiler is recommended because it can make the computations quicker without changing the codes.


## Dataset description
We focus on mining the temporal network so each edge is associated with a timestamp. Temporal edges are stored at the raw data in which each line is one temporal edge.
 
| from_id | \t  | to_id    | \t  |  timestamps  |
| :----:  |:----: | :----:   |:----:   | :----: |

Rmin can be downloaded from http://konect.cc/networks/mit/, Aug. 2021
Lyon and Thiers can be downloaded from http://konect.cc/networks/mit/, Aug. 2021 or http://snap.stanford.edu/data/index.html
Facebook can be downloaded from  http://konect.cc/networks/facebook-wosn-wall/, Aug. 2021.
Twitter can be downloaded from http://snap.stanford.edu/data/higgs-twitter.html, Aug. 2021
Enron can be downloaded from http://konect.cc/networks/enron-rm/, Aug. 2021.
Lkml can be downloaded from http://konect.cc/networks/lkml-reply/, Aug. 2021.
DBLP can be downloaded from http://konect.cc/networks/dblp coauthor/, Aug. 2021 or https://dblp.uni-trier.de/xml/.

## Running example
python qtcs.py  facebook-wall.txt.anon_day

