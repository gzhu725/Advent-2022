#find the sum of the directories with a size of 100,000 or less

with open('elf7.txt') as reader:
  lines = reader.readlines()



for i in range(len(lines)):
  lines[i] = lines[i].strip()

all_chars = []

for i in range(len(lines)):
  chars = lines[i].split(' ')
  all_chars.append(chars)


sizes = []
class Node:
  def __init__(self, name):
    self.parent = None
    self.children = []
    self.size = 0
    self.name = name
  def findSum(self):
    for child in self.children:
      if not isinstance(child, int):
        #not a child, find the sum
        self.size += child.findSum()
      else:
        #is a child, then just add to the size
        self.size += child
    sizes.append(self.size)
    return self.size
  


root = Node("/")
cur = root
for command in all_chars:
  if command[0] == '$':
    if command[1] == "ls":
      #list
      continue
    if command[1] == "cd":
      #current directory
      if command[2] == "..":
        #get out of the current directory
        cur = cur.parent
      elif command[2] == "/":
        #we are back at the start
        cur = root
      else:
        #we go into another directory
        newDir = Node(command[2])
        newDir.parent = cur
        cur.children.append(newDir)
        cur = cur.children[-1]
  else:
    if command[0] != "dir":
      #it is a file
      cur.children.append(int(command[0]))
    
root.findSum()

sum = 0
for size in sizes:
  if size <=100000:
    sum += size

print(sum)



current = 70000000-root.size
needed = 30000000 - current
minDelete = float('inf')

for size in sizes:
  if size>=needed and size<minDelete:
    minDelete = size

print(minDelete)

#CODE PROVIDED BY JAMES CHEN, GITHUB USERNAME 1019JCHEN