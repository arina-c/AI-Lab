import unittest
from functions import generate, create_trie, print_trie

class test_generate(unittest.TestCase):
    def test_case_1(self):
        degree = 4
        roots, comp = create_trie(degree)
        melody = generate(["C4", "C5"], 50, roots, degree)
        ok = True
        for i in range(len(melody)-degree):
            if melody[i: i + degree + 1] not in comp:
                ok = False
        self.assertTrue(ok)

        

    