class ReversedSequenceIterator:
    def __init__(self,sequence):
        self._seq=sequence
        self._k=len(self._seq)

    def __next__(self):
        self._k -= 1 
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self
    
if __name__=='__main__':
    seq=[2,1,34,54]
    for item in ReversedSequenceIterator(seq):
        print(item)
