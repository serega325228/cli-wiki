import json

import httpx


class RequestServiceError(Exception):
    pass


class RequestService:
    def __init__(self, wikipedia_url: str | None = None) -> None:
        path = wikipedia_url or "https://ru.wikipedia.org"
        self._client = httpx.Client(
            base_url=path.rstrip("/"),
            headers={
                "User-Agent": "cli-wiki/1.0 (skarbach@mail.ru)",
                "Accept": "application/json",
            },
            timeout=10,
        )

    def fetch_url(self, url: str, query_params: dict | None = None) -> dict:
        if not url:
            raise ValueError("URL is required")
        try:
            res = self._client.get(url, params=query_params)
            res.raise_for_status()
            return res.json()
        except httpx.HTTPError as error:
            raise RequestServiceError(f"Wikipedia request failed: {error}") from error
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            raise RequestServiceError("Wikipedia returned invalid JSON") from error

    def request(self, user_input: str) -> list[tuple[int, str]]:
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
        return self.format_request(res)

    def format_request(self, result: dict) -> list[tuple[int, str]]:
        try:
            search_results = result["query"]["search"]
            if not isinstance(search_results, list):
                raise TypeError("search results are not a list")
            formatted_results = []
            for item in search_results:
                page_id = item["pageid"]
                title = item["title"]
                if not isinstance(page_id, int) or not isinstance(title, str):
                    raise TypeError("search result has invalid field types")
                formatted_results.append((page_id, title))
            return formatted_results
        except (KeyError, TypeError) as error:
            raise RequestServiceError(
                "Wikipedia returned an unexpected search response"
            ) from error

    def close(self) -> None:
        self._client.close()
