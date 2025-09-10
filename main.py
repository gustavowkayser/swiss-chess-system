import sys
from app.manager import App

def main():
    app = App()

    function = sys.argv[1]
    arguments = sys.argv[2:]

    app.execute(function, *arguments)

if __name__ == "__main__":
    main()