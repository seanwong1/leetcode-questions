# Leetcode 1678

class Solution:
  def interpret(self, command: str) -> str:
    result = ''
    count = 0

    while count < len(command):
      if command[count] == 'G':
        result += 'G'
        count += 1
      elif command[count] == '(' and command[count + 1] == ')':
        result += 'o'
        count += 2
      else:
        result += 'al'
        count += 4

    return result