"""
This script extracts all keywords across all studies, and saves them to a CSV file.
"""

from survey_paper_helpers.utils import load_scopus_indexed_keywords

# Load the Scopus indexed keywords.
df = load_scopus_indexed_keywords()

# Extract the value counts of the keywords.
s = df["Index Keywords"].value_counts()

# Save the value counts to a CSV file.
s.to_csv("./../artifacts/Keywords.csv")