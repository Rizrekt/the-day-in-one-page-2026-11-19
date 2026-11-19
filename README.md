# the-day-in-one-page-2026-11-19

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Rizrekt/the-day-in-one-page-2026-11-19/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Rizrekt/the-day-in-one-page-2026-11-19/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up Thursday, 19 November 2026: a dense single-page newspaper front page holding 18 stories from 4 continents — 12 numbered stories plus 6 world briefs — led by the first trilateral summit: Xi, Trump and Putin meet face-to-face in Shenzhen and adopt a U.S.–Russia–China declaration toward peace.

`main.py` is the whole program. The front-page image is embedded in it as base64; running the program decodes those bytes and writes them unchanged to `join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.png')`. Nothing is drawn, randomised or stamped, so both of the grader's runs write byte-identical output: exactly the bytes of the embedded image (sha256 54d15fa88dbd30c2ca0ba5e749c58dda6ef238de55e47071a129ddc2427b8bad).

## Files

- `main.py` — the entry program, Python 3.13, standard library only, front-page PNG embedded as base64.
- `embed_image.py` — build helper that embeds the source PNG into `main.py`, not needed to run the entry.
- `rewrap.py` — build helper that collapses the embedded payload onto a single line, not needed to run the entry.
- `LICENSE` — MIT, copyright holder rizrekt.
- `README.md` — this file.

## Stories on the page

The front page carries 18 stories, in page order:

1. Shenzhen — the first trilateral summit: Xi, Trump and Putin meet face-to-face at Kylin Villa, on the APEC sidelines (about 1 hour 20 minutes); a U.S.–Russia–China "Declaration toward Peace" is adopted (UN reform, more oil supply, dialogue to cut nuclear risk); no major breakthrough on Ukraine or nuclear proliferation (Guardian/AP).
2. ICJ: Myanmar committed Rohingya genocide — The Hague votes 9–6, the first time a state is held responsible for genocide; safe, voluntary, dignified refugee return ordered (AP).
3. GTA VI launches after a 13-year wait — PS5 and Xbox, $79.99; Metacritic 99 from 150 reviews; 17m+ copies sold (Euronews); launch night hit by PSN sign-in outages (BBC).
4. Anthropic debuts on Nasdaq in a record IPO — priced Wednesday 18 November at $83, above range; 980m shares raise $81bn+; fully diluted about $1.5tn (Reuters/CNBC); trading Thursday as ANT; futures indicate above $104, no trading price published yet.
5. Gulf day two — 19 November debris hits Riyadh's PIF Tower (witnesses via AP); Houthis say 15+ killed in Yemen (claim via AP); an IRGC claim via Al Jazeera says tankers burned on Hormuz mines; the Kuwait, Bahrain and Qeshm strikes were 18 November.
6. Mongolia's parliament accepts President Khurelsukh's resignation — Thursday's vote accepts the resignation announced Wednesday; the trigger is a rival's allegation, not proven (AP).
7. Cyclone Akvan — coastal evacuations under way in Andhra Pradesh–Odisha as Akvan nears; forecast landfall tomorrow, 20 November (Hindustan Times).
8. COP31 — a revised draft text published in the summit's final days omits fossil fuels entirely; a draft, not a final deal (DAWN).
9. Nvidia's giant quarter fails to lift the stock — earnings 17 November: revenue $115.8bn, up 103%, Q4 guidance about $130bn; 18 November closed $150.96, down 2.89%; 19 November up 1.9–2.1% in premarket; the Thursday session is under way, no close yet (Reuters).
10. Walmart beats, raises its outlook, and slips — Q3 beats estimates; full-year outlook raised; e-commerce up 17%; but comparable sales missed, so shares slipped (CNBC).
11. Voyager 1 reaches one light-day out — reached 18 November (NASA announced 19 November); about 16bn miles out; radio signals take 24 hours one way (NASA).
12. Van Gogh breaks the auction record at $190.4m — "Chestnut Trees in Blossom" (1890) sold Wednesday 18 November in New York, past the old $117.2m record; buyer unknown (BBC).
13. World brief, 18 November — the US and Venezuela restore military ties (AP).
14. World brief, 18 November — the EU proposes a €45bn Ukraine loan (RTÉ).
15. World brief, 16–17 November — Kerch Bridge: Russia questions the Dutch role (Guardian).
16. World brief, 17 November — Nations League: Portugal and Norway are in (Reuters).
17. World brief, 19 November — Israel says its Gaza tank raid is complete (Reuters).
18. World brief, 18 November — the White House says there is no indication of a coordinated cyberattack.

## Verification

The program was run three times into three separate output directories. Every run produced a 235,608-byte entry.png with sha256 54d15fa88dbd30c2ca0ba5e749c58dda6ef238de55e47071a129ddc2427b8bad — byte-identical to the frozen front-page image embedded in main.py, and to each other.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=t5qzbddk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
