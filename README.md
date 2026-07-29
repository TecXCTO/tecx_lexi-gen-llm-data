# tecx_lexi-gen-llm-data

TecX(Technology Engineering Computation Expansion)'s Lexical Generation for LLM Data

To build a system that autonomously generates English language training data—progressing from single letters to complex, maximum-length words

* lexi-gen-llm-data (Short for Lexical Generation for LLM Data)
* Alternative: alpha-to-max-dataset-builder

------------------------------

## 📂 GitHub Repository Architecture
```
tecx_lexi-gen-llm-data/
│
├── .gitignore               # Ignores local datasets, caches, and environment files
├── README.md                # Project documentation and setup instructions
├── requirements.txt         # Python dependencies
├── run_pipeline.py          # Main single-script orchestration file
│
└── data/                    # Autonomous output directory (Git-ignored content)
    ├── 01_alphabets.jsonl   # Level 1: A-Z single character data
    ├── 02_short_words.jsonl # Level 2: 2-5 character words with definitions
    ├── 03_long_words.jsonl  # Level 3: 6-14 character words with syntax
    └── 04_max_words.jsonl   # Level 4: 15+ character ultra-long words
```
------------------------------

## 📄 File-by-File Breakdown##


Clear instructions on how the autonomous pipeline works.

# Lexi-Gen LLM Data Builder
An autonomous pipeline that synthesizes English language training data, systematically scaling from single alphabets to maximum-length English words.
## Setup1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the complete autonomous pipeline: `python run_pipeline.py`

------------------------------

------------------------------
## 🚀 Scaling Next Steps
If you plan to scale this project up further, would you like to explore:

* Integrating synthetic sentence creation using open-source models?
* Adding Hugging Face Dataset API token uploading directly into the script?
* Formatting the output files into OpenAI ChatML (messages) structure instead of raw prompt/response pairs?

########

# word_generator.py

Summary (one–two sentences)
- In `word_generator.py` (lines 3–11), the `__init__` of the `Iterative_Nested_Word_Generator` class initializes instance state: it prints a startup message, sets `self.ch_len`, builds `self.lowercase` from `string.ascii_lowercase` (sorted), and sets `self.current_word` to the result of calling `self.iterative_nested_generator()`.

Key ideas (up to five)
- `print("Iterative_Nested_Word_Generator has been started.")` logs that the constructor ran (line 4).
- `self.ch_len = c` stores the constructor argument (default `4`) as the character length parameter (line 5).
- `self.lowercase = sorted(string.ascii_lowercase)` sets `self.lowercase` to the sorted sequence of lowercase letters; an earlier (commented) alternative used the raw `string.ascii_lowercase` (lines 7–8).
- `self.current_word` is first set to an empty list and then immediately overwritten by `self.iterative_nested_generator()` — the initial empty-list assignment is therefore redundant (lines 9–11).
- The constructor delegates further initialization to `self.iterative_nested_generator()` by assigning its return value to `self.current_word` (line 11).

How this snippet is used within its containing function (`__init__`, `word_generator.py` lines 3–11)
- The provided `__init__` function is the class constructor: it configures basic instance attributes (`ch_len` and `lowercase`), then sets up `current_word` by calling `self.iterative_nested_generator()`. The comments show prior versions (using an unsorted `ascii_lowercase`, or different initializations of `current_word`), but the active code ends with `self.current_word` taking whatever value `iterative_nested_generator()` returns.

Calling functions / code path to reach this snippet
- The constructor calls `self.iterative_nested_generator()` (line 11). The implementation of `iterative_nested_generator()` is not provided in the snippet, so I cannot precisely describe what value is produced or whether it returns a generator, list, or other object. If you provide the `iterative_nested_generator` implementation (or surrounding lines beyond 11), I can trace the exact code path and describe the produced `current_word`.
