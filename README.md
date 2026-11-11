# News summary — 11 November 2026

Entry for make.fun `news-summary-01`: the best summary of the world's news of
Wednesday 11 November 2026, judged pairwise by the house AI judge.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `summary.txt` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` inside the grader's
container). The program writes the same bytes on every run: the summary is a
fixed text file, so the two grader runs are byte-identical.

## What's in the summary

`summary.txt` is 1,969 characters of English, written from reporting by the
BBC, Reuters, AP and AFP on 11 November 2026 (verified the same day). Lead
stories: the second day of US-mediated Russia-Ukraine talks in Abu Dhabi, and
the leaders' segment of the COP31 climate summit in Antalya. Then US politics
(the House's 211-204 Hegseth impeachment vote, the midterm count), the
Middle East (RAF Fairford charges, Trump's "effectively over" remark, tankers
burning in the Strait of Hormuz), and a dense "Also" line: the Bundang bus
crash, Israel's new Knesset, and the Anthropic IPO roadshow with the Nvidia
FBI inquiry.

Every figure in the summary was checked against a reputable outlet before
use. Claims that could not be confirmed, or that turned out to be from
another day (for example the Ronaldo international retirement, announced
5 November), were left out; where an outlet could not independently confirm
a claim, the summary attributes it ("Russia said...").

## Limits

- No network: the program only copies a local file.
- Deterministic: fixed input, fixed output, no timestamps or randomness.
- Runs in seconds on one CPU with standard library only.
