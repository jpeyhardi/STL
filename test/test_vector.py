from statiskit import stl

import unittest
from nose.plugins.attrib import attr

@attr(linux=True, 
      osx=True,
      win=True,
      level=1)
class TestVector(unittest.TestCase):

    def test___initialization(self):
        """Test vector initialization"""

        v = stl.VectorIndex()
        self.assertEqual(len(v), 0)

    def test__equal(self):
        """Test vectors equality"""

        v1 = stl.VectorIndex()
        v1.push_back(3)
        v1.push_back(1)
        v1.push_back(2)
        v2 = stl.VectorIndex()
        v2.push_back(3)
        v2.push_back(1)
        v2.push_back(2)
        self.assertEqual(v1, v2)
        v3 = stl.VectorString()
        v3.push_back('A')
        v3.push_back('B')
        v3.push_back('C')
        v4 = stl.VectorString()
        v4.push_back('A')
        v4.push_back('B')
        v4.push_back('C')
        self.assertEqual(v3, v4)