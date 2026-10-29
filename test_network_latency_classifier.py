import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import band


class TestLatency(unittest.TestCase):
    def test_bands(self):
        self.assertEqual(band(20), "excellent")
        self.assertEqual(band(100), "good")
        self.assertEqual(band(200), "fair")
        self.assertEqual(band(500), "poor")

    def test_boundary(self):
        self.assertEqual(band(50), "good")
