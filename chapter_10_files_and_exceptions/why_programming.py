filename = 'programming_reasons.txt'

reasons = []
while True:
    reason = input("Yor programming reasons?")
    reasons.append(reason)

    continue_poll = input("Add another reason? (yes/no)")
    if continue_poll == 'no':
        break

with open(filename, 'a') as file:
    for reason in reasons:
        file.write(f"{reason}\n")