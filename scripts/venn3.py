#%% Word Frequencies
import re

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from survey_paper_helpers.utils import load_key_words, get_papers_from_keywords, \
    load_data

df = load_data()

df_venn = df.reset_index()

def helper(
        terms: list[str],
) -> set:
    pattern = r"|".join(map(re.escape, terms))
    mask = df_venn['Abstract'].fillna('').str.contains(pattern, case=False, regex=True)
    return set(df_venn.loc[mask, 'EID'])


decarbonisation_terms = [
    "Sustainable development",
    "sustainability",
    "Sustainable mobility",
    "Sustainable transport",
    "Sustainable transportation",
    "Carbon",
    "Carbon dioxide",
    "carbon emission",
    "Climate change",
    "Environmental protection",
    "Energy utilization",
    # "Urban mobility",
    # "Urban planning",
    # "Urban growth",
    # "urban area",
]

transportation_terms = [
    "Urban transportation",
    "Motor transportation",
    "Roads and streets",
    "Traffic congestion",
    "Vehicles",
    "transportation planning",
    "transportation system",
    "Intelligent vehicle highway systems",
    "Street traffic control",
    "Railroads",
    "Railroad transportation",
    "railway transport",
    "Intelligent transportation systems",
    "Highway traffic control",
    "Mass transportation",
    "Public transport",
    "Highway administration",
    "Traffic control",
    "Transportation system",
    "urban transport",
]

semantic_technology_terms = [
    # "Semantics",
    "Ontology",
    "Ontology's",
    "Semantic Web",
    "Knowledge graphs",
    "Knowledge graph",
    # "Semantic segmentation",
    # "Semantic Segmentation",
    # "Semantic interoperability",
    "Linked open datum",
    "Semantic Web technology",
    # "Metadata",
    # "Data integration",
    # "Data mining",
    # "Information management",
    # "Extraction",
    # "Open Data",
    # "Image segmentation",
]

set1 = set(get_papers_from_keywords(semantic_technology_terms).index)
set2 = set(get_papers_from_keywords(transportation_terms).index)
set3 = set(get_papers_from_keywords(decarbonisation_terms).index)

# set1 = helper(
#     terms=[
#         "ontolog",
#         # "semantic",
#         "knowledge graph"
#     ]
# )
#
# set2 = helper(
#     terms=[
#         "transport"
#     ]
# )
#
# set3 = helper(
#     terms=[
#         "decarbonis",
#         # "sustain",
#         # "net zero"
#     ]
# )
#
# set4 = helper(
#     terms=[
#         "twin",
#     ]
# )

df_subset = df[df.index.isin(set1 | set2 | set3)]

df_123 = df[df.index.isin(set1 & set2 & set3)]


plt.figure(figsize=(8, 8))
venn3([set1, set2, set3], ('Ontology', 'Transport', 'Decarbonisation'))

# plt.savefig("./../artifacts/venn3.pdf")
plt.show()