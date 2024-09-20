# Leetode 1880

class Solution:
  def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
    firstWord = list(firstWord)
    secondWord = list(secondWord)
    targetWord = list(targetWord)

    for index, letter in enumerate(firstWord):
      firstWord[index] = str(ord(letter) - 97)

    firstWord = int(''.join(firstWord))

    for index, letter in enumerate(secondWord):
      secondWord[index] = str(ord(letter) - 97)

    secondWord = int(''.join(secondWord))

    for index, letter in enumerate(targetWord):
      targetWord[index] = str(ord(letter) - 97)

    targetWord = int(''.join(targetWord))

    return firstWord + secondWord == targetWord