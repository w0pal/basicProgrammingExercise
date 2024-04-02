list = [1, 2, 3, 4, 2, 3, 5, 6, 1]

listNew = []
for i in list:
    if i not in listNew:
        listNew.append(i)

print('Default List: ', list)
print('Removed Duplicate List: ', listNew)