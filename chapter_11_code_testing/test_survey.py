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

    def test_store_three_responses(self):
        """
        Check if the three individual
        responses are stored correctly.
        """
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            self.assertIn(response, my_survey.responses)    

if __name__ == '__main__':
    unittest.main()
