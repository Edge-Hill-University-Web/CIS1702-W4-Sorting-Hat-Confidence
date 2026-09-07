# CIS1702 Week 4: Sorting Hat Condfidence
 
The boilerplate function and the test file have already been written for
you. **You do not need to write or edit the test file.** Your job is only
to replace the `pass` statement inside the boilerplate function with real
`if` / `elif` / `else` logic, following the rules on Page 11.

This is its own standalone project, separate from the Gryffindor
eligibility challenge on Page 12. Keep the two in separate folders.

## Folder structure

```
CIS1702-W4-Sorting-Hat-Confidence
/
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

1. Fork this repository and then clone it (from your own github) folder into your
   workspace.
   
3. Install pytest if you haven't already:

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

