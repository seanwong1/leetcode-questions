# Leetcode 1103

from typing import List

class Solution:
  def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    result = [0] * num_people
    candy = 1

    while candies > 0:
      if candies > candy:
        result[(candy - 1) % num_people] += candy
        candies -= candy
        candy += 1
      else:
        result[(candy - 1) % num_people] += candies
        candies -= candies

    return result

    # level = 1
    # result = [0] * num_people

    # while ((num_people * level) * ((num_people * level) + 1) / 2) <= candies:
    #   level += 1
    # level -= 2

    # for i in range(num_people):
    #   candy = int((((level * (level + 1)) / 2) * num_people) + ((level + 1) * (i + 1)))
    #   result[i] = candy
    #   candies -= candy

    # i = 0
    # level += 1
    # while candies > 0:
    #   if not level:
    #     candy = int((((level * (level + 1)) / 2) * num_people) + ((level + 1) * (i + 1)))
    #   else:
    #     candy = int((((level * (level + 1)) / 2) * num_people) + ((level) * (i + 1)))
    #   if candies > candy:
    #     result[i] += candy
    #     candies -= candy
    #   else:
    #     result[i] += candies
    #     candies -= candies
    #   i += 1

    # return result