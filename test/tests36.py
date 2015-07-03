__author__ = 'dorcas'
import unittest
import tool36
import euler36

class toolTester(unittest.TestCase):

    def setup(self):
        pass

    def test_main_55(self):
        self.assertEqual(58, euler36.main(55), 'it is wrong my dear')

    # def test_euler_9876(self):
        # self.assertEquals(9876, euler36(9876), 'wooooow')

    # def test_euler_3000657(self):
        # self.assertEquals(30000657, euler36.euler(3000657), 'i see')


if __name__ == '__main__':
    unittest.main()



