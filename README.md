# Code for QTCS Algorithm

This repository contains a reference implementation of the following paper. QTCS: Efficient Query-Centered Temporal Community Search.  Please contact longlonglin@swu.edu.cn for any questions


# Environment Setup

Our algorithms are implemented in Python 3.10.12 and all experiments are executed on a server with  an Intel (R) Xeon (R) E5-2680  v4@2.40GHZ  CPU and 256GB RAM running Ubuntu 18.04. 


# Dataset description
We focus on identifying the communities from a temporal network, in which each temporal edge is associated with a timestamp. In particular, temporal edges are stored in the raw data where each line is one temporal edge.
 
| from_id | \t  | to_id    | \t  |  timestamps  |
| :----:  |:----: | :----:   |:----:   | :----: |

Due to the space limit, we only upload some small datasets. But, you can download all datasets used in our paper from the following table

| Datasets | URLs  |
| :----:  |:----: | 
| Rmin | http://konect.cc/networks/mit/|
| Lyon | http://www.sociopatterns.org/datasets/co-location-data-for-several-sociopatterns-data-sets/|
| Thiers | http://www.sociopatterns.org/datasets/co-location-data-for-several-sociopatterns-data-sets/|
|Facebook |  http://konect.cc/networks/facebook-wosn-wall/|
| Twitter | http://snap.stanford.edu/data/higgs-twitter.html|
| Enron | http://konect.cc/networks/enron-rm/ |
| Lkml | http://konect.cc/networks/lkml-reply/|
| DBLP | http://konect.cc/networks/dblp_coauthor/ or https://dblp.uni-trier.de/xml/ |



## Running example
cd ./TSE-Aroc/off-chain-patch-generation-system/Aroc/
      mkdir build
      cd build
      cmake ..
      make
  The executable file called `aroc` will be in the folder build/aroc/
python qtcs.py  facebook-wall.txt.anon_day





