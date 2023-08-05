# Leetcode 424

def characterReplacement(string, replacements):
  counts = {}
  counter = 0
  left = 0

  for right in range(len(string)):
    if string[right] in counts:
      counts[string[right]] += 1
    else:
      counts[string[right]] = 1

    counter = counter if counter >= counts[string[right]] else counts[string[right]]

    if (right - left + 1) - counter > replacements:
      counts[string[left]] -= 1
      left += 1

  return right - left + 1