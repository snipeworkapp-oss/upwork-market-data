# Upwork Market Index — Free Weekly Dataset 📊

**The only open, continuously-updated dataset of the Upwork freelance job market.**

Every week this repository publishes fresh statistics computed from **thousands of live Upwork job posts** — average budgets, hourly rates, category demand, and client-country breakdowns. Upwork does not publish this data, and raw job posts disappear from public view within days, so this is effectively the durable public record of the freelance market, week by week.

The data is gathered by [**SnipeWork**](https://snipework.com), which scans Upwork continuously through the official Upwork API. It is **free to use under CC-BY-4.0** — for research, articles, dashboards, ML training, anything — as long as you credit the source.

> 📈 **Live human-readable report:** [snipework.com/market/index](https://snipework.com/market/index)
> 🔌 **Live JSON API:** [snipework.com/api/market/index](https://snipework.com/api/market/index)

---

## 📂 What's in here

| File | Grain | Description |
|------|-------|-------------|
| [`data/weekly.csv`](data/weekly.csv) | one row per ISO week | Headline metrics: jobs scanned, avg/median fixed budget, avg hourly rate, fixed-vs-hourly split, experience-level demand |
| [`data/categories.csv`](data/categories.csv) | week × category | Per-category jobs, share of market, budgets and hourly rates across all 12 Upwork categories |
| [`data/countries.csv`](data/countries.csv) | week × country | Top client countries by job volume each week |

All files are updated automatically every Monday via GitHub Actions.

### Column reference — `weekly.csv`

| Column | Type | Meaning |
|--------|------|---------|
| `week` | string | ISO week key, e.g. `2026-W29` |
| `period_start` / `period_end` | date | Week bounds (UTC, Monday–Sunday) |
| `jobs_scanned` | int | Number of job posts observed that week |
| `avg_fixed_usd` | int | Mean advertised fixed-price budget (USD) |
| `median_fixed_usd` | int | Median advertised fixed-price budget (USD) |
| `avg_hourly_usd` | int | Mean advertised hourly rate (USD/hr) |
| `fixed_share` / `hourly_share` | float | Share of jobs that are fixed-price vs hourly (0–1) |
| `entry_share` / `intermediate_share` / `expert_share` | float | Experience-level demand mix (0–1) |
| `is_partial` | 0/1 | `1` if the week was still in progress when captured |

---

## 🚀 Quick start

### Python (pandas)
```python
import pandas as pd

weekly = pd.read_csv(
    "https://raw.githubusercontent.com/snipeworkapp-oss/upwork-market-data/main/data/weekly.csv"
)
print(weekly.tail())

# Average fixed budget trend
weekly.plot(x="week", y="avg_fixed_usd", title="Upwork avg fixed budget by week")
```

### JavaScript
```js
const res = await fetch(
  "https://raw.githubusercontent.com/snipeworkapp-oss/upwork-market-data/main/data/weekly.csv"
);
const csv = await res.text();
console.log(csv);
```

### Or hit the live API directly (always current)
```bash
curl https://snipework.com/api/market/index
curl "https://snipework.com/api/market/dataset?file=categories"
```

---

## 📊 Example insights

These are the kinds of questions the dataset answers out of the box:

- **What's the typical Upwork project worth?** The gap between `avg_fixed_usd` and `median_fixed_usd` reveals a long tail — most posts are small, a minority of large projects pulls the average up.
- **Which categories pay best per hour?** Sort `categories.csv` by `avg_hourly_usd` — Legal, IT & Networking and Data Science consistently top it.
- **Where do clients come from?** `countries.csv` is dominated by the US, UK, India, Australia and Canada.
- **Is the market shifting to fixed or hourly?** Track `fixed_share` over time.

---

## 🔄 How it's collected (methodology)

SnipeWork continuously scans **public** Upwork job posts through the **official Upwork GraphQL API**. Each ISO week (Monday–Sunday, UTC) the scanned posts are aggregated:

- Budget averages use the midpoint of posted ranges.
- Hourly outliers above $500/hr and zero-budget posts are excluded.
- Category shares are computed over posts with a known category.
- The current week updates daily and is **finalized on Sunday night**; past weeks never change.

No personal data, client names, or freelancer identities are included — only aggregate market statistics.

---

## 📜 License & attribution

Released under [**Creative Commons Attribution 4.0 (CC-BY-4.0)**](LICENSE). You may share and adapt the data for any purpose, including commercially, provided you give appropriate credit:

> Data: [SnipeWork Upwork Market Index](https://snipework.com/market/index) — CC-BY-4.0

If you build something with this data, we'd love to see it — open an issue or mention [@SnipeWorkApp](https://x.com/SnipeWorkApp).

---

## 🎯 About SnipeWork

[**SnipeWork**](https://snipework.com) helps freelancers win more work on Upwork: it scans the platform every minute through the official API, pings your Telegram the moment a matching job is posted, and drafts an AI proposal ready for you to review and send. This dataset is a byproduct of that scanning — published openly because the freelance market deserves a public record.

⭐ **Star this repo** to follow the weekly updates.
