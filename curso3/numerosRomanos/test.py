import romanos 
import unittest

class Tester(unittest.TestCase):
   def setUp(self):
      self.roman= romanos.Romanos()

   # Simples
   def testValue1(self):
      return self.assertEqual("I", self.roman.toRoman(1))

   def testValue5(self):
      return self.assertEqual("V", self.roman.toRoman(5))

   def testValue10(self):
      return self.assertEqual("X", self.roman.toRoman(10))

   def testValue50(self):
      return self.assertEqual("L", self.roman.toRoman(50))

   def testValue100(self):
      return self.assertEqual("C", self.roman.toRoman(100))

   def testValue500(self):
      return self.assertEqual("D", self.roman.toRoman(500))

   def testValue1000(self):
      return self.assertEqual("M", self.roman.toRoman(1000))

   # Agrupados
   def testValue600(self):
      return self.assertEqual("DC", self.roman.toRoman(600))

   def testValue666(self):
      return self.assertEqual("DCLXVI", self.roman.toRoman(666))

   # Con Restos
   def testValue4(self):
      return self.assertEqual("IV", self.roman.toRoman(4))

   def testValue9(self):
      return self.assertEqual("IX", self.roman.toRoman(9))

   def testValue49(self):
      return self.assertEqual("XLIX", self.roman.toRoman(49))

   def testValue99(self):
      return self.assertEqual("XCIX", self.roman.toRoman(99))

   def testValue499(self):
      return self.assertEqual("CDXCIX", self.roman.toRoman(499))

   def testValue999(self):
      return self.assertEqual("CMXCIX", self.roman.toRoman(999))


unittest.main()