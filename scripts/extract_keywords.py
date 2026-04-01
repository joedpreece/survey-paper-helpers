"""
This script extracts all keywords across all studies, and saves them to a CSV file.
"""

from survey_paper_helpers.utils import load_index_key_words

df = load_index_key_words()

s = df["Index Keywords"].value_counts()

s.to_csv("./../artifacts/Keywords.csv")