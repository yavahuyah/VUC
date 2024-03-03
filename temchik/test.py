valuesInd = []

value = "Взводы / СЗ-1523 /"
j = 0
for i in range(len(value)):
    if value[i] == ' / ':
        valuesInd.append([value[j:i], j, i])
        j = i + 1

print(valuesInd)
