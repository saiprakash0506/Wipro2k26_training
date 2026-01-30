set1={1,2,3,4,5,6,6}
print(set1) 
print(2 in set1)
print(len(set1))

set2=set()
print(type(set2))
print(len(set2))


set1=set("abcdefghi")
set2=set('defghijkl')

print(set2-set1) #removes items from first set to second set
print(set1-set2)
print(set1|set2) #union
print(set1&set2) #intersection
print(set1^set2) #prints uncommom things


a=set('python')
b=set("telusko")
print(a&b)

