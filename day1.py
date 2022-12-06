with open('elf.txt') as reader:
  lines = reader.readlines()


for i in range(len(lines)):
  if lines[i] == '\n':
    continue
  else:
    lines[i].strip()
    lines[i] = int(lines[i])


#lines is modified to be of all '\n' or ints

elves = []

sum = 0 
for i in range(len(lines)):
  if(lines[i] == '\n'):
    elves.append(sum)
    sum = 0
  elif(i == len(lines) - 1):
    sum = sum + lines[i]
    elves.append(sum)
  else:
    sum = sum + lines[i]


elves = sorted(elves)
print(elves)

print(elves[-1] + elves[-2] + elves[-3])