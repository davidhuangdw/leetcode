from unittest import TestCase
# https://leetcode.com/problems/gas-station


class GasStation(TestCase):
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
        i, n = 0, len(gas)
        while i < n:
            s = 0
            for j in range(i, i+n):
                s += gas[j%n] - cost[j%n]
                if s < 0: break
            if s >= 0: return i
            i = j+1         # because for any i<k<=j, sum[k,j] == sum[i,j]-sum[i,k-1] <= sum[i,j] < 0
        return -1

    # # two end:
    # def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
    #     st, ed, s = len(gas)-1, 0, gas[-1]-cost[-1]
    #     while st > ed:
    #         if s >= 0:
    #             s += gas[ed] - cost[ed]
    #             ed += 1
    #         else:
    #             # prove: when sum[st, ed)>=0 again, sum[st, k) >= 0 (st<k<ed)
    #             # 1. for st<k<=last_st, sum[k,ed)<0, so sum[st,k] = sum[st, ed) - sum[k+1, ed) >= sum[st,ed) >= 0
    #             # 2. for last_st<k<ed, sum[st,k] = sum[st, last_st] + sum[last_st, k) both >=0
    #             st -= 1
    #             s += gas[st] - cost[st]
    #     return st if s >= 0 else -1

    # # find max_suffix_sum
    # # if sum[i, n) is the max suffix sum, then we have for j<i<k, sum[j,i]<=0, sum[i,k]>=0,
    # #   then circular_sum[i,j] == total_sum - sum[j,i] >= total_sum >= 0
    # # this also proved that total_sum >= 0, then solution must exist
    # def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
    #     st, mx, s = -1, -1, 0
    #     for i in range(len(gas)-1, -1, -1):
    #         s += gas[i] - cost[i]
    #         if s > mx:
    #             mx, st = s, i
    #     return st if s >= 0 else -1

    def test1(self):
        self.assertEqual(3, self.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))

    def test2(self):
        self.assertEqual(-1, self.canCompleteCircuit([2,3,4], [3,4,3]))




