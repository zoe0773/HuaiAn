#coding=utf-8

def arrt(*args):
    '''不定长参数传递'''
    for i in args:
        print(i)

arrt(1,2,3,4)
print("****************************")
li = (1,2,3,4,5)

arrt(*li)
