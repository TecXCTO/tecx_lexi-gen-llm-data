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


