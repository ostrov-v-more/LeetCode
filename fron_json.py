import json

'''
работает тольк для одного словаря
a = {'a': '1', 'b': '2'} # dict
with open('test.json', 'a') as file:
    json.dump(a, file, indent=4)

with open('test.json', 'r') as file:
    data = json.load(file)
print(data)
'''

'''Создать файл? записать туда лист и вытащить лист'''

# a1 = "'a': '1', 'b': '2'"
# a2 = {"a": "1", "b": "2"}
# # a3 = 'a: 1, b: 2'
# #
# with open('test.txt', 'a') as file:
#     file.write(str(a2)+'\n')
# #
# source = []
# with open('test.txt', 'r') as file:
#     for line in file:
#         source.append(line)
# print(source[0])
# print(type(source[0]))

# source = {'a': '1', 'b': '2'}
# output = ""
# quoting = False
# for char in source:
#     if char.isalnum():
#         if not quoting:
#             output += '"'
#             quoting = True
#     elif quoting:
#         output += '"'
#         quoting = False
#     output += char
#
# print(output)

a = 'sadfrtvyug'
b = 'yug'
a.find(b)
