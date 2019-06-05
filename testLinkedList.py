import unittest
import linked_list as ll


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.a = ll.LinkedList()

    def test_clear(self):
        self.a.insert('some data')
        self.a.clear()

        self.assertEqual('No such node in LinkedList', self.a.find('some data'))

    def test_find(self):
        self.a.insert('some data1')
        self.a.insert('some data2')
        self.a.insert('some data3')
        self.a.insert('some data4')

        self.assertEqual(3, self.a.find('some data1'))

    def test_find2(self):
        self.a.insert('some data1')
        self.a.insert('some data2')
        self.a.insert('some data3')
        self.a.insert('some data4')

        self.assertEqual('No such node in LinkedList', self.a.find('s'))

    def test_remove(self):
        self.a.insert('some data4')
        self.assertIsNone(self.a.remove('some data4'))

    def test_append(self):
        self.a.append('data')
        self.a.append('data2')
        self.a.append('data3')
        self.assertEqual(0, self.a.find('data'))

    def test_delete(self):
        self.a.insert('some data3', 5)
        self.a.insert('some data0', 0)
        self.a.insert('some data1', 1)
        self.a.insert('some data2', 2)
        self.assertEqual('some data0', self.a.delete(0))

    def test_delete2(self):
        self.a.insert('some data3', 5)
        self.a.insert('some data0', 0)
        self.a.insert('some data1', 1)
        self.a.insert('some data2', 2)
        self.assertEqual('some data2', self.a.delete(2))

    def test_delete3(self):
        self.a.insert('some data3', 5)
        self.a.insert('some data0', 0)
        self.a.insert('some data1', 1)
        self.a.insert('some data2', 2)
        self.assertEqual('some data3', self.a.delete(3))

if __name__ == '__main__':
    unittest.main()
