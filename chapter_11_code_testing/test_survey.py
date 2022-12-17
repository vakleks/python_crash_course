import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for TestAnonymousSurvey class."""

    def test_single_response(self):
        """Check whether the single answer is saved correctly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_reponse('English')
        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
    unittest.main()
