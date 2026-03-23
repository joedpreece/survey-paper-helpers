#%% Word Frequencies
from matplotlib import pyplot as plt

from wordcloud import WordCloud

from survey_paper_helpers.utils import load_key_words

df = load_key_words()

df['Index Keywords'] = df['Index Keywords'].str.strip()
df['Index Keywords'] = df['Index Keywords'].fillna('').astype(str)

text = ' '.join(df['Index Keywords'])

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# plt.show()

plt.savefig("./../artifacts/wordcloud.pdf")