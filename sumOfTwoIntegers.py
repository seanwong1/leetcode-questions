# Leetcode 371

def getSum(a, b):
  def add(a, b):
    while b:
      carry = a & b
      a = a ^ b
      b = carry * 2
    return a

  if a * b < 0:
    if add(~a, 1) == b:
      return 0
    if add(~a, 1) < b:
      return add(~add(add(~b, 1), add(~a, 1)), 1)
    if a > 0:
      return add(b, a)

  return add(a, b)