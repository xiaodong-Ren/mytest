import math
class Progression:
    def __init__(self,start=0):
        self._current=start
    
    def _advance(self):
        self._current+=1
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer=self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self

    def print_pro(self,n):
        print('、'.join(str(next(self)) for i in range(n)))


class Arithmetic(Progression):
    def __init__(self,step=1,start=0):
        super().__init__(start)
        self._step=step
    def _advance(self):
        self._current+=self._step



class Fibonacci(Progression):
    def __init__(self,current=0,next_value=1):
        super().__init__(current)
        self._next_value=next_value
        
    def _advance(self):
        self._current,self._next_value=self._next_value,self._current+self._next_value
    def __getitem__(self,i):
        for k in range(i):
            self._advance()
        return self._current
if __name__ == '__main__':
    pro=Fibonacci(2,2)
    pro.print_pro(8)
    ari=Arithmetic(128,0)
    for i,item in enumerate(ari):
        if item >= pow(2,23):
            print(i)
            break