# Choice for SSO Help 
print("You selected SSO Password Help.")
print()

#Ask user to select an option

option = input("Please select an option (1-4): ")
print()

print("Please select an option:")
print("1. I know my current SSO password and want to reset it.")   
print("2. I do not know my current SSO password and need help resetting it.")
print("3. I need help setting up my account for the first time.")
print("4. What is SSO?")

if option == "1": 
    print("To reset your SSO password, please follow these steps:")
    print()
    print("Step 1: Open a web browser and search for password.uri.edu.")
    print("Step 2: Click on reset using current password.")   
    print("Step 3: Enter your current credentials and follow the prompts to create your new password.")

elif option == "2":
    print("Please join the IT service desk zoom meeting at uri-edu.zoom.us for further assistance.")
    print("Note: You will need to show a form of photo id to verify your identity before resetting your password.")

elif option == "3":
    print("To set up your SSO account for the first time, please ensure that you have been assigned a student ID number and have created your e-campus account.")
    print("If you have not done so refer to step 1 on the getting started page linked below.")
    print("Please visit https://its.uri.edu/getting-started-students/ to set up your account.")
    print("Note: After you have set up your account, it will be ready for use in 1-3 business days.")
    
elif option == "4":
    print("Here is some general information about SSO:")
    print("SSO stands for Single Sign-On.")
    print("It allows you to access multiple applications with a single set of credentials.")
    print("Your SSO password is separate from your Microsoft Authenticator pin. *Select option 3 on the main menu for help with Microsoft Authenticator.")
    print("SSO also allows you to access e-Campus, brightspace, and other URI applications.")
    print("In order to check your email you will need to sign in to gmail.com with your SSO credentials.")
    print("Note: You will not be able to use outlook to access your emails.")
    print("If you are a current student, faculty, or staff member you have free acess to Microsoft Office 365 by loging in with your SSO credentials.")

else:
    print("Invalid response. Please select an option (1-4).")
