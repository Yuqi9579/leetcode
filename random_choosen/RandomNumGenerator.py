'''
用rand7()实现rand10()

已有方法rand7 可生成1到7范围内的均匀随机整数，试写一个方法 rand10生成
1到10范围内的均匀随机整数。

randN -> randM
if N > M:
    while True:
        if randN <= M:
            return randN
if N < M:
    randN -> randP where P > M
    randP -> randM(above) 
'''
import random

def rand7():
    return random.randint(1,7)

def rand10():
    while True:
        rand49 = (rand7() - 1) * 7 + rand7() - 1 # 0-48的随机数
        if rand49 <= 39:  # N > M时的思想
            return rand49 // 4 + 1 #除法取整，(0~39)//4产生0~9的等概论分布

print([rand10() for i in range(20)])