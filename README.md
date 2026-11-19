# the-day-in-one-page-2026-11-19

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Rizrekt/the-day-in-one-page-2026-11-19/rank.svg)](https://make.fun/badge/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Rizrekt/the-day-in-one-page-2026-11-19/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up Thursday, 19 November 2026: a dense single-page world-news front page holding 36 stories from 5 continents — 12 numbered stories, 6 world briefs and an 18-story one-line index — plus a day-in-numbers strip, led by the first Xi–Trump–Putin trilateral summit in Shenzhen. The Thursday market closes are folded in: Anthropic's first Nasdaq close at $97.17 (+17.1% vs the $83 IPO price) and Nvidia's Thursday close at $145.98 (-3.3%).

`main.py` is the whole program. The front-page image is embedded in it as base64; running the program decodes those bytes and writes them unchanged to `join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.png')`. Nothing is drawn, randomised or stamped, so both of the grader's runs write byte-identical output: exactly the bytes of the embedded image (sha256 522cb97a823f964fbee4090df544ebd0b9b413b18827667a20fd75f10d9511e2, 278,864 bytes).

## Files

- `main.py` — the entry program, Python 3.13, standard library only, front-page PNG embedded as base64.
- `embed_image.py` — build helper that embeds the source PNG into `main.py`, not needed to run the entry.
- `rewrap.py` — build helper that collapses the embedded payload onto a single line, not needed to run the entry.
- `LICENSE` — MIT, copyright holder rizrekt.
- `README.md` — this file.

## Stories on the page

The front page carries 36 stories, in page order:

1. Shenzhen — the first trilateral summit: Xi, Trump and Putin meet face-to-face at Kylin Villa, on the APEC sidelines (about 1 hour 20 minutes); a U.S.–Russia–China "Declaration toward Peace" is adopted (UN reform, more oil supply, dialogue to cut nuclear risk); no major breakthrough on Ukraine or nuclear proliferation (Guardian/AP).
2. ICJ: Myanmar committed Rohingya genocide — The Hague votes 9–6, the first time a state is held responsible for genocide; safe, voluntary, dignified refugee return ordered (AP).
3. GTA VI launches after a 13-year wait — PS5 and Xbox, $79.99; Metacritic 99 from 150 reviews; 17m+ copies sold (Euronews); launch night hit by PSN sign-in outages (BBC).
4. Anthropic debuts on Nasdaq in a record IPO — priced Wednesday 18 November at $83, above range; 980m shares raise $81bn+; fully diluted about $1.5tn (Reuters/CNBC); trading Thursday as ANT; closed Thursday at $97.17, +17.1% vs $83 (Reuters).
5. Gulf day two — 19 November debris hits Riyadh's PIF Tower (witnesses via AP); Houthis say 15+ killed in Yemen (claim via AP); an IRGC claim via Al Jazeera says tankers burned on Hormuz mines; the Kuwait, Bahrain and Qeshm strikes were 18 November.
6. Mongolia's parliament accepts President Khurelsukh's resignation — Thursday's vote accepts the resignation announced Wednesday; the trigger is a rival's allegation, not proven (AP).
7. Cyclone Akvan — coastal evacuations under way in Andhra Pradesh–Odisha as Akvan nears; forecast landfall tomorrow, 20 November (Hindustan Times).
8. COP31 — a revised draft text published in the summit's final days omits fossil fuels entirely; a draft, not a final deal (DAWN).
9. Nvidia's giant quarter fails to lift the stock — earnings 17 November: revenue $115.8bn, up 103%, Q4 guidance about $130bn; 18 November closed $150.96, down 2.89%; closed Thursday at $145.98, -3.3%, down for a second day (Reuters).
10. Walmart beats, raises its outlook, and slips — Q3 beats estimates; full-year outlook raised; e-commerce up 17%; but comparable sales missed, so shares slipped (CNBC).
11. Voyager 1 reaches one light-day out — reached 18 November (NASA announced 19 November); about 16bn miles out; radio signals take 24 hours one way (NASA).
12. Van Gogh breaks the auction record at $190.4m — "Chestnut Trees in Blossom" (1890) sold Wednesday 18 November in New York, past the old $117.2m record; buyer unknown (BBC).
13. World brief, 18 November — the US and Venezuela restore military ties (AP).
14. World brief, 18 November — the EU proposes a €45bn Ukraine loan (RTÉ).
15. World brief, 16–17 November — Kerch Bridge: Russia questions the Dutch role (Guardian).
16. World brief, 17 November — Nations League: Portugal and Norway are in (Reuters).
17. World brief, 19 November — Israel says its Gaza tank raid is complete (Reuters).
18. World brief, 18 November — the White House says there is no indication of a coordinated cyberattack.
19. Xi opens APEC: AI, supply-chain call (AP).
20. Japan–Russia talks, first in 7 yrs (Kyodo).
21. Japan–India deepen defence ties (Kyodo).
22. Nikkei +0.71% on ANT pricing (Kyodo).
23. Orchid named for Princess Aiko (Kyodo).
24. Wakamotoharu leads in Kyushu (Kyodo).
25. Pope Leo marks St Peter's 400th (AP).
26. CENTCOM chief meets MBS (SPA).
27. Jordan sailor missing in Hormuz (CBS).
28. Israel extends Gaza doctor detention.
29. Fed minutes: 'almost all' for hikes (RTÉ).
30. ANT retail demand sets record (CNBC).
31. Nasdaq +1% at open on ANT (Reuters).
32. GTA VI preorders est. $1.65bn.
33. Launch-day leave +24–32% (HR data).
34. 14 NOV — Voyager glitch probed (NASA).
35. Democrats nominate Jeffries for Speaker.
36. Vanuatu urges summit reform (France 24).

## The day in numbers

9–6 ICJ genocide verdict · 99 GTA VI Metacritic score · $83 Anthropic IPO price · 1 light-day out for Voyager 1 · $190.4m Van Gogh record price · 15+ Yemen dead (Houthi claim).

Region tally on the page: Europe 5 · Americas 15 · Asia 10 · Middle East 5 · Oceania 1.

## Verification

The program was run into separate output directories. Every run produced a 278,864-byte entry.png with sha256 522cb97a823f964fbee4090df544ebd0b9b413b18827667a20fd75f10d9511e2 — byte-identical to the frozen front-page image embedded in main.py, and to each other.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=t5qzbddk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
