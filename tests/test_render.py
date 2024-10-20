
import unittest
import roland_firmware.render
import os

class TestRender(unittest.TestCase):

  def test_fetch(self):
    model = "juno-x"
    data = roland_firmware.render.fetch_data([model])
    self.assertEqual(len(data), 1)
    self.assertEqual(len(data[model]), 3)

  def test_render(self):
    data = { "juno-x": { "url": "http://no", "version": "1.0", "date": "2020-01-01" } }
    content = roland_firmware.render.template(data)
    self.assertIn("JUNO-X", content)

  def test_write(self):
    content = "foo"
    filename = "/tmp/testfile.html"
    roland_firmware.render.write_content(filename, content)
    self.assertTrue(os.path.exists(filename))
    with open(filename, "r") as f:
      self.assertIn(content, f.read())
    os.remove(filename)

if __name__ == '__main__':
  unittest.main()