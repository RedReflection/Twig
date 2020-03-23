import unittest
from groupArrayElements import groupArrayElements

class TestGroupArrayElements(unittest.TestCase):

    def createArrayAndRun(self, arrayLength, N):
        arr = [i for i in range(0, arrayLength)]
        res = groupArrayElements(arr, N)
        return res

    def assertNormalRunning(self, N, res, expectedSubarrayLength, expectedLastSubarrayLength):
        self.assertEqual(len(res), N, "res: {} is not of length: {}".format(res, N))
        for i in range(0, N - 1):
            self.assertEqual((len(res[i])), expectedSubarrayLength, "sub list {} does not have len {}".format(res[i], expectedSubarrayLength))
        self.assertEqual((len(res[-1])), expectedLastSubarrayLength,"Final sub list {} does not have len {}".format(res[-1], expectedLastSubarrayLength))

    def assertExceptionThrown(self, arrayLength, N, error, message):
        with self.assertRaises(error, msg=message):
            self.createArrayAndRun(arrayLength, N)

    def test_arrayLengthIsDivisibleByN(self):
        arrayLength = 10
        N = 2
        res = self.createArrayAndRun(arrayLength, N)
        self.assertNormalRunning(N, res, 5, 5)

    def test_useFloorForSubarrays(self):
        arrayLength = 16
        N = 5
        res = self.createArrayAndRun(arrayLength, N)
        self.assertNormalRunning(N, res, 3, 4)

    def test_useCeilingForSubarrays(self):
        arrayLength = 10
        N = 3
        res = self.createArrayAndRun(arrayLength, N)
        self.assertNormalRunning(N, res, 4, 2)

    def test_exceptionNisZero(self):
        self.assertExceptionThrown( 10, 0, ZeroDivisionError, "N equals 0")

    def test_exceptionNisGreaterThanArrayLength(self):
        self.assertExceptionThrown( 4, 9, Exception, "N: 9 is greater than length of array: 4")

    def test_exceptionEmptyArray(self):
        self.assertExceptionThrown( 0, 2, Exception,"Array is empty and cannot be divided by N: 2")

    def test_exceptionNisNotInteger(self):
        self.assertExceptionThrown( 5, 3.2, Exception, "N: 3.2 needs to be an integer")

    def test_exceptionNisNotPositiveInteger(self):
        self.assertExceptionThrown( 5, -3, Exception, "N: -3 needs to be a positive integer")

    def test_exceptionEmptyArrayAndNisZero(self):
        self.assertExceptionThrown( 0, 0, ZeroDivisionError, "N equals 0")

if __name__ == '__main__':
    unittest.main()
