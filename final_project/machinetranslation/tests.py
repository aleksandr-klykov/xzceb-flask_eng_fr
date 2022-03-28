import unittest
from translator import frenchToEnglish, englishToFrench

class TestenglishtoFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestfrenchtoEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
unittest.main()