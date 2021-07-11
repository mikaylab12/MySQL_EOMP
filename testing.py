# id number testing
import unittest
import rsaidnumber

# testing the id number
def id_number():
    number = rsaidnumber.parse('0011120149080')
    return number.valid


class Rsa(unittest.TestCase):
    def checking(self):
        x = rsaidnumber.parse('0011120149080')

    def testing(self):
        self.assertTrue(rsaidnumber.RSA_ID_LENGTH, 13)


if __name__ == '__main__':
    unittest.main()
