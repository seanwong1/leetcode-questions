# Leetcode 659

def encode(strings):
  encoded = ""

  for string in strings:
    encoded += '$' + str(len(string)) + string

  return encoded

def decode(string):
  decoded = []
  index = 0
  delimiter = False

  while index < len(string):
    currentString = index
    if string[currentString] == '$':
      currentString += 1
      index += 1
      delimiter = True
      continue
    elif delimiter:
      decoded.append(string[currentString + 1 : currentString + int(string[index]) + 1])
      index += int(string[index]) + 1
      delimiter = False

  return decoded