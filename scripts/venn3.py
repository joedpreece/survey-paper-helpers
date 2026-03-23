#%% Word Frequencies
import re

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from survey_paper_helpers.utils import load_key_words

df = load_key_words()

df_venn = df.reset_index()

def helper(
        terms: list[str],
) -> set:
    pattern = r"|".join(map(re.escape, terms))
    mask = df_venn['Index Keywords'].fillna('').str.contains(pattern, case=False, regex=True)
    return set(df_venn.loc[mask, 'EID'])

set1 = helper(
    terms=[
        "ontolog",
        # "semantic",
        # "knowledge graph"
    ]
)

set2 = helper(
    terms=[
        "transport"
    ]
)

set3 = helper(
    terms=[
        "decarbonis",
        "sustain",
        # "net zero"
    ]
)

set4 = helper(
    terms=[
        "twin",
    ]
)

plt.figure(figsize=(8, 8))
venn3([set1, set2, set3], ('Ontology', 'Transport', 'Decarbonisation'))

plt.savefig("./../artifacts/venn3.pdf")