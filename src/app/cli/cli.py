from src.app.services.browser import BrowserService
from src.app.services.request import RequestService


def menu(requests: RequestService, browser: BrowserService):
    while True:
        print("0. Exit")
        print("1. Write a request")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            user_input = input("Enter your request: ").strip()
            if user_input:
                results = requests.request(user_input)
                if results:
                    print(f"Suggested {len(results)} results:")
                    print("0. Exit")
                    for i, res in enumerate(results):
                        print(f"{i+1}. {res[1]}")
                    user_input = input("Enter your choice: ")
                    if user_input == "0":
                        continue
                    if user_input:
                        if user_input.isdigit() and 1 <= int(user_input) <= len(results):
                            page_id = results[int(user_input) - 1][0]
                            browser.open_page(page_id)
                        else:
                            print("Invalid choice.")
                    else:
                        print("Request cannot be empty.")
                else:
                    print("No results found.")
            else:
                print("Request cannot be empty.")
        else:
            print("Invalid choice.")
