import numpy as np

def groupArrayElements(arr, N):
    if type(N) != int:
        raise NotImplementedError( "N {} needs to be an integer".format(N))
    if N < 0 :
        raise NotImplementedError( "N {} needs to be a positive integer".format(N))
    if N == 0:
        raise ZeroDivisionError("N equals 0")
    arrLen = len(arr)
    if N < arrLen:
        if arr and N:
            res = []
            fl = int(np.floor(arrLen/N))
            cl = int(np.ceil(arrLen/N))
            if cl * (N-1) >= arrLen:
                arrSize = fl
            else:
                arrSize = cl

            for i in range(0, N-1):
                i = i*arrSize
                arrI = arr[i:i+arrSize]
                res.append(arrI)
                arrI = []

            i = i+arrSize
            arrI = arr[i::]
            if arrI:
                res.append(arrI)

            return(res)
        return []
    else:
        if arrLen == 0:
            raise Exception("Array is empty and cannot be divided by N: {}".format(N))
        else:
            raise Exception("N: {} is greater than length of array: {}".format(N, arrLen))
