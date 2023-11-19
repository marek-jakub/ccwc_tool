import unittest

import ccwc_methods as ccwc_tool


class TestCcwc(unittest.TestCase):

    def test_file_size(self):
        self.assertEqual(
            ccwc_tool.Ccwc.bytes_in_file('test.txt'),
            342190, 'File size incorrect')

    def test_number_of_lines(self):
        self.assertEqual(
            ccwc_tool.Ccwc.lines_in_file('test.txt'),
            7145, 'Number of lines incorrect')

    def test_words_in_file(self):
        self.assertEqual(
            ccwc_tool.Ccwc.words_in_file('test.txt'),
            58164, 'Number of words incorrect')

    def test_chars_in_file(self):
        self.assertEqual(
            ccwc_tool.Ccwc.chars_in_file('test.txt'),
            339292, 'Number of characters incorrect')


if __name__ == '__main__':
    unittest.main()
