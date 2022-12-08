with open('elf8.txt') as reader:
  lines = reader.readlines()

for i in range(len(lines)):
  lines[i] = lines[i].strip()

#we ignore the first annd last lines
#we also ignore the first and last digit of the lines in  between
sum = 0 
for i in range(len(lines)):
  if i == 0:
    #first row 
    sum += len(lines[i])
  elif i == len(lines) -1:
    #last row
    sum += len(lines[i])
  else:
    #in between
    sum += 2

for i in range(1, len(lines)-1):
  #each line
  for j in range(1,len(lines[i])-1):
    #each character in the line
    #print('current char', lines[i][j])
    visible = False
    #check cases
    #1.left
    for k in range(0, j):
      if int(lines[i][k]) >= int(lines[i][j]):
        #if a character before it is bigger, not visible
        break
      elif k == j-1 :
        sum+=1
        visible = True
      else:
        continue
      #if it doesn't break, then sum increases
   
    if visible == False:
      #2right
      for k in range(j+1, len(lines[i])):
        if int(lines[i][k]) >= int(lines[i][j]):
          break
        elif k == len(lines[i]) -1:
          sum+=1
          visible = True
        else:
          continue
        
    if visible == False:
      #3up
      for k in range(0, i):
        if(int(lines[k][j]) >= int(lines[i][j])):
          break
        elif k == i -1:
          sum+=1
          visible = True
        else:
          continue
  
    if visible == False:
      #4down
      for k in range(i+1, len(lines)):
        if(int(lines[k][j]) >= int(lines[i][j])):
          break
        elif k == len(lines) -1:
          sum+=1
          visible = True
        else:
          continue

print(sum)