# Helper functions for yes/no choices made by GitHub Copilot
def normalize_text(value):
    return str(value).strip().lower()


def is_yes(value):
    return normalize_text(value) in {"yes", "y", "yeah", "yep"}


def is_no(value):
    return normalize_text(value) in {"no", "n", "nah", "nope"}


def is_not_sure(value):
    return normalize_text(value) in {"not sure", "unsure", "maybe", "idk", "i don't know"}

# Choice for Wi-Fi Help 
print("You selected Wi-Fi Issues.")
print()

# Select Device Type
print("Please select your device type:")
print()
print("1. Windows")
print("2. MacOS")    
print("3. Android")
print("4. iPhone & iPad")
print("5. Other")
print()
device_type = normalize_text(input("Enter your choice: "))
print()
print()
print()

# How to troubleshoot Wi-Fi issues for Windows
if device_type in {"windows", "1", "window", "windows 11"}:
    print("Step 1: Join the temporary setup network called URI_Open.")
    print()
    print("Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
    print()
    print("Step 3: Select download.exe for Windows and open the file")
    print()
    print("Step 4: Open the Cloudpath installer to install the certificate.")
    print()
    print("Step 5: Once the certificate is installed, open Wi-Fi settings and connect to URI_Secure.")
    print()
    print()
    print()
    
    worked = input("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()
    
    if is_no(worked):
        print("Please make sure that your settings are up to date and that you are NOT using a VPN such as McAfee.")
        print()
        
# How to remove a VPN on Windows
        print()
        print()
        vpn_check = input("Are you using a VPN? (Yes/No/Not Sure): ")
        print()

        if is_yes(vpn_check) or is_not_sure(vpn_check):
            print("Please fully uninstall the VPN from your system files and try connecting using the previous steps.")
            print()
            print()
            print()

            steps = input("Would you like to see the previous steps? (Yes/No): ")
            print()

            if is_yes(steps):
                print("Step 1: Join the temporary setup network called URI_Open.")
                print()
                print("Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
                print()
                print("Step 3: Select download.exe for Windows and open the file.")
                print()
                print("Step 4: Open the Cloudpath installer to install the certificate.")
                print()
                print("Step 5: Once the certificate is installed, open Wi-Fi settings and connect to URI_Secure.")
                print()

# How to remove a certificate on Windows
        elif is_no(vpn_check):
            print()
            print()
            wifi_before = input("Have you connected to URI_Secure on this device before? (Yes/No): ")
            print()

            if is_yes(wifi_before):
                print("Step 1: Open system settings.")
                print()
                print("Step 2: Search for Manage User Certificates.")
                print()
                print("Step 3: Click on Personal, then Certificates.")
                print()
                print("Step 4: Delete any certificates that say URI using the red X icon on the top of the window.")
                print()
                print("Step 5: Try connecting using the previous steps.")
                print()
                print()
                print()

                steps = input("Would you like to see the previous steps? (Yes/No): ")
                print()

                if is_yes(steps):
                    print("Step 1: Join the temporary setup network called URI_Open.")
                    print()
                    print("Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
                    print()
                    print("Step 3: Select download.exe for Windows and open the file")
                    print()
                    print("Step 4: Open the Cloudpath installer to install the certificate.")
                    print()
                    print("Step 5: Once the certificate is installed, open Wi-Fi settings and connect to URI_Secure.")
                    print()

            elif is_no(wifi_before):
                print("Please contact the URI IT Help Desk for further assistance.")
                print()

    elif is_yes(worked):
        print("Great! Your device is now connected to URI_Secure.")
        print()

# How to troubleshoot Wi-Fi issues for MacOS
elif device_type in {"macos", "mac", "2", "mac os", "macbook", "apple computer"}:
    print("Step 1: Join the temporary setup network called URI_Open.")
    print()
    print("Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
    print()
    print("Step 3: Select download for MacOS and allow the profile download.")
    print()
    print("Step 4: Open system settings and search for VPN & Device Management.")
    print()
    print("Step 5: Once the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.")
    print()
    print("Step 6: Double click the profile and select install; Enter your computer password when prompted.")
    print()
    print("Step 7: Open Wi-Fi settings and connect to URI_Secure.")
    print()
    print()
    print()

    worked = input("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()

    if is_no(worked):
        print("Please make sure that your settings are up to date and that you are NOT using a VPN.")
        print()

# How to remove a VPN on MacOS
        print()
        print()
        vpn_check = input("Are you using a VPN? (Yes/No/Not Sure): ")
        print()

        if is_yes(vpn_check) or is_not_sure(vpn_check):
            print("Please fully uninstall the VPN from VPN settings and try connecting using the previous steps.")
            print()
            print()
            print()

            steps = input("Would you like to see the previous steps? (Yes/No): ")
            print()

            if is_yes(steps):
                print("Step 1: Join the temporary setup network called URI_Open.")
                print()
                print("Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
                print()
                print("Step 3: Select download for MacOS and allow the profile download.")
                print()
                print("Step 4: Open system settings and search for VPN & Device Management.")
                print()
                print("Step 5: Once the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.")
                print()
                print("Step 6: Double click the profile and select install; Enter your computer password when prompted.")
                print()
                print("Step 7: Open Wi-Fi settings and connect to URI_Secure.")
                print()

        elif is_no(vpn_check):
            print()
            print()
            wifi_before = input("Have you connected to URI_Secure on this device before? (Yes/No): ")
            print()
            
# How to remove a profile on MacOS
            if is_yes(wifi_before):
                print("Step 1: Open system settings")
                print()
                print("Step 2: Search for VPN & Device Management")
                print()
                print("Step 3: Click on Profiles")
                print()
                print("Step 4: Delete any profiles that say URI; Enter your computer password when prompted.")
                print()
                print("Step 5: Try connecting using the previous steps.")
                print()
                print()
                print()

                steps = input("Would you like to see the previous steps? (Yes/No): ")
                print()

                if is_yes(steps):
                    print("Step 1: Join the temporary setup network called URI_Open.")
                    print()
                    print("Step 2: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
                    print()
                    print("Step 3: Select download for MacOS and allow the profile download.")
                    print()
                    print("Step 4: Open system settings and search for VPN & Device Management.")
                    print()
                    print("Step 5: Once the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.")
                    print()
                    print("Step 6: Double click the profile and select install; Enter your computer password when prompted.")
                    print()
                    print("Step 7: Open Wi-Fi settings and connect to URI_Secure.")
                    print()

            elif is_no(wifi_before):
                print("Please contact the URI IT Help Desk for further assistance.")
                print()

    elif is_yes(worked):
        print("Great! Your device is now connected to URI_Secure.")
        print()

    else:
        print("Invalid response. Please answer Yes or No.")
        print()

# How to troubleshoot Wi-Fi issues for Android
elif device_type in {"android", "3", "samsung", "Samsgung", "Android"}:
    print("Step 1: Join the temporary setup network called URI_Open and turn off MAC address randomization.")
    print()
    print("Step 2: Open the play store and download the cloudpath app.")
    print()
    print("Step 3: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
    print()
    print("Step 4: After logging in, select download for Android and allow the certificate download through cloudpath.")
    print()
    print("Step 5: Once cloudpath confirms that the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.")
    print()
    print()
    print()

    worked = input("Did this fix your Wi-Fi issue? (Yes/No): ")
    print()

    if is_no(worked):
        print("Please make sure that your settings are up to date and that you are NOT using a VPN.")
        print()

# How to remove a VPN on Android
        print()
        print()
        vpn_check = input("Are you using a VPN? (Yes/No/Not Sure): ")
        print()

        if is_yes(vpn_check) or is_not_sure(vpn_check):
            print("Please fully uninstall the VPN from VPN settings and try connecting using the previous steps.")
            print()
            print()
            print()

            steps = input("Would you like to see the previous steps? (Yes/No): ")
            print()

            if is_yes(steps):
                print("Step 1: Join the temporary setup network called URI_Open and turn off MAC address randomization.")
                print()
                print("Step 2: Open the play store and download the cloudpath app.")
                print()
                print("Step 3: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
                print()
                print("Step 4: After logging in, select download for Android and allow the certificate download through cloudpath.")
                print()
                print("Step 5: Once cloudpath confirms that the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.")
                print()

        elif is_no(vpn_check):
            print()
            print()
            wifi_before = input("Have you connected to URI_Secure on this device before? (Yes/No): ")
            print()

# How to remove a certificate on Android
            if is_yes(wifi_before):
                print("Step 1: Open your Wi-Fi settings.")
                print()
                print("Step 2: Tap and hold URI_Secure, then select Forget network.")
                print()
                print("Step 3: Try connecting using the previous steps.")
                print()
                print()
                print()
            
                steps = input("Would you like to see the previous steps? (Yes/No): ")
                print()

                if is_yes(steps):
                    print("Step 1: Join the temporary setup network called URI_Open and turn off MAC address randomization.")
                    print()
                    print("Step 2: Open the play store and download the cloudpath app.")
                    print()
                    print("Step 3: Open a web browser (not Chrome) and search for wifi.uri.edu and log in with your URI account.")
                    print()
                    print("Step 4: After logging in, select download for Android and allow the certificate download through cloudpath.")
                    print()
                    print("Step 5: Once cloudpath confirms that the certificate is installed, open your Wi-Fi settings and connect to URI_Secure.")
                    print()

            elif is_no(wifi_before):
                print("Please contact the URI IT Help Desk for further assistance.")
                print()

    elif is_yes(worked):
        print("Great! Your device is now connected to URI_Secure.")
        print()

    else:
        print("Invalid response. Please answer Yes or No.")
        print()