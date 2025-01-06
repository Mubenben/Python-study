

import re
'''

# time
import time
import calendar

ticks = time.time()
print("time ticks:", ticks)

localtime = time.localtime(time.time())
print("Local current time :", localtime)


localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a-%b-%d %H:%M:%S%Y", time.localtime()))

cal = calendar.month(24, 12)
print("Here is the calendar:\n", cal)


bitcalc1 = 0x2
bitcalc2 = 0xe
print("bitcalc1 & bitcalc2 = ", bitcalc1 & bitcalc2)
print("bitcalc1 | bitcalc2 = ", bitcalc1 | bitcalc2)
print("bitcalc1 ^ bitcalc2 = ", bitcalc1 ^ bitcalc2)
print("~bitcalc1 = ", ~bitcalc1)
print("bitcalc1 << 2 = ", bitcalc1 << 2)
print("bitcalc1 >> 1 = ", bitcalc1 >> 1)



# 逻辑测试表示False
array_false = [False, None, 0, 0.0, 0j, [], {}, (), set()]
for i in array_false:
    print(i, "is False:", bool(i))


# 顺序、选择、循环语句
userStae = False
if not userStae: print("hello ")

publisher = ["zhangsan", "lisi", "wangwu"]
for i in range(len(publisher)):
    print(i+1,publisher[i]+"-----")

print('--------------------')

for n in range(2, 8):
    for m in range(2, n): # range(2,2) 为空
        print(n, m)
        if n % m == 0:
            print(n, "= ", m, "*", n//m)
            break
    else:
        print(n,'是一个质数')

for n in range(101):
    mystr = "percentage " + str(n) + " %"
    print(mystr, end=" ")
    print("\b"*(len(mystr)*2),end="",flush=True)
    time.sleep(0.01)

# while 倒计时
sec = 6*3600 + 37*60 + 7
# while sec > 0:
#     if sec >= 0:
#         days = sec // (24*3600)
#         hours = sec // 3600 % 24
#         minutes = sec // 60 % 60
#         sec = sec - 60
#         print("%02d:%02d:%02d:%02d" % (days, hours, minutes, sec))
#         time.sleep(0.05)

while(sec>=0):
    if(sec>=0):
        days = int((sec/3600)/24)
        hours = int((sec-days*24*3600)/3600)
        minutes = int((sec-days*24*3600-hours*3600)/60)
        seconds = (sec-hours*3600)% 60
        strHours= days*24+hours
        strP = "End: "+str(strHours)+"Hours "+str(minutes)+"Minutes "+str(seconds)+"Seconds "
        print(strP)

'''


# 序列数据
list1 = list(range(2,20,3))
list2 = ['a','b','c']
x = [list1,list2]

print("print(list1)\
print(list1[2:4])\
print(list1[2:])\
print(list1[:4])\
print(list1[:])\
print(list1[1:3:2])")
print(list1)
print(list1[2:4])
print(list1[2:])
print(list1[:4])
print(list1[:])
print(list1[1:4:2]) # 1:4:2,其中1是开始位置，4是结束位置，2是步长
print(list1[-1]," ",list1[1])


print("print(x)\
print(x[0][1])\
print(x[1][1:2])\
")
print(x)
print(x[0][1])
print(x[1][1:2])

print("print(len(list1),len(x))\
print(max(list1),max(x))\
print(min(list1),min(x))\
print(sum(list1),sum(x))\
print(sorted(list1),sorted(x))\
print(reversed(list1),reversed(x))\
print(str(list1),str(x))\
print(list(list1),list(x))\
print(enumerate(list1),enumerate(x))\
")
print(len(list1),len(x))
print(max(list1)) #,max(x)
print(min(list1)) #,min(x)
print(sum(list1)) #,sum(x)
print(sorted(list1))
print(list(reversed(list1)),reversed(x))
print(str(list1),str(x))
print(list(list1),list(x))
print(list(enumerate(list1)),enumerate(x))

for index,item in enumerate(list1):
    print("index, item: ",index,item)


print("list 可变，tuple 中单个元素值不可变。tuple 可以重新整个赋值。tuple中的可变对象，可变。如tuple中的list可变。\
    tuple 可访问[],可截取[:]，可连接+和重复*，可删除 del tuple\
    ")
print()

print("tuple1 = (1,2,3,4,5)\
print(tuple1[2],tuple1[2:4])\
tuple2 = tuple1 + tuple1\
tuple2 = tuple1 * 3\
")
tuple1 = (1,2,6,3,5,4)
print(tuple1[2],tuple1[2:4])
tuple2 = tuple1 + tuple1
print(tuple2)
tuple2 = tuple1 * 3
print(tuple2)
tuple2 = (9,[11,12,13])
print(tuple2)
tuple2[1][2] = 'a'
print(tuple2,tuple1)
print("tuple1.index(6),tuple1.count('6'),tuple1.count(6),sorted(tuple1)")
print(tuple1.index(6),tuple1.count('6'),tuple1.count(6),sorted(tuple1))
del tuple2
# print(tuple2)
tuple3 = ("go",)*3
print(tuple3)

