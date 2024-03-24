def checkPasswordStrength(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password is too short. Aim for at least 8 characters.")
    if not any(c.isupper() for c in password):
        feedback.append("Uppercase characters are missing.")
    if not any(c.islower() for c in password):
        feedback.append("Lowercase characters are missing.")
    if not any(c.isdigit() for c in password):
        feedback.append("Digits are missing.")
    if not any(c in "!@#$%^&*()_-+=<>?.,;:|{}[]~" for c in password):
        feedback.append("Special characters are missing.")

    if not feedback:
        return "Strong: Password meets all criteria."
    else:
        return "Weak: " + "and ".join(feedback)

def main():
    userPassword = input("Enter your password: ")
    strengthFeedback = checkPasswordStrength(user_password)
    print(strengthFeedback)

if __name__ == "__main__":
    main()
