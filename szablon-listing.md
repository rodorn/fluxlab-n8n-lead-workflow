# Listing szablonu (do sprzedaży)

## Nazwa

**AI Lead & Deal Watcher, Fetch, Score, Save & Notify**

## Krótki opis (tagline)

Auto-monitor any source, let AI score every item, log it to Google Sheets, and get pinged only about the hot ones.

## Opis pełny (marketplace / gumroad / n8n creator)

Stop refreshing tabs and copy-pasting into spreadsheets. This ready-to-import n8n
workflow polls any JSON source (API, RSS-to-JSON, or a website's feed) on a schedule,
normalizes the data, filters out the noise, and asks an AI model to score each item
0-100 for how relevant it is to you. Everything lands in a Google Sheet as a clean,
de-duplicated log (append-or-update, so re-runs never create duplicate rows), and the
highest-scoring hits are pushed straight to your Discord or Slack.

It's a complete, production-shaped pipeline, 9 connected nodes with inline notes on
every step, not a two-node demo. Swap the source URL and one field-mapping block and
it works for leads, job posts, marketplace deals, competitor news, RFPs, real-estate
listings, or any feed you care about.

**What you get**

- Importable `workflow.json` (core nodes only, no community packages to install)
- Step-by-step README: import, credentials, and how to point it at your own source
- Works with any OpenAI-compatible model (OpenAI, Anthropic, OpenRouter, Groq, local LLM)
- Free demo source included (Hacker News API) so you can run it in 2 minutes

**Setup time:** ~10 minutes. **Skill level:** beginner-friendly.

## Dla kogo

- Freelancerzy i agencje śledzące leady / RFP / oferty pracy
- Resellerzy i arbitraż (monitoring okazji na marketplace)
- Zespoły sales/marketing chcące AI-scoring bez pisania kodu
- Każdy, kto ręcznie kopiuje dane ze stron do arkusza

## Cena

**$24** (widełki $19–$29). Sugestia: $19 launch/promo, $24 standard, $29 z wsparciem/aktualizacjami.

## Tagi

`n8n` `automation` `lead-generation` `ai` `openai` `google-sheets` `discord` `slack`
`web-scraping` `rss` `no-code` `data-pipeline` `notifications` `crm`

## Screenshot / demo (do podstawienia)

- Zrzut canvasu 9 node'ów z n8n
- Krótki GIF: trigger → wiersze w Sheecie → ping na Discordzie
- Link do demo/loom: `<REPLACE_WITH_DEMO_LINK>`

---

# Szablon 2

## Nazwa

**Price Drop Monitor, Track Any Product & Get Alerted on Real Price Drops**

## Krótki opis (tagline)

Watch prices from any source, remember the last run, and get pinged the moment something actually drops.

## Opis pełny (marketplace / gumroad / n8n creator)

Most "price tracker" workflows just re-post the current price. This one is stateful: it
polls any JSON price source on a schedule, compares each product against the previous run
stored in a Google Sheet, computes the exact percentage change, tracks the all-time low,
and only alerts you when a price actually falls past your threshold (default 10%). Every
product's current price is written back to the sheet, so the next run has a fresh baseline,
no database required. Alerts go to Discord or Slack and, optionally, straight to your inbox
over SMTP.

It is a complete, production-shaped pipeline, 9 connected nodes with inline notes on every
step. Swap the source URL and one field-mapping block and it tracks e-commerce products,
marketplace listings, competitor pricing, flights, subscriptions, or any feed with a price.

**What you get**

- Importable `workflow-2-price-drop-monitor.json` (core nodes only, no community packages)
- Stateful comparison via Google Sheets, no external database
- Percentage-change and all-time-low logic already written for you
- Two alert channels: Discord/Slack webhook and SMTP email
- Free demo source included (dummyjson.com) so you can run it in minutes

**Setup time:** ~10 minutes. **Skill level:** beginner-friendly.

## Dla kogo

- Resellerzy i arbitraż (spadki cen na marketplace)
- E-commerce i zespoły pricingu (monitoring konkurencji)
- Kupujący czekający na promocję konkretnego produktu
- Każdy, kto ręcznie odświeża strony w poszukiwaniu przeceny

## Cena

**$29** (widełki $24 do $34). Wyższa niż szablon 1, bo logika jest stateful (porównanie,
minimum historyczne) i dochodzi drugi kanał alertów. Sugestia: $24 launch/promo, $29 standard,
$34 z wsparciem/aktualizacjami.

## Tagi

`n8n` `automation` `price-monitoring` `price-drop` `alerts` `google-sheets` `discord` `slack`
`email` `web-scraping` `ecommerce` `no-code` `data-pipeline` `stateful`

## Screenshot / demo (do podstawienia)

- Zrzut canvasu 9 node'ów z n8n
- Krótki GIF: trigger, wiersze w Sheecie, alert o spadku na Discordzie
- Link do demo/loom: `<REPLACE_WITH_DEMO_LINK>`
