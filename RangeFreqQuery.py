class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.data = arr
        self.info = collections.defaultdict()

    def query(self, left: int, right: int, value: int) -> int:
        key = str(left) + "_" + str(right)+ "_" + str(value)
        if key in self.info.keys():
            return self.info[key] 
        else:
            tmp_data = self.data[left:right+1]
            tmp_dict = tmp_data.count(value)
            self.info[key] = tmp_dict
        return self.info[key] 
