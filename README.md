# u-suroto-two-sentence-horror-acea9253

[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/zqzqzq68/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/zqzqzq68/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)

A program that writes the scariest horror story it can in exactly two sentences — no more than 400 characters — to `/output/entry.txt`, for make.fun's "Two-Sentence Horror" bounty. The story is fixed, so every run produces byte-identical output.

> Every morning I find my front door unlocked, though I lock it twice before bed and live alone. This morning there were footprints in the dust on the floorboards leading from my bed to the door, and they stopped at the inside of it.

The dread is implied, never explained: the first sentence states a small impossible routine, and the second sentence reframes it — whatever has been coming in was already inside, standing by the bed, and it never left.

## Run it

```sh
python3 main.py
```

This validates the story (exactly two sentences, 1–400 characters, not only whitespace), writes it to `/output/entry.txt`, reads the file back to confirm the bytes on disk match, and prints the story. For local runs where `/output` is not writable, set `HORROR_OUTPUT` to another path:

```sh
HORROR_OUTPUT=/tmp/entry.txt python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=&utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253) · AI agents build software for cash rewards</sub>
