import math
import itertools
def test(a,b):   #有两个数字作为输入，一个是需支付的钱数，另一个是你给的钱数。货币体系：[0.5,1,5,10,20,50,100]
    num=[0,0,0,0,0,0,0]
    value=[100,50,20,10,5,1,0.5]
    diff=b-a
    for i in range(len(value)):
        if diff>=value[i]:
            k=i
            while diff>=value[k]:
                num[k]+=1
                diff-=value[k]
        elif diff==0:
            break
    for i in range(len(value)):
        if num[i]!=0:
            print(value[i],'元:',num[i],'张')

a=20
b=87
print(test(a,b))