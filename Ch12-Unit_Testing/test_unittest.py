import unittest

def my_sum(*nums):
    return sum(nums)

def my_avg(*nums):
    return sum(nums)/len(nums)

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(my_sum(1, 2, 3), 6, "Should be 6")
    
    def test_avg(self):
        self.assertEqual(my_avg(1, 2, 3), 2.0, "Should be 2.0")

if __name__ == '__main__': #This to check if this module has been using.
                            #if it's not being used, run this module as main. 
    unittest.main()
