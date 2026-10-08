import json

import httpx

from src.app.main import WIKIPEDIA_PATH


class RequestService:
    def __init__(self):
        path = WIKIPEDIA_PATH or "https://ru.wikipedia.org"
        self._client = httpx.Client(
            base_url=path,
            headers={
                "User-Agent": "cli-wiki/1.0 (skarbach@mail.ru)",
                "Accept": "application/json",
            },
            timeout=10,
        )

    def fetch_url(self, url: str, query_params: dict | None = None):
        if not url:
            raise ValueError("URL is required")
        try:
            res = self._client.get(url, params=query_params)
            res.raise_for_status()
            return res.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error: {e}")
            return
        except httpx.RequestError as e:
            print(f"Network or request error: {e}")
            return
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return

    def request(self, user_input: str) -> list:
        if not user_input:
            raise ValueError("User input is required")
        url = "/w/api.php"
        query_params = {
            "action": "query",
            "list": "search",
            "utf8": "",
            "format": "json",
            "srsearch": user_input,
        }
        res = self.fetch_url(url, query_params)
        if res:
            return self.format_request(res)
        return []

    def format_request(self, result: dict) -> list:
        return [(item["pageid"], item["title"]) for item in result["query"]["search"]]

    def close(self):
        self._client.close()
