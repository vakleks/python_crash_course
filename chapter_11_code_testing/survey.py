class AnonymysSurvey:
    """Collect anonymous answers to the questions."""

    def __init__(self, question):
        """Save questions and prepare to store answers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show questions."""
        print(self, question)

    def store_reponse(self, new_response):
        """Save one response to question."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all provided answers."""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")
