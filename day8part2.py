with open('elf8.txt') as reader:
  lines = reader.readlines()

for i in range(len(lines)):
  lines[i] = lines[i].strip()

#we ignore the first annd last lines
#we also ignore the first and last digit of the lines in  between
sum = 0 
scores = []
for i in range(1, len(lines)-1):
  #each line
  for j in range(1,len(lines[i])-1):
    #each tree in the line
    left_score = 0
    right_score = 0
    up_score = 0
    down_score = 0
    
    
    visible = False
    #check cases
    #1.left
    for k in range(j-1, -1,-1):
      if int(lines[i][k]) >= int(lines[i][j]):
        #if a character before it is bigger
        left_score+=1
        break
      else:
        left_score += 1
        #else the score increases
  
    if visible == False:
      #2right
      for k in range(j+1, len(lines[i])):
        if int(lines[i][k]) >= int(lines[i][j]):
          right_score += 1
          break
        else:
          right_score += 1
        
    if visible == False:
      #3up
      for k in range(i-1, -1, -1):
        if(int(lines[k][j]) >= int(lines[i][j])):
          up_score += 1
          break
        else:
          up_score += 1
  
    if visible == False:
      #4down
      for k in range(i+1, len(lines)):
        if(int(lines[k][j]) >= int(lines[i][j])):
          down_score += 1
          break
        else:
          down_score += 1
    total_score = left_score * up_score * right_score * down_score
    scores.append(total_score)
  
#print(scores)
print(max(scores))