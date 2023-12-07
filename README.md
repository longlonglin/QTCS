# QTCS: Efficient Query-Centered Temporal Community Search


# Environment Setup

Our algorithms are implemented in Python 3.10.12 and all experiments are executed on a server with  an Intel (R) Xeon (R) E5-2680 v4@2.40GHZ CPU and 256GB RAM running Ubuntu 18.04. 


# Dataset
We focus on identifying the communities from a temporal network, in which each temporal edge is associated with a timestamp. In particular, temporal edges are stored in the raw data where each line is one temporal edge.
 
| from_id | \t  | to_id    | \t  |  timestamps  |
| :----:  |:----: | :----:   |:----:   | :----: |

Due to the space limit, we only upload some small datasets. But, you can download all original datasets used in our paper from the following table or the preprocessed datasets from 
    
    https://www.dropbox.com/scl/fo/90casjr51m85wr5l5duhm/h?rlkey=zvgyxhhxxu4qvq6c4iiqvxp5p&dl=0. 
    
If you have any questions, please contact longlonglin@swu.edu.cn

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



 # Usage
  You may use git to clone the repository from GitHub and run it manually like this
  
      git clone https://github.com/longlonglin/QTCS.git
      cd QTCS
      python qtcs.py data/Facebook
  The running results are as follows
  
      data/Facebook is loading...
     loading_graph_time(s)4.507202625274658
     number of nodes: 45813
     number of static edges: 183412.0
     number of temporal edges: 585743.0
     number of timestamp: 1473
     self.tmax:552
     compute_ttp_time(s)113.53539848327637
     seed25115
     time_tppr(s)2.2104275226593018
     egr_time(s)3.710035562515259
     time_expanding(s)0.10440444946289062
     time_reducing(s)0.013033390045166016
     seed8401
     time_tppr(s)83.49688935279846
     egr_time(s)85.08008170127869
     time_expanding(s)39.289947748184204
     time_reducing(s)0.5261859893798828
     seed16973
     time_tppr(s)2.932955265045166
     egr_time(s)5.026332855224609
     time_expanding(s)1.946237325668335
     time_reducing(s)0.24632477760314941
     seed38625
     time_tppr(s)20.524596691131592
     egr_time(s)22.073683977127075
     time_expanding(s)2.5056912899017334
     time_reducing(s)0.0404210090637207
     seed29551
     time_tppr(s)1.3863840103149414
     egr_time(s)2.8778045177459717
     time_expanding(s)0.025407791137695312
     time_reducing(s)0.0007688999176025391


Our model has only one parameter, ``alpha``, which ranges from 0 to 1, and its default value is 0.2. If you want to change ``alpha``, you can modify it in line 553 of qtcs.py.


