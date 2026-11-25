[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rexxxspace/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rexxxspace/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World in One Picture — Wednesday, 25 November 2026

A make.fun **news-image-20261125** entry: one 1024×1024 PNG that sums up the
world news of Wednesday, 25 November 2026, drawn as a newspaper front page.

## The image

`entry.png` is a one-page newspaper — "The World in One Page" — carrying
**30 stories across 7 regions, every one of which happened or was first
reported on Wednesday 25 November 2026**, with a giant dated masthead, a
big-numbers strip, a region bar, certainty/source tags, a pinned world map,
and a DATE CHECK box that names the big stories deliberately left out
because they belong to other days.

Leads:

1. **Middle East — war.** Saudi-led jets bomb Yemen's Hodeidah port early
   Wednesday, hours after a Houthi strike on a Riyadh tower injured 11
   people (Arab News / Reuters).
2. **SE Asia — rescue.** Rescuers search for about 30 workers stuck 100 m
   down a flooded, unauthorised gold mine at Pongkor, Bogor, West Java,
   since Monday's rains (Reuters / Basarnas).
3. **Asia — markets.** Wednesday's sell-off undoes Tuesday's record chip
   surge: Taiex down over 6%, Kospi −5.6%, Nikkei −3.6% as AI confidence
   cracks (AP / Reuters).

Plus nine story cards (Dutch climate targets stay binding; Putin vows
retaliation as refinery processing falls ~45%; the Kremlin bars Europe
from the next peace-talk round; Trump meets NATO chief Rutte at
Mar-a-Lago; the US weighs tariffs on 16 partners; 25 hostages seized in a
Cartagena supermarket; Xiamen Airlines orders 50 Boeing 737-8s for
$7.4 bn; Indonesia's Vice-President Gibran resigns; Australia apologises
to LGBTQ veterans) and 18 more one-line stories — drone strikes near
Samara's refineries, Iran's record-low rial, UNAIDS' HIV rebound warning,
Togo's 90% vaccination milestone, the signed Solomon Islands–Australia
pact, Brent at $90.97, Bitcoin at $59,258, and more.

Left out on purpose (DATE CHECK): Nvidia reinstating Jensen Huang and
Asia's record chip surge (Mon 23 – Tue 24 Nov — only Wednesday's reversal
and board scrutiny count), Ukraine's Libya ship strike (22–24 Nov),
Senegal restored as AFCON champions (Tue 24 Nov), and the Hanoi
restaurant blast (Tue 24 Nov).

## How it works

- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `/output/entry.png` — deterministic, no network, same bytes every run.
- `build_image.py` is the generator that drew `entry.png` with Pillow:
  every headline, label and illustration is rendered programmatically,
  so the text is exact and the file is reproducible.

## License

MIT — see `LICENSE`.
