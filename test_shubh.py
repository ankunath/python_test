#!/usr/bin/env python
import unittest
from mounttab2 import parse_mounts, parse_mounts1, parse_mounts2, parse_mounts3

class TestMount(unittest.TestCase):
    """
    Our basic test class
    """

    def test_parsemount(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        result = parse_mounts()
	
	var1 = 100
	if var1:
	   print "1 - Got a true expression value"
	   print var1
	else:
	   print "1 - Got a false expression value"
	   print var1

        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)

    def test_parsemount1(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        result = parse_mounts1()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)

    def test_parsemount2(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        result = parse_mounts2()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)

    def test_parsemount3(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        result = parse_mounts3()
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)

 

if __name__ == '__main__':
    unittest.main()
