
import unittest
import roland_firmware.parse
import roland_firmware.render
import os


class TestParse(unittest.TestCase): 

  def test_known(self):
    data = roland_firmware.parse.get_latest('juno-x')
    self.assertEqual(len(data), 2)

  def test_bad_model(self):
    with self.assertRaises(SystemExit):
      roland_firmware.parse.get_latest('bogus-product')

if __name__ == '__main__':
  unittest.main()
