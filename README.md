# CLI Wiki

Search Wikipedia from a terminal and open a selected result in your browser.

## Run

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
uv run python -m src.app.main
```

Choose `1`, enter a search phrase, then select a result. Choose `0` to exit or go back.

Optional `.env` settings:

```env
WIKIPEDIA_PATH=https://ru.wikipedia.org
BROWSER_PATH=/path/to/browser
```

`BROWSER_PATH` is optional; the system default browser is used if it is unset or the path does not exist.

## Main components

- `main()` loads `.env`, configures services, runs the CLI, and closes the HTTP client.
- `CLI.run()` handles prompts, search, and result selection.
- `RequestService.request()` queries Wikipedia and formats results as page IDs and titles.
- `BrowserService.open_page()` opens a selected page in the configured wiki and browser.

## Русский

Поиск по Википедии из терминала с открытием выбранной статьи в браузере.

### Запуск

Нужны Python 3.14+ и [uv](https://docs.astral.sh/uv/).

```sh
uv sync
uv run python -m src.app.main
```

Выберите `1`, введите запрос и номер результата. `0` — выход или возврат.

Необязательные настройки в `.env`:

```env
WIKIPEDIA_PATH=https://ru.wikipedia.org
BROWSER_PATH=/путь/к/браузеру
```

Если `BROWSER_PATH` не задан или путь не существует, используется браузер системы по умолчанию.

### Основные компоненты

- `main()` загружает `.env`, настраивает сервисы, запускает CLI и закрывает HTTP-клиент.
- `CLI.run()` обрабатывает ввод, поиск и выбор результата.
- `RequestService.request()` ищет статьи в Википедии и возвращает их ID и названия.
- `BrowserService.open_page()` открывает выбранную статью в настроенной Википедии и браузере.
