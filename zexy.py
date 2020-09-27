# coding: utf-8
import time

t1 = time.time()
str1 = ""
for i in range(10000000):
    str1 += "aaa"
t2 = time.time()
print("+=消耗时间为{}".format(t2-t1))


t3 = time.time()
list1 = []
for i in range(10000000):
    list1.append("aaa")
a = "".join(list1)
t4 = time.time()
print("join消耗时间为{}".format(t4-t3))









