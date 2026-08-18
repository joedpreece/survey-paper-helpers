"""
This script generates a word cloud of the index keywords.
"""
#%%
from collections import Counter

from matplotlib import pyplot as plt

from wordcloud import WordCloud

from survey_paper_helpers.utils import load_scopus_indexed_keywords

# Load the Scopus indexed keywords.
df = load_scopus_indexed_keywords()

#%% Strip whitespaces
df["Index Keywords"] = df["Index Keywords"].str.strip()

#%% Fill the null values with empty strings
df["Index Keywords"] = df["Index Keywords"].fillna("").astype(str)

#%%
freqs = Counter(df["Index Keywords"])

#%%
text = " ".join(df["Index Keywords"])

dpi = 300
width_mm = 89
width_inches = width_mm / 25.4
width_pixels = int(width_inches * dpi)

wordcloud = WordCloud(
    width=width_pixels,
    height=int(width_pixels / 2),
    background_color=None,
    mode="RGBA",
    min_font_size=7,
    margin=0,
    collocations=False,
).generate_from_frequencies(freqs)

fig, ax = plt.subplots(
    figsize=(width_inches, width_inches / 2),
    dpi=dpi,
)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
ax.set_position([0, 0, 1, 1])

# plt.show()
plt.savefig("./../artefacts/Figure_Wordcloud.pdf")
