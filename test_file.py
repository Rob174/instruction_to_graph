import numpy as np
from pathlib import Path

from h5py import File


class Test:
    def normalise(self,d):
        return (d-np.mean(d))/(np.std(d))
    def test1(self,data1,data2):
        data1 = self.normalise(data1)
        data1 = (data1-np.mean(data1))/np.std(data1)
        data2 = self.normalise(data2)
        data2 *= 2
        l=[data2 for _ in range(10)]
        lout = []
        for v in l:
            lout.append(2*v)


        data1 = np.stack((data1,)*3,axis=0)
        return data1,lout

