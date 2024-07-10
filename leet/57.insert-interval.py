#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 2 pts
        # find the right place to insert or create a new interval
        # 1. fits in interval or 2. starts new one
        # merge intervals until you find the right interval to stop at or extend.
        # can: 1. stop where an existing interval stops, 2. overlap with one. 3. extend an existing one
        #
        # eg. [1,3],[6,7],[8,10],[12,16]], newInterval = [4,8]
        if len(intervals) == 0:
            return [newInterval]

        ins = 0
        new_intervals = []
        while ins < len(intervals):
            if newInterval[0] < intervals[ins][0]:
                # the right one is i-1
                break
            new_intervals.append(intervals[ins])
            ins+=1
        
        if new_intervals[-1][1] >= newInterval[0]:
            # fits, naively set interval
            new_intervals[-1][1] = max(newInterval[1], new_intervals[-1][1])
        else:
            new_intervals.append(newInterval)
        
        print(ins)
        # flatten the intervals
        # look at the back one and see if it should fold into the next one
        while ins < len(intervals):
            if new_intervals[-1][1] < intervals[ins][0]:
                break
            elif new_intervals[-1][1] <= intervals[ins][1]:
                new_intervals[-1][1] = intervals[ins][1]
            ins+=1

        new_intervals.extend(intervals[ins:])


        return new_intervals
            
            



        
        
# @lc code=end

