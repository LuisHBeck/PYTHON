from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(*zip(l1,l2))
print(*zip_longest(l1,l2, fillvalue="sem cidade"))


l3 = [1,2,3,4,5,6,7]
l4 = [2,3,4,5,6]

result = [sum(i) for i in zip_longest(l3, l4, fillvalue=0)]
print(result)
