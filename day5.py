with open('elf5.txt') as reader:
  lines = reader.readlines()



for i in range(len(lines)):
  lines[i] = lines[i].strip()


#list bottom ----> top

singular_stack = []
whole_stack = []
for index in range(1,34, 4):
  for i in range(len(lines)):
    if(lines[i] == '1   2   3   4   5   6   7   8   9'):
      break
    else:
      potential_letter = lines[i][index]
      if(ord(potential_letter)>=65 and ord(potential_letter)<=90 or ord(potential_letter)>=97 and ord(potential_letter)<=122):
        #if it's a letter
        singular_stack.append(potential_letter)
  whole_stack.append(singular_stack)
  singular_stack = []





#whole_stack contains every stack you need

for i in range(len(whole_stack)):
  whole_stack[i].reverse()


#0bottom ----> 1 top
instructions = []
single_instruction = []
for i in range(10, len(lines)):
  words = lines[i].split(' ')
  single_instruction.append(int(words[1]))
  single_instruction.append(int(words[3]))
  single_instruction.append(int(words[5]))
  instructions.append(single_instruction)
  single_instruction = []

#instructions[i] = [3,2,1] 
#0, how many to move
#1, from where
#2, to where

for i in range(len(instructions)):
  current_instruction = instructions[i]
  for j in range(current_instruction[0]):
    whole_stack[current_instruction[2]-1].append(whole_stack[current_instruction[1]-1].pop())




for i in range(len(instructions)):
  current_instruction = instructions[i]
  sublist = []
  for j in range(current_instruction[0]):
    sublist.append(whole_stack[current_instruction[1]-1].pop())
    print(sublist)

print(whole_stack)

  

