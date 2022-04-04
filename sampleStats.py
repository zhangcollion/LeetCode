from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        if sum(count) % 2 == 0:
            median_data = [sum(count) / 2 , sum(count) / 2+1]
        else:
            median_data = [int(sum(count) / 2), int(sum(count) / 2)]

        min_index = -1
        sum_data = 0
        count_data = 0
        median_sum = []
        max_index = 0
        for i in range(0, len(count)):
            if count[i] != 0:
                if -1 == min_index:
                    min_index = i
                max_data = i
                count_data += count[i]
                if count_data >= median_data[0]:
                    if len(median_sum) < 2:
                        if count_data >= median_data[1]:
                            if len(median_sum) == 1:
                                median_sum.append(i)
                            else:
                                median_sum.append(i)
                                median_sum.append(i)
                        elif count_data >= median_data[0] and count_data < median_data[1]:
                            median_sum.append(i)
                        else:
                            median_sum.append(i)
                            median_sum.append(i)

                if count[i] > max_index:
                    max_index = count[i]
                    flagv = i
                sum_data += i * count[i]
        result = [min_index, max_data, round(sum_data / count_data, 5), float(sum(median_sum) / 2), flagv]
        return result


if __name__=="__main__":
    count = [0,1,3,4,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    r = Soluti.sampleStats(ssssssssss)
    r = Solution().sampleStats(count)
    print(r)
