"""
This script generates the venn diagram for the different categories of the survey.
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from survey_paper_helpers.utils import (
    COMBINED_SEMANTIC_TERMS,
    TRANSPORTATION_TERMS,
    DECARBONISATION_TERMS, load_data, get_eids_with_keywords,
)

# Get the EIDs of the papers that contain all the keywords for the different categories.
set1 = get_eids_with_keywords(COMBINED_SEMANTIC_TERMS)
set2 = get_eids_with_keywords(TRANSPORTATION_TERMS)
set3 = get_eids_with_keywords(DECARBONISATION_TERMS)

set_all = set(load_data().index)
outside = set_all - (set1 | set2 | set3)

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
plt.savefig("./../artifacts/Venn3.pdf", dpi=300, transparent=True)
# plt.show()
