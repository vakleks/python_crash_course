from survey import AnonymousSurvey

# Define the questions and create a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show questions and save answers to it.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_reponse(response)

# Show the results of survey.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
