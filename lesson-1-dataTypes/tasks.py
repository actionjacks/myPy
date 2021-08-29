import math
1
'2'
[1, 2, 3]
(1, 1, 1)
{'ja': 1}
print(type(3+1.5+4))  # float

print(math.sqrt(4))

s = 'hello'
print(s[1])
print(s[-4])

mylist = []
mylist.append(0)
mylist.append(0)
mylist.append(0)
# or [0]*3
print(mylist)

list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
# print(list3)


list4 = [5, 3, 4, 6, 1]
# sorted return sorted list
sorted(list4)  # !!!!!!!!!

list4.sort()
# print(list4)

#d = {'simple_key': 'hello'}
# print(d['simple_key'])
#d = {'k1':{'k2':'hello'}}
# print(d['k1']['k2'])
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1])

x = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(x['k1'][2]['k2'][1]['tough'][2])

newset = set()
list15 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
list15.sort()
newset.update(list15)
print(newset)

print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(3.0 == 3)
print(4**0.5 != 2)

l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
print(l_one[2][0] >= l_two[2]['k1'])
