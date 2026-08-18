"""
This script produces the pie chart summarising the W3C status of the studies.
"""

#%%
from matplotlib import pyplot as plt

from survey_paper_helpers.utils import load_studies_against_definitions_df

#%% Load the crosschecked studies.
df = load_studies_against_definitions_df()

# Remove the out of scope studies.
out_of_scope = [
    "bouchereauSemanticAnnotationResources2017a",
    "masekResearchPassengersDemand2018a",
    "gaudet-blavignacNationalSemanticdrivenThreepillar2021a",
    "zhangUseComparativeQuantitative2017a",
    "shellerTheorizingMobilityJustice2018a",
    "kimbrellElectricCarsharingSustainable2021a",
    "denissenRequirementsCorrosionInhibitor2022",
    "parkChangingIslandSociety2022a",
    # "benesKnowledgeGraphsTransport2023a",
    # "palSupplyChainInformation2023",
    # "asgariOntologyResilienceSustainability2025a",
    # "liuBridgingDataSilos2025a",
    "tomassiHealthcareSupplyChain2025a",
    "juEmbodiedEnergyEmergy2011",
    "wozniakEverydayProblemsVs2012a",
    "watanabeEstimatingQOLCar2023a"
]

df = df[~df["Study"].isin(out_of_scope)]

#
df_w3c = df[df["W3C"] == 1]
df_not_w3c = df[df["W3C"] == 0]

# Set up the figure parameters.
plt.rcParams.update({"font.size": 7})
width_mm = 89
height_mm = 89
width_inches = width_mm / 25.4
height_inches = height_mm / 25.4

#%% Testing the figure
w3c_count = len(df_w3c)
non_w3c_count = len(df_not_w3c)

artefact_available = df_w3c["Artefact"].value_counts().get(1, 0)
artefact_unavailable = df_w3c["Artefact"].value_counts().get(0, 0)

fig, ax = plt.subplots(
    figsize=(width_inches, width_inches),
    dpi=300,
)

# Outer ring
ax.pie(
    [non_w3c_count, w3c_count],
    radius=1.0,
    labels=[
        f"Non-W3C\n(n={non_w3c_count})",
        f"W3C\n(n={w3c_count})",
    ],
    colors=["#d9d9d9", "#4e79a7"],
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor="white"),
)

# Inner ring
ax.pie(
    [
        non_w3c_count,          # hidden
        artefact_available,
        artefact_unavailable,
    ],
    radius=0.7,
    labels=[
        "",
        f"Artefact\n(n={artefact_available})",
        f"No Artefact\n(n={artefact_unavailable})",
    ],
    colors=[
        "white",      # hidden sector
        "#59a14f",
        "#e15759",
    ],
    # labeldistance=1,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor="white"),
)

ax.set(aspect="equal")

plt.tight_layout()
plt.savefig("./../artefacts/Figure_W3C_Summary.pdf", dpi=300, transparent=True)