#conjuntos

set0 = {1,2,3,2,1,12,12,12,12,1}
set1 = set([1,2,3,1,2,1,4,0,1,4])
set2 = set('abacaxi')
set1.add(13)

print(set0)
print(set1)
print(set2)

print(set0.intersection(set1))
print(set0.union(set1))
print(set0.difference(set1))
print(set0.symmetric_difference(set1))
