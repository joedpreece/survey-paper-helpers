"""
This script checks the number of studies which do not have indexed keywords.
"""

from survey_paper_helpers.utils import load_data

# Load the Scopus indexed keywords.
df = load_data()

df = df[df["Index Keywords"].isna()]

print(len(df))