# passwordStrengthChecker

Key Features:

Multi-Criteria Evaluation: 
The checkPasswordStrength function checks for password strength by evaluating multiple factors:
Length (at least 8 characters)
Presence of uppercase letters
Presence of lowercase letters
Presence of digits
Presence of special characters

Clear Feedback: 
The function provides informative feedback, indicating specific areas for improvement if the password is weak.
User Input and Output: It prompts the user to enter a password, evaluates its strength, and prints appropriate feedback.

# Functionality:

The checkPasswordStrength function:
Takes a password as input.
Creates a list to store feedback messages.
Checks for each strength criterion and adds corresponding feedback if not met.
Returns "Strong: Password meets all criteria" if no issues are found, otherwise returns "Weak: " followed by a list of issues.
The main function:
Prompts the user to enter a password.
Calls the checkPasswordStrength function to evaluate it.
Prints the returned strength feedback to guide the user.
