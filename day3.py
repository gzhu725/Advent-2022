with open('elf3.txt') as reader:
  lines = reader.readlines()



for i in range(len(lines)):
  lines[i] = lines[i].strip()

sum = 0
for i in range(len(lines)):
  length = len(lines[i])
  first = lines[i][0:length/2]
  last = lines[i][length/2:]
  common = ''.join(set(first).intersection(last))
  letter = common[0]
  priority = ord(letter)
  if priority >= 97:
    priority = priority - 96
  else:
    priority = priority -38
  sum += priority

#part 2
groups = []
count = 0
singular = []
for i in range(len(lines)):
  singular.append(lines[i])
  count+=1
  if(count == 3):
    groups.append(singular)
    singular = []
    count = 0

secondsum = 0
for i in range(len(groups)):
  first = groups[i][0]
  second = groups[i][1]
  third = groups[i][2]
  common = ''.join(set(first).intersection(second).intersection(third))
  letter = common[0]
  priority = ord(letter)
  if priority >= 97:
    priority = priority - 96
  else:
    priority = priority -38
  secondsum += priority

print(secondsum)
  



