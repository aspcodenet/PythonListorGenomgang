
board = []
for i in range(8):
   row = [' ' for i in range(8)]
   board.append(row)

#bonderaden = board[1]
#bonderaden[3] = "B"
#board[1][3] = "B"
for column in range(0,8):
    board[1][column] = "B"
    board[6][column] = "B"


for row in board:
    print(row)





#Write a Python program to find the list of words that are longer
#  than n from a given list of words.
n = int(input("Ange längd"))
newList = []
listan = ['abc', 'xyz123', 'abc', 'aba', '1221']
for oneString in listan:
    if len(oneString) > n:
        newList.append(oneString)

n = int(input("Ange längd"))
listan = ['abc', 'xyz123', 'abc', 'aba', '1221']
newList = [oneString  for oneString in listan if len(oneString) > 5  ]



#Write a Python program to remove duplicates from a list
listan = ['abc', 'xyz', 'abc', 'aba', '1221']
listWithoutDuplicates = []
for oneString in listan:
    if oneString in listWithoutDuplicates:
        pass
    else:
        listWithoutDuplicates.append(oneString)

#Write a Python program to count the number of strings where 
# the string length is 2 or more and
#the first and last character are same from a given list of strings. Go to the editor
#ample List : ['abc', 'xyz', 'aba', '1221']
listan = ['abc', 'xyz', 'aba', '1221']
antal = 0
for oneString in listan:
    firstLetter = oneString[0]
    lastLetter = oneString[len(oneString)-1]
    if len(oneString) > 2  and firstLetter == lastLetter :
        antal = antal + 1
print(antal)        



#Write a Python program to get the largest number from a list
allaTal =  [12,44,567,23]
theLargestNumberIHaveFoundSoFar = allaTal[0]
for number in allaTal:
    if number > theLargestNumberIHaveFoundSoFar:
        theLargestNumberIHaveFoundSoFar = number
print(f"Största är {theLargestNumberIHaveFoundSoFar}")        

#Write a Python program to sum all the items in a list
allaTal =  [12,44,567,23]
summa = 0
for tal in allaTal:
    summa = summa + tal
print(f"Summa:{summa}")


#Skapa ett program där användaren får upp fyra frågor om att mata 
# in ett tal. Spara
#alla talen i en lista. Loopa igenom lista och ta fram det 
# tal som är störst. Skriv
#tillbaka resultatet på skärmen för användaren

allaTal =  []
for times in range(0,4):
    tal = input(f"Ange tal nummer{times+1}:")
    allaTal.append(tal)

theLargestNumberIHaveFoundSoFar = allaTal[0]
for number in allaTal:
    if number > theLargestNumberIHaveFoundSoFar:
        theLargestNumberIHaveFoundSoFar = number

print(f"Största är {theLargestNumberIHaveFoundSoFar}")





