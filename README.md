# Code for QTCS Algorithm

This repository contains a reference implementation of the following paper. QTCS: Efficient Query-Centered Temporal Community Search.  Please contact longlonglin@swu.edu.cn for any questions


# Environment Setup

Our algorithms are implemented in Python 3.10.12 and all experiments are executed on a server with  an Intel (R) Xeon (R) E5-2680 v4@2.40GHZ CPU and 256GB RAM running Ubuntu 18.04. 


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



 ## Running Example
  You may use git to clone the repository from GitHub and run it manually like this:
  
      git clone https://github.com/longlonglin/QTCS.git
      cd QTCS
      python qtcs.py facebook-wall.txt.anon_day
      facebook-wall.txt.anon_day is loading...
      loading_graph_time(s)4.515358924865723
      number of nodes: 45813
      number of static edges: 183412.0
      number of temporal edges: 585743.0
      number of timestamps: 1473
      self.tmax:552
      compute_ttp_time(s)119.09577298164368
      seed33203
      time_tppr(s)2.995162010192871
      egr_time(s)4.52646541595459
      time_expanding(s)0.36696600914001465
      time_reducing(s)0.016901016235351562
      seed55564
      time_tppr(s)0.3347628116607666
      egr_time(s)1.1299402713775635
      time_expanding(s)4.870069742202759
      time_reducing(s)1.2183952331542969
      seed5343
      time_tppr(s)2.8038454055786133
      egr_time(s)4.327779769897461
      time_expanding(s)0.0963292121887207
      time_reducing(s)0.011249542236328125
      seed27543
      time_tppr(s)29.35983681678772
      egr_time(s)30.91551446914673
      time_expanding(s)3.698026180267334
      time_reducing(s)0.19061565399169922
      seed39873
      time_tppr(s)6.759989023208618
      egr_time(s)8.80293869972229
      time_expanding(s)0.11980819702148438
      time_reducing(s)0.002406597137451172





