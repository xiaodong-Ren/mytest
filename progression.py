import math
import itertools
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

class Fibonacci(Progression):
    def __init__(self,current=0,next_value=1):
        super().__init__(current)
        self._next_value=next_value
        
    def _advance(self):
        self._current,self._next_value=self._next_value,self._current+self._next_value

if __name__ == '__main__':
    pro=Fibonacci(4,6)
    for i in pro:
        if i<=50:
            print(i)
        else:
            break