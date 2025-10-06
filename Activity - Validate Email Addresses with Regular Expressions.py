import re

def validate_email(email):
    email_addresses_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    """
    Validates an email address using a regular expression.

    Args:
    email: The email address to validate.

    Returns:
    True if the email is valid, False otherwise.
    """
    ### YOUR CODE HERE ###
    if re.match(email_addresses_pattern, email): 
        return True
    else:
       return False

# Test cases
emails = [
    "test@example.com",
    "invalid.email",
    "another_test@domain.co.uk",
    "not_valid@.com",
    "user+123@company.net"
]

# Validate each email and print the result
for email in emails:
  if validate_email(email):
    print(f"{email} is a valid email.")
  else:
    print(f"{email} is not a valid email.")