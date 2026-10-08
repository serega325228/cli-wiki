import os

from dotenv import load_dotenv

from src.app.cli.cli import menu
from src.app.services import browser
from src.app.services.request import RequestService

load_dotenv()

BROWSER_PATH = os.getenv("BROWSER_PATH")
WIKIPEDIA_PATH = os.getenv("WIKIPEDIA_PATH")


def main():
    print("Hello from cli-wiki!")
    request_service = RequestService()
    browser_service = browser.BrowserService()
    menu(request_service, browser_service)
    request_service.close()


if __name__ == "__main__":
    main()
