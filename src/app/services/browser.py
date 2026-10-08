import webbrowser

from src.app.main import BROWSER_PATH


class BrowserService:
    def __init__(self) -> None:
        if BROWSER_PATH:
            self._browser = webbrowser.get(f'"{BROWSER_PATH}" %s')
        else:
            self._browser = webbrowser.get()

    def open_page(self, page_id: str):
        url = f"{WIKIPEDIA_PATH}/w/index.php/?curid={page_id}"
        self._browser.open(url)
