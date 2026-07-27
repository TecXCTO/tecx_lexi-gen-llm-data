"""
Main Single Script: 
run_pipeline.py
This single script handles the entire lifecycle: 
downloading linguistic corpus data, structuring it by word length, 
adding educational prompt-response formatting, and saving the files cleanly.
"""

import os
import json
import string
import nltk
from nltk.corpus import words, wordnet
from tqdm import tqdm

# Ensure required linguistic databases are downloaded locally
print("Initializing linguistic databases...")
nltk.download('words', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

class DataGeneratorPipeline:
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load unique lowercase English words from NLTK corpus
        print("Loading and filtering English dictionary...")
        raw_word_list = words.words()
        self.english_words = sorted(list(set(w.lower() for w in raw_word_list if w.isalpha())))

    def get_definition(self, word):
        """Fetch basic definition or concept from WordNet."""
        synsets = wordnet.synsets(word)
        if synsets and synsets[0].definition():
            return synsets[0].definition()
        return f"The English word '{word}'."

    def save_jsonl(self, filename, dataset):
        """Helper to write to JSONL format optimal for LLM training."""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in dataset:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        print(f"Successfully saved {len(dataset)} records to {filepath}")

    def build_alphabet_data(self):
        """Level 1: Generates representations for individual characters A-Z."""
        print("Generating Level 1: Alphabet Data...")
        dataset = []
        for char in string.ascii_uppercase:
            prompt = f"Identify and describe the uppercase English letter: {char}"
            response = f"The character '{char}' is the English alphabet letter index {string.ascii_uppercase.index(char) + 1}."
            dataset.append({"prompt": prompt, "response": response})
        self.save_jsonl("01_alphabets.jsonl", dataset)

    def build_word_data(self):
        """Levels 2, 3, & 4: Categorizes and extracts data by word lengths."""
        print("Processing dictionary into scale-length datasets...")
        
        short_words_data = []  # 2 to 5 chars
        long_words_data = []   # 6 to 14 chars
        max_words_data = []    # 15+ chars

        for word in tqdm(self.english_words, desc="Analyzing Words"):
            length = len(word)
            if length < 2:
                continue
                
            definition = self.get_definition(word)
            
            # Structuring the data sample natively for LLM instruction tuning
            sample = {
                "prompt": f"Analyze the English word: '{word}'. Provide its length, structural makeup, and semantic definition.",
                "response": f"The word '{word}' consists of {length} characters. Definition: {definition}."
            }

            if 2 <= length <= 5:
                short_words_data.append(sample)
            elif 6 <= length <= 14:
                long_words_data.append(sample)
            elif length >= 15:
                # Highlight maximal complexity traits for maximum-length tier
                sample["response"] += f" This is classified as an ultra-long maximum length English word."
                max_words_data.append(sample)

        self.save_jsonl("02_short_words.jsonl", short_words_data)
        self.save_jsonl("03_long_words.jsonl", long_words_data)
        self.save_jsonl("04_max_words.jsonl", max_words_data)

    def run_all(self):
        """Orchestrate the full autonomous generation lifecycle."""
        print("=== Starting Autonomous Data Generation Pipeline ===")
        self.build_alphabet_data()
        self.build_word_data()
        print("=== Pipeline Execution Successfully Completed ===")

if __name__ == "__main__":
    generator = DataGeneratorPipeline()
    generator.run_all()
