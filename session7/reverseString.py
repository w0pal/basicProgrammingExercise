original_string = str(input('input your name! : '))

reversed_string = ''

for i in range(len(original_string) - 1, -1, -1):
  reversed_string += original_string[i]

print("Original String:", original_string)
print("Reversed String:", reversed_string)