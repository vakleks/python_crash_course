def show_messages(messages):
    """Show alll messages in a list."""
    for message in messages:
        msg = f"The message is: '{message}'!"
        print(msg)

phrases = ['waesome', 'great', 'nice']
show_messages(phrases)