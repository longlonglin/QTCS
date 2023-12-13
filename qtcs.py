# -*- coding:utf-8 -*-

import sys
from random import choice
from binary_heap import *
from collections import defaultdict
import time
class Graph:

    def __init__(self, dataset):
        self.dataset = dataset
        self.tadj_list, self.edge_stream,self.T = self.TemporalGraph()
        print("number of nodes: " + str(len(self.tadj_list)))
        number, self.tmax = 0, 0
        for u in self.tadj_list:
            tset = set()
            number += len(self.tadj_list[u])
            for v in self.tadj_list[u]:
                for t in self.tadj_list[u][v]:
                    tset.add(t)
            if len(tset) > self.tmax:
                self.tmax = len(tset)
        print("number of static edges: " + str(number / 2))
        print("number of temporal edges: " + str(len(self.edge_stream) / 2))
        print("number of timestamp: "+str(self.T))
        print("self.tmax:" + str(self.tmax))
        self.number_temporal_edge=len(self.edge_stream) / 2
        self.ttp, self.dangling_state, self.t_vertex,self.number_t_vertex = self.Ttp()



    def TemporalGraph(self):
        tadj_list, temp = {}, set()
        print(self.dataset + " is loading...")
        starttime = time.time()
        with open(self.dataset, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.split()
                from_id, to_id, time_id = int(line[0]), int(line[1]), int(line[2])
                if from_id == to_id:
                    continue
                for (f_id, t_id) in [(from_id, to_id), (to_id, from_id)]:
                    temp.add((f_id, t_id, time_id))
        temp = list(temp)
        temp.sort(key=lambda x: x[2])
        edge_stream = [(temp[0][0], temp[0][1], 1)]
        t_index, t_current = 1, temp[0][2]
        for i in range(1, len(temp)):
            if temp[i][2] != t_current:
                t_index += 1
                t_current = temp[i][2]
            edge_stream.append((temp[i][0], temp[i][1], t_index))
        for f_id, t_id, time_id in edge_stream:
            if f_id in tadj_list:
                if t_id in tadj_list[f_id]:
                    tadj_list[f_id][t_id].add(time_id)
                else:
                    tadj_list[f_id][t_id] = {time_id}
            else:
                tadj_list[f_id] = {}
                tadj_list[f_id][t_id] = {time_id}
        endtime = time.time()
        print("loading_graph_time(s)" + str(endtime - starttime))
        return (tadj_list, edge_stream,t_index)

    def Ttp(self):
        starttime = time.time()
        ttp, tnode_out_adj_list = {}, {}
        dangling_state = set()
        for (u, v, t) in self.edge_stream:
            if u in tnode_out_adj_list:
                for t1 in tnode_out_adj_list[u]:
                    if t1 == t:
                        continue
                    tnode_out_adj_list[u][t1].add((v, t))
            if v in tnode_out_adj_list:
                tnode_out_adj_list[v][t] = set()
            else:
                tnode_out_adj_list[v] = {}
                tnode_out_adj_list[v][t] = set()
        for v in tnode_out_adj_list:
            for t in tnode_out_adj_list[v]:
                ttp[(v, t)] = {}
                if len(tnode_out_adj_list[v][t]) == 0:
                    ttp[(v, t)][(v, t)] = 1
                    dangling_state.add((v, t))
                    continue
                sum1 = 0
                for (u, t1) in tnode_out_adj_list[v][t]:
                    sum1 = sum1 + self.f(t1 - t)
                for (u, t1) in tnode_out_adj_list[v][t]:
                    ttp[(v, t)][(u, t1)] = (self.f(t1 - t)) / sum1
        endtime = time.time()
        print("compute_ttp_time(s)" + str(endtime - starttime))

        t_vertex = {}
        number_t_vertex=0

        for u in self.tadj_list:
            for v in self.tadj_list[u]:
                for t in self.tadj_list[u][v]:
                    if u not in t_vertex:
                        t_vertex[u] = {t}
                    else:
                        t_vertex[u].add(t)
            number_t_vertex+=len(t_vertex[u])

        return ttp, dangling_state, t_vertex,number_t_vertex

    def f(self, x):
        return 1 / x

    def core_decompisition(self):
        deg, core_number, core_renumber = {}, {}, {}
        max_core = 0
        myMinHeap = MinHeap([])
        n = len(self.tadj_list)
        n_core = 0
        for u in self.tadj_list:
            deg[u] = len(self.tadj_list[u])
            myMinHeap.insert([u, deg[u]])
        starttime = time.time()
        while n_core != n:
            x = myMinHeap.remove()
            if x[1] > max_core:
                max_core = x[1]
            core_number[x[0]] = max_core
            n_core += 1
            if core_number[x[0]] in core_renumber:
                core_renumber[core_number[x[0]]].add(x[0])
            else:
                core_renumber[core_number[x[0]]] = {x[0]}
            for u in self.tadj_list[x[0]]:
                if u not in core_number:
                    deg[u] = deg[u] - 1
                    myMinHeap.decrease_key(u, deg[u])
        endtime = time.time()
        # print("core_decomposition_time(s)" + str(endtime - starttime))
        return core_number, core_renumber

    def maintain_connected(self, temp, seed):
        q, visited = [seed], {seed}
        while q:
            v = q.pop()
            for u in self.tadj_list[v]:
                if u in temp and u not in visited:
                    q.append(u)
                    visited.add(u)
        return visited



    def Compute_tppr(self, alpha, seed):
        starttime = time.time()

        tppr, D = {}, defaultdict(lambda: defaultdict(int))

        e_out_seed = 0
        for u in self.tadj_list[seed]:
            e_out_seed += len(self.tadj_list[seed][u])
        for (u, v, t) in self.edge_stream:
            for t1 in D[u]:
                if (v,t) in self.ttp[(u,t1)]:
                    D[v][t] += (1 - alpha) * D[u][t1] * self.ttp[(u, t1)][(v, t)]
            if u == seed:
                D[v][t] = D[v][t] + (alpha) / e_out_seed

        for v in D:
            tppr[v] = 0
            for t in D[v]:
                if (v, t) in self.dangling_state:
                    D[v][t] = D[v][t] / (alpha)
                tppr[v] = tppr[v] + D[v][t]
        endtime = time.time()
        return tppr, endtime - starttime


    def qtcs_baseline(self, alpha, seed, k):
        starttime = time.time()
        q = []
        D = set()
        deg = {}
        for node_id in self.tadj_list:
            deg[node_id] = len(self.tadj_list[node_id])
            if deg[node_id] < k:
                q.append(node_id)
        while q:
            v = q.pop()
            D.add(v)
            for w in self.tadj_list[v]:
                if deg[w] >= k:
                    deg[w] = deg[w] - 1
                    if deg[w] < k:
                        q.append(w)
        kcore = set(self.tadj_list.keys()) - D
        if seed not in kcore:
            print("noanswer")
            return set(),0
        temp = self.maintain_connected(kcore, seed)
        tppr,time1 = self.Compute_tppr(alpha, seed)
        mymin_heap = MinHeap([])
        for u in temp:
            mymin_heap.insert([u, tppr[u]])
        D, best_indx = [], 0
        while mymin_heap.heap:
            u = mymin_heap.remove()[0]
            if u == seed:
                break
            if deg[u] < k:
                continue
            q = [u]
            while q:
                u = q.pop()
                D.append(u)
                for w in self.tadj_list[u]:
                    if deg[w] >= k:
                        deg[w] = deg[w] - 1
                        if deg[w] < k:
                            q.append(w)
                            if w == seed:
                                q = []
                                mymin_heap = MinHeap([])
                                break

            if mymin_heap.heap:
                best_indx = len(D)
        R = temp - set(D[:best_indx])
        result = self.maintain_connected(R, seed)
        endtime = time.time()
        return result, endtime - starttime


    def EGR(self, alpha, seed):
        starttime = time.time()

        tppr,time_tppr = self.Compute_tppr(alpha, seed)
        rho = {}
        mymin_heap = MinHeap([])
        for u in self.tadj_list:
            rho[u] = 0
            for v in self.tadj_list[u]:
                rho[u] = rho[u] + tppr[v]
            mymin_heap.insert([u, rho[u]])
        temp = set(self.tadj_list)
        opt = (mymin_heap.peek())[1]
        D, best_index = [], 0
        while temp:
            while (mymin_heap.peek())[1] <= opt:
                u = mymin_heap.remove()[0]
                temp.remove(u)
                D.append(u)
                if str(u) == str(seed):
                    temp = set()
                    break
                for v in self.tadj_list[u]:
                    if v in temp:
                        rho[v] = rho[v] - tppr[u]
                        mymin_heap.decrease_key(v, rho[v])
            if temp:
                opt = (mymin_heap.peek())[1]
                best_index = len(D)
        R = set(self.tadj_list) - set(D[:best_index])
        result = self.maintain_connected(R, seed)
        endtime = time.time()
        return result,time_tppr,endtime - starttime




    def propagation(self,v,t,alpha,C):
        if (v, t) not in self.dangling_state:
            for (w, t1) in self.ttp[(v, t)]:
                if (w, t1) not in self.r:
                    self.r[(w, t1)] = 0
                self.r[(w, t1)] = self.r[(w, t1)] + (1 - alpha) * self.r[(v, t)] * self.ttp[(v, t)][(w, t1)]
            if v not in self.tppr:
                self.tppr[v] = 0
            self.tppr[v] = self.tppr[v] + alpha * self.r[(v, t)]

            #maintain some heap structures
            if v in self.Q.heap_dict:
                self.sum_Q += alpha * self.r[(v, t)]
            if v in C:
                for w in self.tadj_list[v]:
                    if w in C:
                        self.inter_rho[w] = self.inter_rho[w] + alpha * self.r[(v, t)]
                        self.inter_rho_min_heap.increase_key(w, self.inter_rho[w])
                    if w in self.Q.heap_dict:
                        self.Q_with_C[w] = self.Q_with_C[w] + alpha * self.r[(v, t)]
                        self.Q.increase_key(w, self.Q_with_C[w])
            self.r_sum = self.r_sum - alpha * self.r[(v, t)]
            # maintain some heap structures

            self.r[(v, t)] = 0

        if (v, t) in self.dangling_state:
            if v not in self.tppr:
                self.tppr[v] = 0
            self.tppr[v] = self.tppr[v] + self.r[(v, t)]

            #maintain some heap structures
            if v in self.Q.heap_dict:
                self.sum_Q += self.r[(v, t)]
            if v in C:
                for w in self.tadj_list[v]:
                    if w in C:
                        self.inter_rho[w] = self.inter_rho[w] +self.r[(v, t)]
                        self.inter_rho_min_heap.increase_key(w, self.inter_rho[w])
                    if w in self.Q.heap_dict:
                        self.Q_with_C[w] = self.Q_with_C[w] + self.r[(v, t)]
                        self.Q.increase_key(w, self.Q_with_C[w])
            self.r_sum = self.r_sum -  self.r[(v, t)]
            # maintain some heap structures

            self.r[(v, t)] = 0


    def ALS(self, alpha, seed):
        starttime = time.time()
        self.r = {}
        e_out_seed = 0
        for v in self.tadj_list[seed]:
            e_out_seed = e_out_seed + len(self.tadj_list[seed][v])
        for v in self.tadj_list[seed]:
            for t in self.tadj_list[seed][v]:
                self.r[(v, t)] = 1 / e_out_seed

        self.inter_rho, self.inter_rho_min_heap = {}, MinHeap([])
        self.tppr = {}
        self.Q = MaxHeap([])
        self.Q.insert([seed, 0])
        self.Q_with_C = {}

        best, C, D = 0, set(), {seed}

        self.r_sum = 1
        unqualified = set()
        self.sum_Q = 0

        while self.Q.heap:
            u = self.Q.remove()[0]
            if u in self.tppr:
                self.sum_Q -= self.tppr[u]

            for v in self.tadj_list[u]:
                for t in self.t_vertex[v]:
                    if (v, t) in self.r and self.r[(v, t)] >1 / self.number_t_vertex:
                        self.propagation(v,t,alpha,C)

            #maintain some heap structures
            self.inter_rho[u] = 0
            for w in self.tadj_list[u]:
                if w in C:
                    if w in self.tppr:
                        self.inter_rho[u] = self.inter_rho[u] + self.tppr[w]
                    if u in self.tppr:
                        self.inter_rho[w] = self.inter_rho[w] + self.tppr[u]
                        self.inter_rho_min_heap.increase_key(w, self.inter_rho[w])
                if w in self.Q.heap_dict and u in self.tppr:
                    self.Q_with_C[w] = self.Q_with_C[w] + self.tppr[u]
                    self.Q.increase_key(w, self.Q_with_C[w])
            self.inter_rho_min_heap.insert([u, self.inter_rho[u]])
            # maintain some heap structures

            C.add(u)
            if self.inter_rho_min_heap.peek()[1] > best:
                best = self.inter_rho_min_heap.peek()[1]

            if self.r_sum<0: #self.r_sum may be negative because of the accuracy of the computer
                self.r_sum=0

            for v in self.tadj_list[u]:
                if v not in D:
                    D.add(v)
                    xv = self.r_sum
                    for w in self.tadj_list[v]:
                        if w not in unqualified and w in self.tppr:
                            xv = xv + self.tppr[w]
                    if xv >= best:
                        #maintain some heap structures
                        if v not in self.tppr:
                            self.tppr[v] = 0
                        self.sum_Q += self.tppr[v]
                        self.Q_with_C[v] = 0
                        for w in self.tadj_list[v]:
                            if w in C and w in self.tppr:
                                self.Q_with_C[v] = self.Q_with_C[v] + self.tppr[w]
                        # maintain some heap structures

                        self.Q.insert([v, self.Q_with_C[v]])
                    else:
                        unqualified.add(v)
            # min_inter_C = float('inf')
            # for v in C:
            #     inter_C = 0
            #     for w in self.tadj_list[v]:
            #         if w in C:
            #             inter_C += self.tppr[w]
            #     if inter_C < min_inter_C:
            #         min_inter_C = inter_C
            #
            # if format(min_inter_C, ".6f") != format(self.inter_rho_min_heap.peek()[1], ".6f"):
            #     print(min_inter_C)
            #     print(self.inter_rho_min_heap.peek()[1])
            #     print("wrong.....................")
            # Verify the correctness of the expanding algorithm and heap structure maintenance

            if self.sum_Q + self.r_sum < best:
                # print("Q prune is effective")
                # print("Q(len)"+str(len(self.Q.heap_dict)))
                for v in self.Q.heap_dict:
                    C.add(v)
                break

        endtime = time.time()
        expanding_time= endtime - starttime

        #Verify the correctness of the expanding algorithm and heap structure maintenance
        # print("self.r_sum" + str(self.r_sum))
        # print("rsum" + str(sum(self.r.values())))
        # vaiable = sum(self.tppr.values())+ self.r_sum
        # print("vaiable" + str(vaiable))
        # sum1 = 0
        # for u in self.Q.heap_dict:
        #     sum1 += self.tppr[u]
        # if format(sum1, ".8f") != format(self.sum_Q, ".8f"):
        #     print("QQQQQQQQQQQQwrong")
        #     print(sum1)
        #     print(self.sum_Q)
        starttime = time.time()
        R, rho_hat, flag = C.copy(), {}, True
        max_rho, min_rho = 0, float('inf')
        for u in C:
            rho_hat[u] = 0
            if u not in self.tppr:
                self.tppr[u] = 0
            for v in self.tadj_list[u]:
                if v in C  and v in self.tppr:
                    rho_hat[u] += self.tppr[v]
            if rho_hat[u] > max_rho:
                max_rho = rho_hat[u]
            if rho_hat[u] < min_rho and rho_hat[u] != 0:
                min_rho = rho_hat[u]
        temp = self.r_sum + max_rho
        epsion = temp / min_rho
        lambda_1 = epsion
        while flag:
            D, Q = set(), []
            for u in R:
                if epsion * rho_hat[u] <= temp:
                    Q.append(u)
                    if u == seed:
                        flag = False
                        Q = []
                        break
            while Q:
                u = Q.pop()
                D.add(u)
                for v in self.tadj_list[u]:
                    if v in R and v not in D:
                        rho_hat[v] = rho_hat[v] - self.tppr[u]
                        if epsion * rho_hat[v] <= temp:
                            Q.append(v)
                            if v == seed:
                                flag = False
                                Q = []
                                break
            if flag:
                lambda_1 = epsion
                R = R - D
                epsion = epsion / 2
        result = self.maintain_connected(R, seed)
        endtime = time.time()
        reducing_time= endtime - starttime
        return C,expanding_time,reducing_time,result,lambda_1


    def metric(self,S):
        temporal_edge_S=0
        time_S=set()
        for u in S:
            for v in self.tadj_list[u]:
                if v in S:
                    for t in self.tadj_list[u][v]:
                        time_S.add(t)
                        temporal_edge_S+=1
        TD=temporal_edge_S/(len(S)*(len(S)-1)*len(time_S))

        temporal_cut_S=0
        temporal_vol_S=0
        for u in S:
            for v in self.tadj_list[u]:
                if v not in S:
                    temporal_cut_S+=len(self.tadj_list[u][v])
            for w in self.tadj_list[u]:
                temporal_vol_S+=len(self.tadj_list[u][w])

        if temporal_vol_S>len(self.edge_stream)-temporal_vol_S:
            temporal_vol_S=len(self.edge_stream)-temporal_vol_S
        if temporal_vol_S==0:
            TC=1
        else:
            TC=temporal_cut_S/temporal_vol_S

        return TD, TC

    def t_vertex_sort(self): #temporal occurrence rank
        number_t_vertex=[]
        for u in self.tadj_list:
            number_t_vertex.append((u,len(self.t_vertex[u])))
        number_t_vertex.sort(key=lambda x:x[1])
        sorted_vertex=[] #sort vertex by increasing len(self.t_vertex[u]))
        for pair in number_t_vertex:
            sorted_vertex.append(pair[0])
        sorted_vertex_percent={}
        step=len(self.tadj_list)/10
        for i in range(1,11):
            sorted_vertex_percent[i]=[]
            for j in range(int((i-1)*step),int(i*step)):
                sorted_vertex_percent[i].append(sorted_vertex[j])

        return sorted_vertex_percent


    def inter_min_rho(self,H,alpha,seed): #for testing precision,recall and F1
        tppr,time_tppr = self.Compute_tppr(alpha, seed)
        min_inter_rho_H=float('inf')
        for u in H:
            inter_H= 0
            for v in self.tadj_list[u]:
                if v in H:
                    inter_H += tppr[v]
            if inter_H<min_inter_rho_H:
                min_inter_rho_H=inter_H

        return min_inter_rho_H

    def temporal_subgraph(self, S): #for case study
        interaction = {}
        for u in S:
            interaction[u] = {}
            for v in self.tadj_list[u]:
                if v in S:
                    interaction[u][v] = set()
                    for t in self.tadj_list[u][v]:
                        interaction[u][v].add(t)
        return interaction

if __name__ == '__main__':
    dataset = sys.argv[1]
    G_qtcs = Graph(dataset)
    alpha=0.2
    number = 0

    while number < 5:
        seed = int(choice(list(G_qtcs.tadj_list)))
        t_set=set()
        for u in G_qtcs.tadj_list[seed]:
            for t in G_qtcs.tadj_list[seed][u]:
                t_set.add(t)
        if len(t_set) < 3:
            continue
        number += 1
        print("seed"+str(seed))
        result,time_tppr,t_egr=G_qtcs.EGR(alpha, seed)
        C,expanding_time,reducing_time,result_11,lambda_1=G_qtcs.ALS(alpha, seed)
        for u in result:  #verfied the correct of expanding stage
            if u not in C:
                print("wrong!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("time_tppr(s)"+str(time_tppr))
        print("egr_time(s)"+str(t_egr))
        print("time_expanding(s)"+str(expanding_time))
        print("time_reducing(s)"+str(reducing_time))





