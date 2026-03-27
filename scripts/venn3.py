from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from survey_paper_helpers.utils import (
    get_papers_from_keywords,
    COMBINED_SEMANTIC_TERMS,
    TRANSPORTATION_TERMS,
    DECARBONISATION_TERMS,
)

# Get the EIDs of the papers that contain all the keywords for the different categories.
set1 = set(get_papers_from_keywords(COMBINED_SEMANTIC_TERMS).index)
set2 = set(get_papers_from_keywords(TRANSPORTATION_TERMS).index)
set3 = set(get_papers_from_keywords(DECARBONISATION_TERMS).index)

# df_subset = df[df.index.isin(set1 | set2 | set3)]
#
# df_123 = df[df.index.isin(set1 & set2 & set3)]

# Plot the Venn diagram.
plt.figure(figsize=(8, 8))
venn3([set1, set2, set3], ("Ontology", "Transport", "Decarbonisation"))

plt.savefig("./../artifacts/venn3.pdf")
# plt.show()
