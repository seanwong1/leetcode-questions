# Leetcode 71

class Solution:
  def simplifyPath(self, path: str) -> str:
    result = []
    elements = path.split('/')

    for element in elements:
      if len(result) and element == '..':
        result.pop()
      elif element != '.' and element != '' and element != '..':
        result.append(element)

    result = '/'.join(result)
    return '/' + result