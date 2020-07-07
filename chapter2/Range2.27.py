import time
class Range:
    def __init__(self,start,stop=None,step=1):
        if step==0:
            raise ValueError('step cannot be 0')
        if stop==None:
            stop,start=start,0
        self._len=(stop-start+step-1)/step
        self._start,self._step=start,step

    def __len__(self):
        return self._len
    
    def __getitem__(self,k):
        if k<0 :
            k+=self._len
        if not 0<=k<self._len:
            raise IndexError('index out of range')
        return self._start+k*self._step

    def __contains__(self,a):
        if a<self._start or a>self._start+self._len:
            return False
        if (a-self._start)%self._step != 0:
            return False
        return True

if __name__=='__main__':
    start_time=time.time()
    if 2 in Range(100000):
        end_time=time.time()
        print('need time:',end_time-start_time)
    start_time1=time.time()
    if 99999.5 in Range(100000):
        end_time1=time.time()
        print('need time:',end_time1-start_time1)
        

