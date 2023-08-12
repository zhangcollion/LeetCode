import numpy as np
class Solution:
    def get_answer(self, input):
        ## 样本个数
        data = np.array(input)
        D = data.shape[0]
        K = 2
        ## 不同样本个数C0, C1,计算H(D)
        C_1 = np.count_nonzero(list(data[:,-1]))
        C_0 = D-C_1
        H_D = (-((C_0)/(D))*np.log2(((C_0)/(D)))) + (-((C_1)/(D))*np.log2(((C_1)/(D))))

        ans = 0
        idx = 0

        for i in range(data.shape[1]-1):
            tmp_data = data[:, [i, -1]]
            D_i = []
            D_0_cnt = []
            D_1_cnt = []
            HDA0 = 0
            HDA1 = 0
            D_i.append(sum(tmp_data[:,0] == 0))
            D_0 = tmp_data[(tmp_data[:,0] == 0) ]
            D_0_cnt.append(sum(D_0[:,1] == 0))
            D_0_cnt.append(len(D_0[:,1])-sum(D_0[:,1] == 0))
            D_i.append(len(tmp_data[:,0])-sum(tmp_data[:,0] == 0))
            D_1 = tmp_data[(tmp_data[:, 0] == 1)]
            D_1_cnt.append(sum(D_1[:, 1] == 0))
            D_1_cnt.append(len(D_1[:, 1]) - sum(D_1[:, 1] == 0))
            if D_i[0] != 0:
                if D_0_cnt[0]:
                    HDA0 = -(D_i[0] / D)*(D_0_cnt[0]/D_i[0])*np.log2(D_0_cnt[0]/D_i[0])
                if D_0_cnt[1]:
                    HDA0 += -(D_i[0] / D)*(D_0_cnt[1] / D_i[0]) * np.log2(D_0_cnt[1] / D_i[0])

            if D_i[1] != 0:
                if D_1_cnt[0]:
                    HDA1 = -(D_i[1] / D) * (
                                (D_1_cnt[0] / D_i[1]) * np.log2(D_1_cnt[0] / D_i[1]))
                if D_1_cnt[1]:
                    HDA1 += -(D_i[1] / D) *(D_1_cnt[1] / D_i[1]) * np.log2(
                        D_1_cnt[1] / D_i[1])

            tmp_ans = round(H_D-(HDA0+HDA1), 2)
            print(tmp_ans)
            if tmp_ans > ans:
                ans = tmp_ans
                idx = i


        return idx, ans






if __name__=="__main__":
    # input = [[1,1,0,1,1,0],[1,0,0,1,1,1],[0,1,0,0,1,1],
    #          [0,1,0,1,0,0],[0,1,0,0,0,0],[0,0,0,1,0,0]]
    input = [[1,1,0,1,0,1],[0,1,0,1,1,0],[0,1,0,0,0,0],
             [0,0,0,1,0,0]]
    print(Solution().get_answer(input))
