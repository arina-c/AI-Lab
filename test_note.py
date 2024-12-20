import unittest
from functions import note

class test_note(unittest.TestCase):
    def test_case_1(self):
        input_data = 1
        expected_result = "C#1"
        self.assertEqual(note(input_data), expected_result)

    def test_case_2(self):
        input_data = 128
        with self.assertRaises(ValueError) as context:
            note(input_data)
        self.assertEqual(str(context.exception), "Invalid MIDI number")

    def test_case_3(self):
        input_data = '128'
        with self.assertRaises(ValueError) as context:
            note(input_data)
        self.assertEqual(str(context.exception), "Invalid MIDI number")
