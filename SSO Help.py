# Helper functions for formatting questions and steps
def ask_question(question):
    print(f"\033[1m{question}\033[0m", end="")
    return input()


def print_bold(text):
    print(f"\033[1m{text}\033[0m")


def print_steps(steps):
    for index, step in enumerate(steps):
        if step.startswith("Step "):
            label, text = step.split(": ", 1)
            print(f"\033[1m{label}:\033[0m {text}")
        else:
            print(step)
        if index < len(steps) - 1:
            print()


# Choice for SSO Help
print("You selected Single Sign-On Help.")
print()

# Select an option
print_bold("Please select an option:")
print()
print("1. I know my current password and want to reset it.")
print("2. I do not know my current password and need help resetting it.")
print("3. I need help setting up my account for the first time.")
print("4. What is SSO?")
print()
option = ask_question("Enter your choice (1-4): ")
print()

if option == "1":
    print_bold("To reset your password, please follow these steps:")
    print()
    print_steps([
        "Step 1: Open a web browser and go to password.uri.edu",
        'Step 2: Select "Reset using current password."',
        "Step 3: Enter your current credentials and follow the instructions to create a new password.",
    ])

elif option == "2":
    print_bold("Resetting a forgotten password")
    print()
    print("Join the URI IT Service Desk Zoom meeting at uri-edu.zoom.us for help resetting your password.")
    print()
    print("\033[1;3mNote:\033[0m\033[3m You must show a photo ID to verify your identity before your password can be reset.\033[0m")

elif option == "3":
    print_bold("Setting up your account for the first time")
    print()
    print("Before setting up your account, make sure you have been assigned a student ID number and URI email address.")
    print()
    print("If you have not received your student ID number or URI email address, allow time for them to be issued.")
    print("For questions about your enrollment status, contact Enrollment Services at 401-874-9500")
    print("Once you have your student ID number and URI email address, visit https://its.uri.edu/getting-started-students/ and follow the instructions to set up your account.")
    print()
    print("\033[1;3mNote:\033[0m\033[3m Your account may take 1-3 business days to become available after setup.\033[0m")

elif option == "4":
    print_bold("About SSO")
    print()
    print_steps([
        "SSO stands for Single Sign-On.",
        "It lets you sign in to multiple applications with one set of credentials.",
        "Your SSO password is separate from your Microsoft Authenticator PIN. For help setting up Microsoft Authenticator, select option 3 from the main menu.",
        "Use your SSO credentials to access e-Campus, Brightspace, and other URI applications.",
        "To check your email, sign in to gmail.com with your SSO credentials.",
        "\033[1;3mNote:\033[0m\033[3m You cannot access your URI email through Outlook.\033[0m",
    ])

else:
    print("Invalid response. Please select an option (1-4).")
