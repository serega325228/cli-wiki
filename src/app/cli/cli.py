from src.app.services.browser import BrowserService
from src.app.services.request import RequestService, RequestServiceError


class CLI:
    def __init__(self, requests: RequestService, browser: BrowserService) -> None:
        self._requests = requests
        self._browser = browser

    def run(self) -> None:
        while True:
            self._show_menu()
            try:
                choice = input("Enter your choice: ").strip()
                if choice == "0":
                    return
                if choice == "1":
                    self._search_and_open()
                else:
                    print("Invalid choice.")
            except (EOFError, KeyboardInterrupt):
                print("\nExiting.")
                return

    def _show_menu(self) -> None:
        print("0. Exit")
        print("1. Write a request")

    def _search_and_open(self) -> None:
        query = input("Enter your request: ").strip()
        if not query:
            print("Request cannot be empty.")
            return

        try:
            results = self._requests.request(query)
        except RequestServiceError as error:
            print(f"Search failed: {error}")
            return

        if not results:
            print("No results found.")
            return

        print(f"Suggested {len(results)} results:")
        print("0. Back")
        for index, (_, title) in enumerate(results, start=1):
            print(f"{index}. {title}")

        choice = input("Enter your choice: ").strip()
        if choice == "0":
            return
        if not choice.isdigit() or not 1 <= int(choice) <= len(results):
            print("Invalid choice.")
            return

        page_id = results[int(choice) - 1][0]
        try:
            if not self._browser.open_page(page_id):
                print("Could not open the selected page in a browser.")
        except (RuntimeError, ValueError) as error:
            print(f"Could not open the selected page: {error}")
