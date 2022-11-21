uncomfirmed_users = ['aleks', 'brian', 'candace']
confirmed_users = []

while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())