print()
print("list是有序集合，dict是无序集合")
dict1 = {'name':'zhangsan','age':18,'sex':'male',4:'a'}
dict2 = {}
dict3 = dict()
print(dict1,dict2,dict3)
print(dict1['age'])

dictkey = ['name','age','sex',5]
dictvalue = ['lisi',20,'female','b']
dict4 = dict(zip(dictkey,dictvalue))
print(dict4)

dict5 = dict(name='wangwu',age=22,sex='male')

print()
print("print(dict5)\
print(dict5.keys())\
print(dict5.values())\
print(dict5.items())\
")

print(dict5)
print(dict5.keys())
print(dict5.values())
print(dict5.items())
dict5['name2'] = 'zhaoliu'
print(dict5)
dict5['name2'] = 'zhaoliuliu'
print(dict5)
del dict5['name2']
print(dict5)
print(len(dict5),str(dict5),type(dict5))
print(dict5['name'] if 'name' in dict5 else 'not exist')
print(dict5['name3'] if 'name3' in dict5 else 'not exist')

for item in dict5.items():
    print('item:',item)
for key,value in dict5.items():
    print('key,value: ',key,value)


print('\n set 是一个无序不重复元素序列')
print()
set1 = {"name1","name2","name3"}
set2 = set(["name1","name2","name3"])
print(set1,set2)
set1.add('apple')
print(set1)
set1.add('banana')
set1.update(['apple','banana','orange'])
print(set1)
set1.remove('apple')
print(set1)
set1.discard('banana')
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)

set3 = {'apple','banana','orange','watermelon'}
set4 = {'apple','banana','orange','pear'}
set5 = {'apple','banana','orange'}
print('set3,set4,set5  集合方法',set3,set4,set5)
print(set3.union(set4)) # 交集
print(set3.intersection(set4)) # 并集
print(set3.difference(set4)) # 差集
print(set3.symmetric_difference(set4)) # 两个集合中不重复的元素集合，差集
print(set3.issubset(set4)) # 3 是否是4的子集
print(set5.issubset(set3)) # 
print(set3.issuperset(set4)) # 3 是否是4的超集
print(set3.issuperset(set5)) #
print(set3.isdisjoint(set4)) # 3和4是否没有交集,若有交集，返回False；若没有交集，返回True



set6 = {'a','b','c'}
set7 = {'d','e','a','b'}
set8 = {'a','b','c','d','e'}
set9 = {'a','b'}
print('set6,set7,set8  集合运算',set6,set7,set8)
print(set6 | set7) # 并
print(set6 & set7) # 交
print(set6 - set7) # 差, 6-7的差
print(set6 ^ set7) # 差, 6-7的差和7-6的差 的合并
print(set6 < set7) # 6是否是7的子集
print(set6 > set7) # 6是否是7的子集
print(set9 < set6) # 6是否是7的子集



str1 = 'Hello word. I am a student.'
str2 = 'abcde'
print('字符串不能直接与其他类型数据连接+')
print(str1[0])
print(str1[0:5])
print(str1[0:5:2])
print(str1[::-1])
print(str1[-2])
print(str1+' '+str2)
print(str1 * 3)
print('Hello' in str1)
print(r'\\ \n')
print(str1.split(' '))
print(str1.split(' ', 2))
print(str1.find('word'),str1.find('o'))
print(str1.replace('word', 'world'))
print(max(str1),min(str1))
print(str1.upper())
print(str1.lower())
print(str1.title())
sword = ' '.join(str1.split(' ')[::-1]) # 翻转字符串
print(sword)


print('format')
print('{} {} {}'.format('alice',21,'c'))
print('{0} {1} {2}'.format('alice',21,'c'))
print('{0} {2} {1}'.format('alice',21,'c'))
print('{0} {1} {other}'.format('alice',21,other='c'))

fieldName = ['id','name','price','codenum','publishment']
bookdate = [1,'python',99.9,123456,'oreilly']
for item in fieldName:
    print('{0:>10s}'.format(item),end=' ') # 0:>10s,表示字符串右对齐，宽度为10
print()
for item in fieldName:
    print('{0:^10s}'.format(item),end=' ') # 0:^10s,表示


print('regular expression, 正则表达式')
print('\d{3}-\d{3}-\d{4}')


match = re.match(r'go.*d','good goac')
print(match.group())









































