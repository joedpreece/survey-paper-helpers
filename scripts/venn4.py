# %%
import re

from venny4py.venny4py import *

from survey_paper_helpers.utils import load_key_words

df = load_key_words()

df_venn = df.reset_index()


def helper(
    terms: list[str],
) -> set:
    pattern = r"|".join(map(re.escape, terms))
    mask = (
        df_venn["Index Keywords"]
        .fillna("")
        .str.contains(pattern, case=False, regex=True)
        | df_venn["Author Keywords"]
        .fillna("")
        .str.contains(pattern, case=False, regex=True)
        # df_venn['Abstract'].fillna('').str.contains(pattern, case=False, regex=True)
    )
    return set(df_venn.loc[mask, "EID"])


set1 = helper(
    terms=[
        "ontolog",
        # "semantic",
        # "knowledge graph"
    ]
)

set2 = helper(terms=["transport"])

set3 = helper(
    terms=[
        "decarbonis",
        # "sustain",
    ]
)

set4 = helper(
    terms=[
        "digital twin",
    ]
)

venny4py(
    sets={
        "Ontology": set1,
        "Transport": set2,
        "Decarbonisation": set3,
        "Digital Twin": set4,
    },
    out="./../artifacts/",
)

# plt.show()
plt.savefig("./../artifacts/venn4.pdf")
