import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for TestAnonymousSurvey class."""

    def setUp(self):
        """
        Create survey and set of responses for
        all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_single_response(self):
        """Check whether the single answer is saved correctly."""
        self.my_survey.store_reponse(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """
        Check if the three individual
        responses are stored correctly.
        """
        for response in self.responses:
            self.my_survey.store_reponse(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)   

if __name__ == '__main__':
    unittest.main()
