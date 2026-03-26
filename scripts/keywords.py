#%%
from survey_paper_helpers.utils import load_index_key_words

df = load_index_key_words()

s = df["Index Keywords"].value_counts()
