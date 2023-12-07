# Code for QTCS Algorithm

This repository contains a reference implementation of the algorithms for QTCS: Efficient Query-Centered Temporal Community Search.


## Environment Setup

Our algorithms are implemented in Python 3.10.12 and all experiments are executed on a server with  an Intel (R) Xeon (R) E5-2680 v4@2.40GHZ CPU and 256GB RAM running Ubuntu 18.04. 

You may use Git to clone the repository from GitHub and run it manually like this:

git clone https://github.com/longlonglin/QTCS.git
cd QTCS
python qtcs.py  facebook-wall.txt.anon_day

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


## Tips

Due to the limit of space, we only upload some datasets of small size here. Welcome to e-mail me for more datasets of temporal networks.

