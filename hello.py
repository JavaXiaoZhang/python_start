import math
import statistics
import numpy as np


i = 1333
print("""hello world!""" + str(i))
print(math.sin(1))

# userAge = input('输入你的年龄：')
# print(userAge)
#
# if int(userAge) > 18:
#     print('已成年')
#     if int(userAge) < 35:
#         print('未毕业')
#     elif 40 > int(userAge) > 35:
#         print('已失业')
# else:
#     print('未成年')

list = ['111', '222']
list.append('333')
list.append

print(list[1])

dict = {'key1': 'v1', 'k2': 'v2'}

dict['k3'] = 'v3'
del dict['key1']

print(type(dict))
print(dict)
print('k1' in dict)
print(dict.get('k2'))
for i in range(1, 10):
    print(i)
print(f'{1.1111:.2f}')


def calculate(num):
    result = num / 2
    print(result)
    #return result


print(calculate(10))

print(statistics.median([111, 2222, 3333, 444]))


class cat:
    def __init__(self, sex):
        self.name = 'mimi'
        self.color = 'orange'
        self.sex = sex

    def speak(self):
        print("喵" + self.name)


cat1 = cat('y')
print(cat1.name + '' + cat1.sex)
cat1.speak()

from student import Student

student1 = Student(1, "zs")
student1.setGrades("语文", 90)
student1.printGrades()

f = open("./test.txt", "r", encoding="utf-8")
print(f.read())

lines = f.readlines()
for line in lines:
    print(line)

f.close()

with open("./test.txt", "r", encoding="utf-8") as f:
    print(f.read())

try:
    1 / 0
    print("执行完成")
except Exception:
    print("捕获异常")
finally:
    print("final")

assert 1 + 2 < 6

import numpy as np

arr1 = np.array([1,2])
print(arr1)

import pandas as pd

s1 = pd.Series(arr1)
print(s1)