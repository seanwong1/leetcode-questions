# Leetcode 57

def insert(intervals, newInterval):
  result = []

  for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]:
      result.append(newInterval)
      return result + intervals[i:]
    elif newInterval[0] > intervals[i][1]:
      result.append(intervals[i])
    else:
      newInterval[0] = newInterval[0] if newInterval[0] < intervals[i][0] else intervals[i][0]
      newInterval[1] = newInterval[1] if newInterval[1] > intervals[i][1] else intervals[i][1]

  result.append(newInterval)

  return result