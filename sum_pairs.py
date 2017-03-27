def sum_pairs(ints, s):
    for i in range(0,len(ints)):
        for j in range(i+1, len(ints)):
            if s == ints[i]+ints[j]:
                return [ints[i],ints[j]]

l1= [1, 4, 8, 7, 3, 15]
l5= [10, 5, 2, 3, 7, 5]
print(sum_pairs(l1, 10))
print(sum_pairs(l5, 10))