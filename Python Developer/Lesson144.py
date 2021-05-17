from functools import reduce

my_list = [1,2,3]

print(reduce(lambda acc, item: acc+item, my_list))
print(my_list)