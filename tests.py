from valid import valid_input
import unittest

class valid_test(unittest.TestCase):

    def test_input_1(self):

        x_position = 8

        try :
            valid_input(x_position)
            self.assertFalse(valid_input(x_position), True)
        except:
            pass

    def test_input_2(self):

        x_position = "abc"

        try:
            valid_input(x_position)
            self.assertFalse(valid_input(x_position), True)
        except:
            pass

