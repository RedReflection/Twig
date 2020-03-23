from numpy import floor

class GroupArrayElements(object):
    def __init__(self, arr, N):
        self.arr = arr
        self.N = N

    def run(self):
        finalArrSize = len(self.arr) % self.N
        res = []
        for i in floor(len(self.arr)/N):
