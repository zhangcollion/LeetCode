import numpy as np
class Solution:
    def get_answer(self, input):
        n,m,k = input[0]
        edge = np.array(input[1:m+1],dtype=int)-1
        node_f = np.array(input[m+1:])
        node_f = node_f[:,1:]
        data_map = {"1":[0,0,1],"2":[0,1,0],"3":[1,0,0]}
        add_f = np.zeros((node_f.shape[0],3))
        for idx, data in enumerate(node_f):
            add_f[idx,:] = data_map[data[0]]
        node_f = np.concatenate((add_f,node_f),axis=1)
        for i in range(n):
            near_node =  edge[edge[:,0] == i][:,1]
            if near_node.any():
                node_f[i,3] = round(node_f[near_node,:][:,3].astype(int).mean(),2)
                node_f[i,4] = round(node_f[near_node,:][:,4].astype(int).mean(),2)
                node_f[i,5] = round(node_f[near_node,:][:,5].astype(int).mean(),2)
        ref = node_f[node_f[:,-1]=='unknown']

        dist  = []
        for tmp_data in node_f:
            if tmp_data[-1] =='unknown':
                dist.append(10000)
            else:
                distance = sum(abs(tmp_data[:-1].astype(float) - ref[0][:-1].astype(float)))
                dist.append(distance)
        node_f = np.concatenate((node_f, np.array(dist)[:,None].astype(float)),axis=1)
        node_f = node_f.tolist()
        for i, data in enumerate(node_f):
            data.insert( 0, i+1)
        sort_distance = sorted(node_f, key=lambda x:(x[-1]))[:k]
        label_map = {"RSG":0, "ASG":1,"CSG":2}
        label_turn = {0:"RSG", 1:"ASG",2:"CSG"}
        label_cnt = {"RSG": 0, "ASG": 0, "CSG": 0}
        idx = []
        for data in sort_distance:
            label_cnt[data[-2]] +=1
            idx.append(data[-2])
            data[-2] = label_map[data[-2]]
        for i, data in enumerate(sort_distance):
            data.append(label_cnt[idx[i]])
        sort_distance = sorted(sort_distance, key=lambda x: (-x[-1],x[-2] ))[0]
        idx = int(sort_distance[0])-1
        label = label_turn[sort_distance[-3]]
        return idx, label


if __name__ == "__main__":
    # input = [[1,1,0,1,1,0],[1,0,0,1,1,1],[0,1,0,0,1,1],
    #          [0,1,0,1,0,0],[0,1,0,0,0,0],[0,0,0,1,0,0]]
    input = [[7,6,5],[1,2],[1,3],[1,4],[3,6], [3,7],[4,5],[1, 1, 5, 8, 10, 3,"RSG"], [2, 3, 12, 10, 11, 7,"CSG"],
             [3, 2, 4, 1, 6, 10, "unknown"],[4, 2, 4, 1, 6,10,"ASG"],[5, 3, 12, 10, 11, 7,"CSG"],
             [6, 3, 12, 10, 11, 7,"CSG"],[7, 3, 12, 10, 11, 7,"CSG"]]
    print(Solution().get_answer(input))