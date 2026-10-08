import os

from dotenv import load_dotenv

from src.app.cli.cli import CLI
from src.app.services.browser import BrowserService
from src.app.services.request import RequestService

load_dotenv()

BROWSER_PATH = os.getenv("BROWSER_PATH")
WIKIPEDIA_PATH = os.getenv("WIKIPEDIA_PATH")


def main():
    print("Hello from cli-wiki!")
    request_service = RequestService(WIKIPEDIA_PATH)
    browser_service = BrowserService(BROWSER_PATH, WIKIPEDIA_PATH)
    try:
        CLI(request_service, browser_service).run()
    finally:
        request_service.close()


if __name__ == "__main__":
    main()
