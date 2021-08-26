my_list = [1, 2, 3]
len(my_list)  # return 3

print(my_list[1:2])  # get 2 (second element from array)

new_list = ['1', '2', '3']
new_list[0] = 'lorem'
print(new_list)
# new_list.append('2') to end of list .pop() remove last but can .pop(some index) default .pop(-1)

# dicionaries
my_dic = {'key1': 'value1', 'key2': 'value2'}
print(my_dic['key1'])
my_dic.keys()  # 'key1 key2
my_dic.values()  # value1 value2

# tuples
my_tuple = (1, 2, 3)  # can mutable


# set place where can hold data
my_set = set()  # values must by unique
my_set.add(1)
print(my_set)
