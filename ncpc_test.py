# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:20:57 2020

@author: jhaj
"""

import unittest
import ncpc_functions

class Test_NCPC(unittest.TestCase):
    
    def test_A_2013(self):
        self.assertEqual(ncpc_functions.A_2013(4, [2, 3, 4, 3]), 7)
        self.assertEqual(ncpc_functions.A_2013(6, [39, 38, 9, 35, 39, 20]), 42)
    """
    def test_E_2013(self):
        self.assertEqual(ncpc_functions.E_2013("AAAAA", "AGCGAA"), 3)
        self.assertEqual(ncpc_functions.E_2013("GTTTGACACACATT", "GTTTGACCACAT"), 4)
        
    def test_G_2013(self):
        self.assertEqual(ncpc_functions.G_2013(1, "10001110101000001111010100001110", "01110001010111110000101011110001"), "Deletion succeeded")
        self.assertEqual(ncpc_functions.G_2013(20, "0001100011001010", "0001000011000100"), "Deletion failed")
    """
    def test_A_2014(self):
        self.assertEqual(ncpc_functions.A_2014(4, 4, [[1, 2, 2], [2, 3, 1], [3, 4, 1], [4, 1, 2]]), 3)
        self.assertEqual(ncpc_functions.A_2014(5, 5, [[1, 2, 1], [2, 3, 1], [2, 4, 1], [2, 5, 1], [4, 5, 1]]), "impossible")
        self.assertEqual(ncpc_functions.A_2014(4, 5, [[1, 2, 1], [2, 3, 0], [2, 4, 1], [3, 1, 1], [3, 4, 1]]), 2)
    """    
    def test_D_2014(self):
        self.assertEqual(ncpc_functions.D_2014([1,4,1,4], [1,6,1,6]), "Emma")
        self.assertEqual(ncpc_functions.D_2014([1,8,1,8], [1,10,2,5]), "Tie")
        self.assertEqual(ncpc_functions.D_2014([2,5,2,7], [1,5,2,5]), "Gunnar")
        
    def test_E_2014(self):
        self.assertEqual(ncpc_functions.E_2014(6, [2, 1, 8, 8, 2, 3]), 5)
        self.assertEqual(ncpc_functions.E_2014(5, [1, 1, 1, 1, 10]), 2)
        
    def test_G_2014(self):
        self.assertEqual(ncpc_functions.G_2014(4, 4, [1, 2, 3, 4]), 4)
        self.assertEqual(ncpc_functions.G_2014(12, 3, [2, 3, 4, 5, 6, 7, 4, 7, 8, 8, 12, 12]), 2)
        self.assertEqual(ncpc_functions.G_2014(5, 4, [2, 3, 1, 5, 4]), 3)
    """    
    def test_I_2014(self):
        self.assertEqual(ncpc_functions.I_2014(10, [[0, 0, 1, 0], [0, 1, 1, 1], [0, 2, 2, 2], [0, 0, 0, 4], [1, -1, 1, 0], [2, -2, 2, 2], [1, 1, 2, 2], [1, 1, 0, 2], [3, 1, 2, 2], [1, 3, 0, 2]]), 6)
        
        
if __name__ == '__main__':
    unittest.main()