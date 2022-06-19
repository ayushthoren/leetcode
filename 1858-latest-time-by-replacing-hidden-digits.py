class Solution:
    def maximumTime(self, time: str) -> str:
      #Split the time into hours and minutes
      time=time.split(":")
      #Make a string to hold the maxed time
      new=""
      for i in range(len(time)):
        #Add the colon if needed
        if i==1: new+=":"
        for j in range(len(time[i])):
          #If there is a missing number at this index...
          if time[i][j]=="?":
            #If it is in the hours section...
            if i==0:
              #If it is the first digit of the hour...
              if j==0:
                #If possible, add 2, otherwise add 3
                if time[i][j+1]=="?" or int(time[i][j+1])<4: new+="2"
                else: new+="1"
              #If it is the last digit of the hour...
              else:
                #If the first digit is 2, add 3, otherwise go up to 9
                if time[i][j-1]=="?" or int(time[i][j-1])>1: new+="3"
                else: new+="9"
            #If it is in the minutes section...
            else:
              #If it is the first digit of the minute...
              #Add 5, there is no other option
              if j==0: new+="5"
              #If it is the second digit of the minute...
                #Add 9, there is no other option
              else: new+="9"
          #If the digit isn't missing, add it to the new time
          else: new+=time[i][j]
      return new
