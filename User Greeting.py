import shutil
import textwrap


# Title screen
def ask_question(question):
    print(f"\033[1m{question}\033[0m", end="")
    return input()


def print_welcome_banner():
    title = "WELCOME TO TECH SUPPORT"
    subtitle = "Your guide to technology at URI"
    terminal_width = max(1, shutil.get_terminal_size(fallback=(80, 24)).columns)
    banner_width = min(64, terminal_width)

    if banner_width < 8:
        for line in textwrap.wrap(title, width=banner_width):
            print(f"\033[1;36m\033[1m{line}\033[0m")
        for line in textwrap.wrap(subtitle, width=banner_width):
            print(line)
        return

    inner_width = banner_width - 4
    title_lines = textwrap.wrap(title, width=inner_width)
    subtitle_lines = textwrap.wrap(subtitle, width=inner_width)
    border = "+" + "=" * (banner_width - 2) + "+"
    left_padding = (terminal_width - banner_width) // 2

    print()
    print(" " * left_padding + border)
    print(" " * left_padding + "|" + " " * (banner_width - 2) + "|")
    for line in title_lines:
        centered_title = line.center(inner_width)
        print(
            " " * left_padding
            + f"| \033[1;36m\033[1m{centered_title}\033[0m |"
        )
    for line in subtitle_lines:
        print(" " * left_padding + f"| {line.center(inner_width)} |")
    print(" " * left_padding + "|" + " " * (banner_width - 2) + "|")
    print(" " * left_padding + border)
    print()


print_welcome_banner()
print("How can we help you today?")
print()
print("1. Wi-Fi connection help")
print("2. Single Sign-On (SSO) help")
print("3. Microsoft Authenticator help")
print("4. e-Campus help")
print("5. IT Help Desk contact information")
print()
choice = ask_question("Enter your choice (1-5): ")