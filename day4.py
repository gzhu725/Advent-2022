with open('elf4.txt') as reader:
  lines = reader.readlines()


for i in range(len(lines)):
  lines[i] = lines[i].strip('\n')

sum = 0
for i in range(len(lines)):
  pair = lines[i].split(',')
  #one single pair like ['51-88', '52-87']
  first = pair[0].split('-')
  second = pair[1].split('-')
  # two pairs like ['51', '88'] AND ['52', '87']
  minfirst = int(first[0])
  maxfirst= int(first[1])
  minsecond = int(second[0])
  maxsecond= int(second[1]) 

  #part 1
  '''if(set((range(minfirst,maxfirst+1))).issubset(range(minsecond,maxsecond+1)) or set((range(minsecond,maxsecond+1))).issubset(range(minfirst,maxfirst+1))):
    sum += 1'''
  #part2

  if(minfirst <= maxsecond) and (maxfirst >= minsecond):
    sum += 1

print(sum)





print(sum)

'''
pair = lines[0].split(',')

first = pair[0].split('-')
second = pair[1].split('-')
#DO FOR ['51-88,52-57']

minfirst = int(first[0])
maxfirst= int(first[1])

minsecond = int(second[0])
maxsecond= int(second[1])

print(range(minfirst,maxfirst+ 1))
print(range(minsecond,maxsecond+ 1))

#51-88 and 52-87 INCLUDES SHOULD BE True

print(set((range(minfirst,maxfirst+1))).issubset(range(minsecond,maxsecond+1)))


print(set((range(minsecond,maxsecond+1))).issubset(range(minfirst,maxfirst+1)))


#MUST CHECK BOTH CASES

'''




