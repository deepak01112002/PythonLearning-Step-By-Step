#read Write


def ReadWrite(input,output):
  with open(input,'r') as file:
    text = file.read()
  words = text.split()
  word_count = len(words)

  with open(output , 'w') as file:
    file.write(f"Number of words : {word_count}")

input = 'input.txt'
output = 'output.txt'

ReadWrite(input,output)