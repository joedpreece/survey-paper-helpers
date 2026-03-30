from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from survey_paper_helpers.utils import (
    get_papers_from_keywords,
    COMBINED_SEMANTIC_TERMS,
    TRANSPORTATION_TERMS,
    DECARBONISATION_TERMS, load_data,
)

# Get the EIDs of the papers that contain all the keywords for the different categories.
set1 = set(get_papers_from_keywords(COMBINED_SEMANTIC_TERMS).index)
set2 = set(get_papers_from_keywords(TRANSPORTATION_TERMS).index)
set3 = set(get_papers_from_keywords(DECARBONISATION_TERMS).index)

set_all = set(load_data().index)
outside = set_all - (set1 | set2 | set3)

# df_subset = df[df.index.isin(set1 | set2 | set3)]
#
# df_123 = df[df.index.isin(set1 & set2 & set3)]

# Plot the Venn diagram.

plt.rcParams.update({
    'font.size': 5,
    'axes.labelsize': 5,
    'xtick.labelsize': 5,
    'ytick.labelsize': 5,
    'legend.fontsize': 5,
})


width_mm = 89
height_mm = 89
width_inches = width_mm / 25.4
height_inches = height_mm / 25.4

plt.figure(
    figsize=(width_inches, height_inches),
    dpi=300,
    facecolor="none",

)
venn3([set1, set2, set3], ("Semantic Web", "Transportation", "Decarbonisation"))

plt.text(0.1, -0.55, f"{len(outside)}", fontsize=5)

plt.tight_layout()
plt.savefig("./../artifacts/venn3.pdf", dpi=300, transparent=True)
# plt.show()
