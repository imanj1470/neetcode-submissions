"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda m: m.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True
        
        #time: O(nlogn + n) with n being legnth of list due to sorting the list of intervals in ascending order, and adding n as having to loop through the list once, which reduces to O(nlogn). cost of each iteration is O(1) as its just performing an integer coompaarator, and time complexity of loop is loops * cost per iteration.

        #space complexity: o(1) as the addiotnal mem used is storing constants, which is not proportional to input.
            

