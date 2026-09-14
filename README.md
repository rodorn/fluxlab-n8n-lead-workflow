# Lead & Deal Watcher, n8n Template

Cyklicznie pobiera nowe pozycje ze źródła (HTTP/API/RSS-as-JSON), normalizuje je,
odfiltrowuje istotne, ocenia je modelem AI (relevance score 0-100), zapisuje do
Google Sheets (upsert, bez duplikatów) i wysyła powiadomienie o najgorętszych
trafieniach na Discord/Slack.

## Co robi (9 node'ów)

1. **Every Hour**, Schedule Trigger, uruchamia pipeline co godzinę.
2. **Fetch Source**, HTTP GET do dowolnego źródła JSON (domyślnie demo: Hacker News Algolia API, bez auth).
3. **Normalize**, Code (JS): spłaszcza payload do jednego czystego itemu na wiersz. TU adaptujesz template do swojego źródła.
4. **Filter Relevant**, odrzuca pozycje bez URL / poniżej progu.
5. **AI Score (HTTP)**, generyczny POST do endpointu OpenAI-compatible; zwraca `{score, reason}`.
6. **Merge Score**, Code (JS): dokleja score + reason, liczy tier HOT/WARM/COLD.
7. **Save to Google Sheets**, upsert po kolumnie `id` (re-run nie duplikuje).
8. **Only HOT**, przepuszcza tylko `tier == HOT`.
9. **Notify Discord**, POST na webhook Discord/Slack.

## Import do n8n

1. n8n → **Workflows** → prawy górny róg → **Import from File** (albo `...` → _Import from File_).
2. Wskaż `workflow.json`.
3. Workflow pojawi się jako nowy, nieaktywny. Ustaw credentiale (niżej), potem **Active**.

Alternatywnie: **Import from URL** albo wklej zawartość przez _Import from Clipboard_.

## Credentiale do ustawienia

| Node                  | Typ credentiala          | Co ustawić                                                                                             |
| --------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ |
| AI Score (HTTP)       | **Header Auth**          | Name: `Authorization`, Value: `Bearer <TWÓJ_API_KEY>`. Podepnij pod pole _Credential to connect with_. |
| Save to Google Sheets | **Google Sheets OAuth2** | Zaloguj konto Google, nadaj dostęp do arkuszy.                                                         |

Placeholdery `REPLACE_WITH_YOUR_CREDENTIAL_ID` w JSON znikną, gdy w UI wybierzesz
własny credential z listy, nie edytuj ich ręcznie w pliku.

## Konfiguracja bez grzebania w kodzie (n8n Variables)

W **Settings → Variables** (n8n) ustaw:

- `SOURCE_URL`, Twój endpoint źródłowy (nadpisuje demo HN).
- `DISCORD_WEBHOOK_URL`, webhook Discord (lub Slack).

Node'y czytają je przez `{{ $vars.SOURCE_URL }}` / `{{ $vars.DISCORD_WEBHOOK_URL }}`.
Na darmowym self-hosted bez zmiennych, po prostu wpisz URL-e wprost w polach node'ów.

## Google Sheet, nagłówki

W arkuszu (zakładka `Sheet1`) pierwszy wiersz musi zawierać kolumny:

```
id | title | url | aiScore | tier | aiReason | fetchedAt
```

Wklej ID arkusza (z URL: `docs.google.com/spreadsheets/d/<TU_ID>/edit`) do node'a Save to Google Sheets.

## Jak dostosować do własnego źródła

1. Zmień `SOURCE_URL` (lub URL w **Fetch Source**). Dodaj auth, jeśli API tego wymaga.
2. W **Normalize** popraw mapowanie pól, to jedyne miejsce zależne od źródła.
3. W **Filter Relevant** ustaw próg (`points >= 5` → własna reguła).
4. Chcesz inny model / dostawcę? W **AI Score** podmień URL i `model` (Anthropic, OpenRouter, Groq, lokalny LLM). Nie potrzebujesz AI? Usuń node i licz score regułą w **Normalize**.
5. Slack zamiast Discord? Ten sam node, body zmień na `{ text: ... }` i wklej Slack Incoming Webhook.

## Wymagania

- n8n `>= 1.30` (self-hosted lub Cloud). Wszystkie node'y to core-nodes, bez community packages.
- Konto Google (dla Sheets) i klucz API modelu (dla AI Score), oba opcjonalne, jeśli wytniesz odpowiednie node'y.

## Koszt uruchomienia

Demo działa za darmo (HN API + darmowy tier n8n). Jedyny płatny element to wywołania
modelu w AI Score, kontroluj je progiem w **Filter Relevant**.


---

## O autorze / About

Zbudowane przez Pawła Iwanka, **FluxLab**, automatyzacja procesów biznesowych i wdrożenia AI dla małych firm.

Strona: https://fluxlab.pl

Potrzebujesz podobnej automatyzacji na zamówienie? Napisz przez https://fluxlab.pl
