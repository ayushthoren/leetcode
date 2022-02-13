class Solution:
    def findWords(self, words: List[str]) -> List[str]:
      #List to hold the characters in each row of the American keyboard
      rows=["qwertyuiop", "asdfghjkl", "zxcvbnm"]
      #List to hold all of the words whose characters can all be found in one row
      oneRow=[]
      #Variable to see if a word can be put in the oneRow array
      isValid=True
      #For each word in the array...
      for i in words:
        #For each row in the keyboard...
        for j in rows:
          #For each letter in the current word...
          for k in i.lower():
            #If the letter isn't in the current row, disqualify the word
            if k not in j: isValid = False
          #If toe letters passed the tests, add the word to the list
          if isValid: oneRow.append(i)
          #Reset the isValid variable for the next row
          isValid = True
      return oneRow
