import unittest

from src.high_scores import latest, personal_best, personal_top_three, highest_to_lowest_scores, top_two

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [2, 4, 10, 10, 2, 3]
        # self.scores = [10, 10]
        # self.scores = [10]

    # # Test latest score (the last thing in the list)
    def test_can_get_latest_score(self):
        expected_value = 3
        actual_value = latest(self.scores)
        self.assertEqual(expected_value, actual_value)

    # # Test personal best (the highest score in the list)
    def test_can_get_personal_best(self):
        expected_value = 10
        actual_value = personal_best(self.scores)
        self.assertEqual(expected_value, actual_value)

    # # Test top three from list of scores
    def test_can_get_top_3(self):
        expected_value = [10, 10, 4]
        actual_value = personal_top_three(self.scores)
        self.assertEqual(expected_value, actual_value)

    # # Test ordered from highest tp lowest
    def test_can_get_highest_to_lowest_scores(self):
        expected_value = [10, 10, 4, 3, 2, 2]
        actual_value = highest_to_lowest_scores(self.scores)
        self.assertEqual(expected_value, actual_value)

    # # Test top three when there is a tie
    def test_can_get_top_3_with_tie(self):
        expected_value = [10, 10, 4]
        actual_value = personal_top_three(self.scores)
        self.assertEqual(expected_value, actual_value)

    # # Test top three when there are less than three
    def test_top_3_when_there_is_only_2(self):
    #     # expected_value = [10, 10]
    #     # actual_value = top_two(self.scores)
    #     # self.assertEqual(expected_value, actual_value)
        # expected_value = [10, 10]
        # actual_value = personal_top_three(self.scores)
        # self.assertEqual(expected_value, actual_value)
        self.scores = [10, 10]
        expected_value = [10, 10]
        actual_value = personal_top_three(self.scores)
        self.assertEqual(expected_value, actual_value)
        # two seperate soloutions for the same problem worded differently

    # Test top three when there is only one
    def test_top_three_when_there_is_only_1(self):
        self.scores = [10]
        expected_value = [10]
        actual_value = personal_top_three(self.scores)
        self.assertEqual(expected_value, actual_value)
        # expected_value = [10]
        # actual_value = personal_top_three(self.scores)
        # self.assertEqual(expected_value, actual_value)
        # expected_value = [10]
        # actual_value = personal_best(self.scores)
        # self.assertEqual(expected_value, actual_value)
    # two seperate soloutions for the same problem worded differently


