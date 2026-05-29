import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from solution import assign_tables as user_assign_tables

class TestSampleAssignTables(unittest.TestCase):

    def _check(self, groups, tables_num, answer):
        out_user, collisions_user = user_assign_tables(groups, tables_num)
        out_answer, collisions_answer = answer
        self.assertEqual(out_user, out_answer, f"Table numbers mismatch for input: {groups}")
        self.assertEqual(collisions_user, collisions_answer, f"Collisions mismatch for input: {groups}")

    def test_assign_tables_1(self):
        groups = {"Team1": ["Ali", "Sara", "Mamad"], "Team2": ["Reza", "Nina", "Gholi"]}
        answer = ({'Team1': 1, 'Team2': 0}, [])
        self._check(groups, 2, answer)

    def test_assign_tables_2(self):
        groups = {"Alpha": ["John", "Doe"], "Beta": ["Jane", "Smith"]}
        answer = ({'Alpha': 0, 'Beta': 1}, [])
        self._check(groups, 3, answer)

    def test_assign_tables_3(self):
        groups = {"Group1": ["Tom", "Jerry"], "Group2": ["Spike", "Tyke"], "Group3": ["Olampic", "Fanavari"]}
        answer = ({'Group1': 2, 'Group2': 2, 'Group3': 0}, [('Group2', 2, 'Group1')])
        self._check(groups, 4, answer)

    def test_assign_tables_4(self):
        groups = {"Red": ["Rick", "Morty", "Gogoli"], "Blue": ["Summer", "Winter"]}
        answer = ({'Red': 0, 'Blue': 0}, [('Blue', 0, 'Red')])
        self._check(groups, 2, answer)

    def test_assign_tables_5(self):
        groups = {"X1": ["Neo", "Trinity"], "X2": ["Morpheus", "Cypher"]}
        answer = ({'X1': 2, 'X2': 2}, [('X2', 2, 'X1')])
        self._check(groups, 4, answer)

if __name__ == "__main__":
    unittest.main()
