# given a set of intervals [start, end], find the maximum overlap of intervals
# return  the two pairs of intervals that overlap the most
# the start and end of the intervals don't overlap if they're the same value
# also if the end value of the second pair is less than the end of the first pair, they don't overlap
# e.g. [[10, 30], [2, 10], [5, 5], [3, 20]]
# this should return [[2, 10], [3, 20]]
# the biggest overlap is 10-3 = 7
