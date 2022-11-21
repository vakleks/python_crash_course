def send_messages(unsended_messages, sended_messages):
    """
    simulate sending of each messages, till all of them out.
    transwer each message to seneded_messages after sending.
    """
    while unsended_messages:
        current_message = unsended_messages.pop()
        print(f"The meassage is: {current_message}")
        sended_messages.append(current_message)

def show_sended_messages(sended_messages):
    """Sow all sended messages."""
    print(f"\nThe next messages have been sended:")
    for sended_message in sended_messages:
        print(sended_message)

unsended_messages = ['awesome', 'great', 'nice']
sended_messages = []

send_messages(unsended_messages[:], sended_messages)
show_sended_messages(sended_messages)