import unittest
import BCRA

class TestBCRA(unittest.TestCase):
    def test_monetary_base_fecth(self):
    	self.assertEqual(len(BCRA.monetary_base('1 Y')), 365, "Monetary base for 1 Y should be 365")

if __name__ == '__main__':
    unittest.main()
