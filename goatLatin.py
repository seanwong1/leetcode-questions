# Leetcode 824

class Solution:
  def toGoatLatin(self, sentence: str) -> str:
    result = sentence.split(' ')

    for i in range(len(result)):
      if result[i][0] in 'aeiouAEIOU':
        result[i] += 'ma'
      else:
        result[i] = result[i][1:] + result[i][0] + 'ma'

      result[i] += ('a' * (i + 1))

    return ' '.join(result)