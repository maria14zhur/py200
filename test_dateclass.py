import unittest
import dateclass as dc


class MyTestCase(unittest.TestCase):
    def test_dif_y(self):
        self.a = dc.Date(2000, 6, 23)
        self.b = dc.Date(1994, 7, 25)
        self.assertEqual(2160, dc.Date.date2_date1(self.a, self.b))

    def test_same_yearmonth(self):
        self.a = dc.Date(2000, 6, 30)
        self.b = dc.Date(2000, 6, 25)
        self.assertEqual(5, dc.Date.date2_date1(self.a, self.b))

    def test_same_year(self):
        self.a = dc.Date(2000, 4, 30)
        self.b = dc.Date(2000, 3, 31)
        self.assertEqual(30, dc.Date.date2_date1(self.a, self.b))