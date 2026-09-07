# Confidence Challenge -- Starter Files

Starter project for Page 11 (Final Challenge, Part 1: Comparison Operators).

The boilerplate function and the test file have already been written for
you. **You do not need to write or edit the test file.** Your job is only
to replace the `pass` statement inside the boilerplate function with real
`if` / `elif` / `else` logic, following the rules on Page 11.

This is its own standalone project, separate from the Gryffindor
eligibility challenge on Page 12. Keep the two in separate folders.

## Folder structure

```
confidence-challenge/
├── app/
│   └── sorting_hat_confidence.py
├── test/
│   └── test_sorting_hat_confidence.py
├── pytest.ini
└── requirements.txt
```

Application code lives in `app/`. Tests live in `test/`.

| File | What it is | Do you edit it? |
|---|---|---|
| `app/sorting_hat_confidence.py` | Boilerplate | Yes -- replace `pass` with your logic |
| `test/test_sorting_hat_confidence.py` | Tests | No |

## Setup

1. Copy this whole `confidence-challenge` folder into your
   `hogwarts-sorting-hat` repository, as a top-level folder alongside your
   existing `sorting_hat.py`.
2. Install pytest if you haven't already:

   ```
   cd confidence-challenge
   pip install -r requirements.txt
   ```

   (or simply `pip install pytest`)

## Running the tests

Always run pytest from inside the `confidence-challenge` folder (the one
containing `app/`, `test/` and `pytest.ini`):

```
cd confidence-challenge
pytest test/test_sorting_hat_confidence.py -v
```

Or simply:

```
pytest -v
```

### Why the imports still work

The test file still says `from sorting_hat_confidence import ...`, even
though `sorting_hat_confidence.py` now lives in a different folder
(`app/`) to the test file (`test/`). That works because of `pytest.ini`:
it tells pytest to add `app/` to Python's import path before the tests
run. You don't need to understand this file in detail, and you don't need
to change it -- just keep it inside `confidence-challenge`, alongside
`app` and `test`.

Follow the instructions on Page 11 of the tutorial for the full Red,
Green, Refactor workflow, including when to commit and push at each
stage.
