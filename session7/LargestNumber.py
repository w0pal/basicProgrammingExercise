#initialize list
number = [10, 20, 5, 40, 30, 72, 34]

#initialize largest with first element
largest = number[0]
smallest = number[0]

#traverse the array
for i in number:
    if i>largest:
        largest = i
    
    if i<smallest:
        smallest = i

print('Largest Number : ', largest)
print('Smallest Number : ',smallest)