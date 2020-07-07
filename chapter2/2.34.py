import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
class Satistics:
    def __init__(self,path='data\introduction.txt'):#通过路径path得到文档
        self._fp=open(path,'r',encoding='utf-8')

    def count(self):  #计算各字母的出现次数
        rate={}  #dict用于存放各字母及其出现的次数
        for line in self._fp.readlines():
            if len(line)==0:
                continue
            for i in range(len(line)):

                if not line[i] in rate:
                    if 64<ord(line[i])<91 or 96<ord(line[i])<123:  #只添加字母
                        rate[line[i]]=0
                if 64<ord(line[i])<91 or 96<ord(line[i])<123:  #只添加字母
                    rate[line[i]]+=1
        return rate

    def picture(self):#画出字母出现次数的统计表
        result=self.count()

        label=[]
        number=[]
        for key in dict(result):
           # print(value)
            label.append(key)
            number.append(result[key])
            #print(number)
        plt.bar(x=label,height=number,color='indianred',alpha=0.8) 
        plt.xlabel('字母')
        plt.ylabel('次数')
        plt.title('文档中各字母出现的次数统计表')
        plt.show()

        

if __name__=='__main__':
   # print(int('a'))
    test=Satistics()
   # result=test.count()
    #print(result)
    test.picture()
    #str = 'a1b2c3-)'
   # print filter(lambda x:x not in '0123456789',str)