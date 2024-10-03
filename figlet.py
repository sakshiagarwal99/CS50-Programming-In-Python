import sys
import random
from pyfiglet import Figlet

def main():
    font = get_font()
    render_text(font)

def get_font():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        return random.choice(fonts)

    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            return sys.argv[2]
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

def render_text(font):
    figlet = Figlet()
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
