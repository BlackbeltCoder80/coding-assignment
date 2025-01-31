emails = ["user_email_1", None, "user_email_2", "user_email_3", None]

valid_emails = []
for email in emails:    
    print(f"checking this email: {email}")
    if email is None:
        print(f"email {email} is not valid")    
        continue
    input()
    print("Adding to valid_emails list...")
    valid_emails.append(email)
    print(valid_emails)
