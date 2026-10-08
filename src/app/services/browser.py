import webbrowser
from pathlib import Path
from urllib.parse import urlsplit


class BrowserService:
    def __init__(
        self,
        browser_path: str | None = None,
        wikipedia_url: str | None = None,
    ) -> None:
        try:
            if browser_path and Path(browser_path).exists():
                self._browser = webbrowser.get(f'"{browser_path}" %s')
            else:
                self._browser = webbrowser.get()
        except (webbrowser.Error, OSError) as error:
            raise RuntimeError(f"Could not initialize browser: {error}") from error
        self._wikipedia_url = (wikipedia_url or "https://ru.wikipedia.org").rstrip("/")

    def open_page(self, page_id: int | str) -> bool:
        page_id = str(page_id)
        if not page_id.isdigit():
            raise ValueError("Page ID must be numeric")
        return self.open_url(f"{self._wikipedia_url}/w/index.php?curid={page_id}")

    def open_url(self, url: str) -> bool:
        parsed_url = urlsplit(url)
        if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
            raise ValueError("Enter a valid HTTP or HTTPS URL")
        try:
            return self._browser.open(url)
        except (webbrowser.Error, OSError) as error:
            raise RuntimeError(f"Browser could not open {url}: {error}") from error
