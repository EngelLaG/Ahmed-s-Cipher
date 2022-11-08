import unittest
from encrypt import encrypt_file
from decrypt import decrypt_file


class Test_test(unittest.TestCase):
    def test_Hello(self):
        self.assertEqual(encrypt_file(2,"Easy"),"Esay")
    def test_Hello2(self):
        self.assertEqual(encrypt_file(2,"Easy"),"Easy")
    def test_Hello3(self):
        self.assertEqual(decrypt_file(2,"Esay"),"Easy")
if __name__ == '__main__':
    unittest.main()

