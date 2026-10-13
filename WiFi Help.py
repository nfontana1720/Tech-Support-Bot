# Helper functions for yes/no choices and text operations made by GitHub Copilot
def normalize_text(value):
    return str(value).strip().lower()


def is_yes(value):
    return normalize_text(value) in {"yes", "y", "yeah", "yep"}


def is_no(value):
    return normalize_text(value) in {"no", "n", "nah", "nope"}


def is_not_sure(value):
    return normalize_text(value) in {"not sure", "unsure", "maybe", "idk", "i don't know"}


def print_question_spacing():
    print("\n\n\n", end="")


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


def handle_wifi_follow_up(worked, setup_steps, vpn_action):
    if is_yes(worked):
        print("Great! Your device is now connected to the network.")
        print()
        return
    elif is_no(worked):
        print("Please make sure that your settings are up to date and that you are NOT using a VPN.")
        print()
    else:
        print("Invalid response. Please answer Yes or No.")
        print()

    print_question_spacing()
    vpn_check = ask_question("Are you using a VPN? (Yes/No/Not Sure): ")
    print()

    if is_yes(vpn_check) or is_not_sure(vpn_check):
        print(vpn_action)
        print_question_spacing()
        steps = ask_question("Would you like to see the previous steps? (Yes/No): ")
        print()
        if is_yes(steps):
            print_steps(setup_steps)

        print_question_spacing()
        vpn_worked = ask_question("Did this fix your Wi-Fi issue? (Yes/No): ")
        print()
        if is_yes(vpn_worked):
            print("Great! Your device is now connected to the network.")
            print()
            return
        elif not is_no(vpn_worked):
            print("Invalid response. Please answer Yes or No.")
            print()


# Choice for Wi-Fi Help 
print("You selected Wi-Fi Issues.")
print()

# Select Device Type
print_bold("Please select your device type:")
print()
print("1. Windows")
print("2. MacOS")    
print("3. Android")
print("4. iPhone & iPad")
print("5. Other")
print()
device_type = normalize_text(ask_question("Enter your choice: "))
print()
wifi_before = None
if device_type in {
    "windows", "1", "window", "windows 11",
    "macos", "mac", "2", "mac os", "macbook", "apple computer",
    "android", "3", "samsung", "Samsgung",
    "4", "iphone", "ipad", "apple", "ios",
}:
    wifi_before = ask_question("Have you connected to URI_Secure on this device before? (Yes/No): ")
    print()
print()
print()

