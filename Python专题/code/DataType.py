# names_class2 = ['张三', '李四', '王五', '赵六']
# names_class2.reverse()
# print(names_class2)

# x = [4, 6, 2, 1, 7, 9]
# x.sort(reverse=True)
# print(x)
# dic1={'name':'alex','age':36,'sex':'male'}  # 推荐使用
# dic2=dict((('name','alex'),))
#
# print(dic1)
# print(dic2)


# dic3 = {}
#
# dic3['name'] = 'alex'
# dic3['age'] = 18
# print(dic3)  # {'name': 'alex', 'age': 18}
#
# # 如果键已存在，不改变键原来的值
# a = dic3.setdefault('name', 'yuan')
# b = dic3.setdefault('ages', 22)
# print(a, b)
# print(dic3)


# dic3 = {'name': 'alex', 'age': 18}

# print(dic3['name'])  # alex
# print(dic3['names'])  # KeyError: 'names'

# print(dic3.get('age', False))
# print(dic3.get('ages', False))
#
# print(dic3.items())  # dict_items([('name', 'alex'), ('age', 18)])
# print(dic3.keys())  # dict_keys(['name', 'age'])
# print(dic3.values())  # dict_values(['alex', 18])
#
#
# print(list(dic3.values()))  # ['alex', 18]

# s = set('alvinyuan')
# # s1 = set('alvin')
# # print('v' in s)
# # print(s1 < s)

# s1 = {1, 2, 3}
# del s1
# print(s1)  # NameError: name 's1' is not defined


# original_lis = [1, 2, 5, 3, 1, 2]
# lis = list(set(original_lis))
# print(lis)
#
# lis.sort(key=lambda x: original_lis.index(x))
# print(lis)

import copy

lis_1 = [1, 2, ["a", "b", "c"], 4]
# lis_2 = lis_1
# lis_3 = copy.copy(lis_1)
# lis_4 = copy.deepcopy(lis_1)
#
# lis_1[0] = 1111
# lis_1[2][1] = "bbbbb"
#
# print(lis_1)
# print(lis_2)
# print(lis_3)
# print(lis_4)