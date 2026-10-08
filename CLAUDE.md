# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose

workout-processor converts workout programs written in spreadsheet form (Google Sheets exported as
.xlsx, specifically) into a human-readable, presentable HTML file. The target input is the author's
own personal/client workout spreadsheets — `reader.py`'s parsing logic is intentionally hardcoded to
one specific sheet layout, not a general-purpose spreadsheet parser.

The project is early-stage/in-progress. Modules like `printer.py` and `editor.py` (HTML rendering,
web UI) don't exist yet. `workout_processor.py`'s `__main__` block is currently a scratch area for
manually exercising `reader.read()` against sample files rather than a finished CLI.

## Environment

`.venv/` has both `pytest` and the project's runtime dependencies (`pandas`, `openpyxl`), pinned in
`pyproject.toml` and installed via `.venv/bin/pip install .`. The system Python (Gentoo
`dev-python/*` packages) also has `pandas`/`openpyxl` available separately, which is why
`python3 workout_processor.py` works outside the venv too.

Commands:
```
# run all tests
.venv/bin/pytest tests/

# run a single test
.venv/bin/pytest tests/test_builder.py::test_build_exercise

# run the manual reader scratch script
.venv/bin/python3 workout_processor.py
```

## Code Style
- Maximum line length of 100 characters for python files

## Architecture

### Data model (`data/data.py`)
A containment hierarchy, each level a `@dataclass`:

```
Training_Program -> Period -> Workout -> Block -> Line -> Set
                                       -> Line (Workouts can also hold Lines/Blocks directly)
```

- `Training_Program.period_and_workout_list` and `Workout.line_and_block_list` are typed as
  `list[Period | Workout]` / `list[Line | Block]` — a program/workout doesn't have to go through every
  intermediate layer, it can mix in lower layers directly.
- `Set` holds the actual numeric training data (`rep_count`, `resistance_kg`, `intensity`, `tempo`,
  `volume`, `order_index`); `Line` pairs an optional `Exercise` with a `set_list`; `Block`/`Workout`
  group `Line`s (and `Block`s) under a title/description/timestamp.
- `Exercise`, `Muscle`, `Tag`, `Equipment`, `Movement`, and `Adaptation` are the supporting
  descriptive/taxonomy dataclasses referenced from `Exercise` and from `tag_list` fields throughout.
- `User`/`Trainer`/`Athlete` exist for the `Training_Program.author` field but have no `build_*`
  counterparts in `builder.py` yet.
- Dataclass gotchas enforced throughout this file: list fields must use `field(default_factory=list)`
  (never a bare `[]` default); fields without defaults must come before fields with defaults; a class
  referencing another type defined later in the file (or itself) relies on
  `from __future__ import annotations` at the top of the module rather than needing manual string
  forward references.

### `builder.py`
One `build_x` factory function per `data/data.py` dataclass (`build_muscle`, `build_tag`,
`build_exercise`, `build_set`, `build_line`, `build_block`, `build_workout`, `build_period`,
`build_training_program`, plus the `get_volume` helper). This is where input normalization belongs —
not in the dataclasses or in `reader.py`:
- Name/title-like string inputs are normalized with `" ".join(x.split()).title()` (collapses stray
  internal whitespace, strips leading/trailing whitespace, title-cases).
- `build_tag` returns `Tag(tag=f"#{name.strip()}")` — tags are always stored with a leading `#`.
- `get_volume(rep_count, resistance_kg)` computes the standard strength-training "volume load"
  (`rep_count * resistance_kg`); `build_set` calls it to fill `Set.volume` rather than taking volume as
  an input.
- Builders that accept child collections (`build_line`, `build_block`, `build_workout`, `build_period`,
  `build_training_program`) take them as optional keyword args defaulting to `None` and normalize to
  `[]` internally — never pass a mutable default directly.

### `reader.py` — xlsx parsing
Reads one worksheet at a time with openpyxl in `read_only=True` mode and locates workouts purely by
cell formatting, not by fixed coordinates:
- A workout's title cell is detected by `check_title`: value starts with `"Day"`, bold font, black
  fill (`FF000000`).
- The reader scans right from a title cell to find the workout's width (stops at the first date cell)
  and down to find its height (stops at a "Coaching Notes" cell), then walks that bounding box to pull
  out row/column data.
- `check_unused`/blank-run counters (`blank_count_h`, `blank_count_v`) are how the scan knows it has
  run off the end of a row/column of workouts on the sheet.
- `read_sheet` and `read_workout` are mid-refactor; `read_workout`'s row/column loop bounds and the
  commented-out `sheet.iter_rows` block are known-incomplete/incorrect, not finished reference code.
- This module's output (plain dicts) doesn't yet feed into `builder.py`/`data/data.py` — wiring the
  reader's parsed rows into `build_*` calls is still open work.

### `config.py`
Just `ACCEPTED_EXTENSIONS` — the file extensions `workout_processor.py` will accept
(`.pdf .csv .ods .xlsx`), even though only `.xlsx` is actually handled by `reader.py` today.

### `workout_processor.py`
Intended as the CLI entry point: validates the input file exists (`validate_file`) and has an
accepted extension (`check_extension`), then hands off to `reader.read`. CLI arg handling
(`sys.argv`) and the `run()` wiring are currently commented out in favor of hardcoded sample-file
paths for manual testing — re-enabling argv handling is pending, not an oversight to silently "fix"
without checking intent.
