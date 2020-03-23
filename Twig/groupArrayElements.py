import numpy as np

def groupArrayElements(array, N):
    # Check that N is a positive non-zero integer
    if type(N) != int:
        raise NotImplementedError("N {} needs to be an integer".format(N))
    if N < 0:
        raise NotImplementedError("N {} needs to be a positive integer".format(N))
    if N == 0:
        raise ZeroDivisionError("N equals 0")

    arrayLength = len(array)
    if N < arrayLength:
        if array and N:
            res = []
            # Round up (ceiling) and round down (floor) division of array length by N
            # Check whether N-1 subarrays can be made with upper rounding to fill array
            floor = int(np.floor(arrayLength/N))
            ceiling = int(np.ceil(arrayLength/N))
            # If N-1 subarrays can be created using the ceiling for the size of each subarray, use ceiling
            # Using N-1 to leave one array for the remainder of the division
            if ceiling * (N-1) < arrayLength:
                subarrayLength = ceiling
            # If N-1 subarrays can't be created using the ceiling for the size of each subarray, use floor
            else:
                subarrayLength = floor

            # Create all subarrays except the last one
            for i in range(0, (N-1)*subarrayLength, subarrayLength):
                subarray = array[i:i + subarrayLength]
                res.append(subarray)
                subarray = []

            # Create the last subarray with the remaining elements
            i = (N-1)*subarrayLength
            subarray = array[i::]
            if subarray:
                res.append(subarray)

            return(res)
        return []
    else:
        # Exceptions if array is empty and if N is greater than length of array
        if arrayLength == 0:
            raise Exception("Array is empty and cannot be divided into N: {} parts".format(N))
        else:
            raise Exception("N: {} is greater than length of array: {}".format(N, arrayLength))
