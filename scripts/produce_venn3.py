"""
This script generates the venn diagram for the different categories of the survey.
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

from scripts.extract_relevant_papers import set_semantic_web
from survey_paper_helpers.utils import (
    COMBINED_SEMANTIC_TERMS,
    TRANSPORTATION_TERMS,
    DECARBONISATION_TERMS, load_data, get_eids_with_keywords,
)

# Get the EIDs of the papers that contain all the keywords for the different categories.
set_S = get_eids_with_keywords(COMBINED_SEMANTIC_TERMS)
set_T = get_eids_with_keywords(TRANSPORTATION_TERMS)
set_D = get_eids_with_keywords(DECARBONISATION_TERMS)

set_all = set(load_data().index)
outside = set_all - (set_S | set_T | set_D)

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

v = venn3([set_S, set_T, set_D], ("Semantic Technologies (S)", "Transportation (T)", "Decarbonisation (D)"))


if v.get_label_by_id('100'):
    label = v.get_label_by_id('100')
    x, y = label.get_position()
    label.set_text(r"$\it{S}$" + f"\n{len(set_S - (set_T | set_D))}")

if v.get_label_by_id('010'):
    label = v.get_label_by_id('010')
    x, y = label.get_position()
    label.set_text(r"$\it{T}$" + f"\n{len(set_T - (set_S | set_D))}")

if v.get_label_by_id('001'):
    label = v.get_label_by_id('001')
    x, y = label.get_position()
    label.set_text(r"$\it{D}$" + f"\n{len(set_D - (set_T | set_S))}")
    label.set_position((x, y + 0.05))

if v.get_label_by_id('110'):
    label = v.get_label_by_id('110')
    x, y = label.get_position()
    label.set_text(r"$\bf{TS}$" + f"\n{len((set_S & set_T) - set_D)}")

if v.get_label_by_id('101'):
    label = v.get_label_by_id('101')
    x, y = label.get_position()
    label.set_text(r"$\bf{DS}$" + f"\n{len((set_D & set_S) - set_T)}")

if v.get_label_by_id('011'):
    label = v.get_label_by_id('011')
    x, y = label.get_position()
    label.set_text(r"$\it{TD}$" + f"\n{len((set_T & set_D) - set_S)}")

# if v.get_label_by_id('110'):
#     label = v.get_label_by_id('110')
#     x, y = label.get_position()
#     label.set_text(r"$\it{TS}$" + f"\n{len(set_S & set_T & set_D)}")
#     label.set_position((x, y + 0.1))

if v.get_label_by_id('111'):
    label = v.get_label_by_id('111')
    x, y = label.get_position()
    label.set_text(r"$\bf{TDS}$" + f"\n{len(set_S & set_T & set_D)}")
    label.set_position((x, y - 0.05))

plt.text(0.1, -0.6, r"$\it{N}$" + f"\n{len(outside)}", fontsize=5)

plt.tight_layout()
plt.savefig("./../artefacts/Figure_Venn3.pdf", dpi=300, transparent=True)
# plt.show()
