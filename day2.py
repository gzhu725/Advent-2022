with open('elf2.txt') as reader:
  lines = reader.readlines()


opponent = []
your = []

for i in range(len(lines)):
  opponent.append(lines[i][0])
  your.append(lines[i][2])


sum = 0
for i in range(len(opponent)):
  if(opponent[i] == 'A'):
    #opponent is rock
    if(your[i] == 'X'):
      #2: you must be scissors: 3 + 0 
      #you are rock: 1 + 3
      sum += 3
    elif(your[i] == 'Y'):
      #2: you must be rock: 1 + 3
      #you are paper: 2 + 6
      sum += 4
    elif(your[i] == 'Z'):
      #2: you must be paper 2 + 6
      #you are scissors: 3 + 0 
      sum += 8
  elif(opponent[i] == 'B'):
    #opponent is paper
    if(your[i] == 'X'):
      #2: you must be rock: 1+ 0
      #you are rock: 1 + 0
      sum += 1
    elif(your[i] == 'Y'):
      #you must be paper: 2+ 3
      #you are paper: 2 + 3
      sum += 5
    elif(your[i] == 'Z'):
      #you are scissors: 3 + 6 
      sum += 9
  elif(opponent[i] == 'C'):
    #opponent is scissors
    if(your[i] == 'X'):
      #you must be paper: 2+ 0
      #you are rock: 1 + 6
      sum += 2
    elif(your[i] == 'Y'):
      #you must be scissors
      #you are paper: 2 + 0
      sum += 6
    elif(your[i] == 'Z'):
      #you must be rock
      #you are scissors: 3 + 3 
      sum += 7
  
print(sum)