# How to troubleshoot Wi-Fi issues for Windows
if device_type in {"windows", "1", "window", "windows 11"}:
    previous_connection_steps = [
        "Step 1: Open system settings.",
        "Step 2: Search for Manage User Certificates.",
        "Step 3: Click on Personal, then Certificates.",
        "Step 4: Delete any certificates that say URI using the red X icon on the top of the window.",
        "Step 5: Try connecting using the previous steps.",
    ]
    setup_steps = [
        "Step 1: Join the temporary setup network called URI_Open.",
        "Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.",
        "Step 3: Select download.exe for Windows and open the file.",
        "Step 4: Open the Cloudpath installer to install the certificate.",
        "Step 5: Once the certificate is installed, open Wi-Fi settings and connect to URI_Secure.",
    ]
    if is_yes(wifi_before):
        print_steps(previous_connection_steps)
        print_question_spacing()
    print_bold("Connecting Windows to URI_Secure")
    print()
    print_steps(setup_steps)

    print_question_spacing()
    worked = ask_question("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()
    handle_wifi_follow_up(
        worked,
        setup_steps,
        "Please fully uninstall the VPN from your system files and try connecting using the previous steps.",
    )

# How to troubleshoot Wi-Fi issues for MacOS
elif device_type in {"macos", "mac", "2", "mac os", "macbook", "apple computer"}:
    previous_connection_steps = [
        "Step 1: Open system settings.",
        "Step 2: Search for VPN & Device Management.",
        "Step 3: Click on Profiles.",
        "Step 4: Delete any profiles that say URI; Enter your computer password when prompted.",
        "Step 5: Try connecting using the previous steps.",
    ]
    setup_steps = [
        "Step 1: Join the temporary setup network called URI_Open.",
        "Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.",
        "Step 3: Select download for MacOS, open the file in downloads, and allow the profile download.",
        "Step 4: Open system settings and search for VPN & Device Management.",
        "Step 5: Under profile downloads, double click the profile and select install; Enter your device password when prompted.",
        "Step 6: Open Wi-Fi settings and connect to URI_Secure.",
    ]
    if is_yes(wifi_before):
        print_steps(previous_connection_steps)
        print_question_spacing()
    print_bold("Connecting MacOS to URI_Secure")
    print()
    print_steps(setup_steps)

    print_question_spacing()
    worked = ask_question("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()
    handle_wifi_follow_up(
        worked,
        setup_steps,
        "Please fully uninstall the VPN from VPN settings and try connecting using the previous steps.",
    )

# How to troubleshoot Wi-Fi issues for Android
elif device_type in {"android", "3", "samsung", "Samsgung", "Android"}:
    previous_connection_steps = [
        "Step 1: Open your Wi-Fi settings.",
        "Step 2: Tap and hold URI_Secure, then select Forget network.",
        "Step 3: Try connecting using the previous steps.",
    ]
    setup_steps = [
        "Step 1: Join the temporary setup network called URI_Open and turn off MAC address randomization.",
        "Step 2: Open the play store and download the cloudpath app.",
        "Step 3: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.",
        "Step 4: After logging in, select download for Android and allow the certificate download through cloudpath.",
        "Step 5: Once cloudpath confirms that the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.",
    ]
    if is_yes(wifi_before):
        print_steps(previous_connection_steps)
        print_question_spacing()
    print_bold("Connecting Android to URI_Secure")
    print()
    print_steps(setup_steps)

    print_question_spacing()
    worked = ask_question("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()
    handle_wifi_follow_up(
        worked,
        setup_steps,
        "Please fully uninstall the VPN from VPN settings and try connecting using the previous steps.",
    )

# How to troubleshoot Wi-Fi issues for iPhone & iPad
elif device_type in {"4", "iphone", "ipad", "apple", "ios"}:
    previous_connection_steps = [
        "Step 1: Open system settings.",
        "Step 2: Search for VPN & Device Management.",
        "Step 3: Click on Profiles.",
        "Step 4: Delete any profiles that say URI; Enter your computer password when prompted.",
        "Step 5: Try connecting using the previous steps.",
    ]
    setup_steps = [
        "Step 1: Join the temporary setup network called URI_Open.",
        "Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.",
        "Step 3: Select download for iPhone or iPad and allow the profile download.",
        "Step 4: Open system settings and search for VPN & Device Management.",
        "Step 5: Under profile downloads, double click the profile and select install; Enter your device password when prompted.",
        "Step 6: Once the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.",
    ]
    if is_yes(wifi_before):
        print_steps(previous_connection_steps)
        print_question_spacing()
    print_bold("Connecting iPhone & iPad to URI_Secure")
    print()
    print_steps(setup_steps)

    print_question_spacing()
    worked = ask_question("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()
    handle_wifi_follow_up(
        worked,
        setup_steps,
        "Please fully uninstall the VPN from VPN settings and try connecting using the previous steps.",
    )

# How to troubleshoot Wi-Fi issues for Other Devices
elif device_type in {"other", "5", "other device", "other devices"}:
    setup_steps = [
        "Step 1: Go to rhodywifi.uri.edu using a different device that is already connected to the university wi-fi.",
        "Step 2: Click on Register a Device and log in with your URI account.",
        "Step 3: Click on Create a Device and select your device type from the drop down menu.",
        "Step 4: Locate your device's MAC address and enter it in the webpage.",
        "Step 5: Select create device and restart or unplug the device you want to register.",
        "Step 6: Once the device is restarted, open Wi-Fi settings and connect to URI_Open.",
    ]
    print_steps(setup_steps)
    print()
    print("\033[1;3mNote:\033[0m\033[3m Devices registered this way will only be able to connect to URI_Open, but it will work the same as URI_Secure for the device.\033[0m")

    print_question_spacing()
    worked = ask_question("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()
    if is_yes(worked):
        print("Great! Your device is now connected to the network.")
        print()
    elif is_no(worked):
        print("Please try restarting your device or contact the URI IT Service Desk for further assistance.")
        print()
    else:
        print("Invalid response. Please answer Yes or No.")
        print()

else:
    print("Invalid response. Please select your device type:")
    print()  