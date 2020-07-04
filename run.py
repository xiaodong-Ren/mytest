import math
import itertools
class modify:
    def __init__(self,name):
        self.name=int(name)
    def __add__(self,new_name):

        return self.name+int(new_name)
mo=modify(1)
print(mo.__add__(2))
