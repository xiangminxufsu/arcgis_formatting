#test for formatting.py

import unittest
from formating import handler

class Test(unittest.TestCase):
        def testhandler(self):
            r1 = handler('abc')
            self.assertEqual('abc',r1)
        

        def test_split(self):
            s = 'hello world'
            self.assertEqual(s.split(), ['hello', 'world'])
            # check that s.split fails when the separator is not a string
            with self.assertRaises(TypeError,self.assertEqual(s.split(), ['hello', 'world'])):
                s.split(2)
                
if __name__=='__main__':
    unittest.main()