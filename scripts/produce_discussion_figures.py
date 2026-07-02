#%%
import pandas as pd
from matplotlib import pyplot as plt

from survey_paper_helpers.utils import load_studies_against_definitions_df

df = load_studies_against_definitions_df()

#%% Remove the out of scope papers
out_of_scope = [
    "bouchereauSemanticAnnotationResources2017a",
    "masekResearchPassengersDemand2018a",
    "gaudet-blavignacNationalSemanticdrivenThreepillar2021a",
    "zhangUseComparativeQuantitative2017a",
    "shellerTheorizingMobilityJustice2018a",
    "kimbrellElectricCarsharingSustainable2021a",
    "denissenRequirementsCorrosionInhibitor2022",
    "parkChangingIslandSociety2022a",
    "benesKnowledgeGraphsTransport2023a",
    "palSupplyChainInformation2023",
    "asgariOntologyResilienceSustainability2025a",
    # "liuBridgingDataSilos2025a",
    "tomassiHealthcareSupplyChain2025a",
    "juEmbodiedEnergyEmergy2011",
    "wozniakEverydayProblemsVs2012a",
    "watanabeEstimatingQOLCar2023a"
]

df = df[~df["Study"].isin(out_of_scope)]

df_w3c = df[df["W3C"] == 1]
df_not_w3c = df[df["W3C"] == 0]

plt.rcParams.update({"font.size": 7})

# %% Produce the artefact plot
v = df["Artefact"].value_counts()

v = v.rename(
    {0: "Artefact Unavailable", 1: "Artefact Available"}
)

width_mm = 89
height_mm = 89
width_inches = width_mm / 25.4
height_inches = height_mm / 25.4

fig, ax = plt.subplots(
    figsize=(width_inches, width_inches * (2/3)),
    dpi=300,
)

v.plot.pie(autopct="%1.0f%%", startangle=90, ax=ax)
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("./../artifacts/Figure_Artefact_Status.pdf", dpi=300, transparent=True)

# %%
v = df["W3C"].value_counts(normalize=True).mul(100).round(0)

v = v.rename(
    {0: "Non W3C", 1: "W3C"}
)

width_mm = 89
height_mm = 89
width_inches = width_mm / 25.4
height_inches = height_mm / 25.4

fig, ax = plt.subplots(
    figsize=(width_inches, width_inches * (2/3)),
    dpi=300,
)

v.plot.pie(autopct="%1.0f%%", startangle=90, ax=ax)
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("./../artifacts/Figure_W3C_Status.pdf", dpi=300, transparent=True)

# %%
width_mm = 89
height_mm = 89
width_inches = width_mm / 25.4
height_inches = height_mm / 25.4

fig, ax = plt.subplots(
    figsize=(width_inches, width_inches),
    dpi=300,
)

cols = ["OWL Ontology", "RDF Knowledge Graph", "Linked Data"]
# "Ontology", "Knowledge Graph", "Taxonomy"

plot_df = (
    pd.concat(
        {
            col: df_w3c[col].value_counts()
            for col in cols
        },
        axis=1
    )
    .T
)

plot_df.plot(
    kind="bar",
    ax=ax,
)

ax.set_ylabel("Number of Studies")
ax.set_xlabel("")
plt.legend(title="Response")
plt.tight_layout()
plt.show()

# %%

width_mm = 89
height_mm = 89
width_inches = width_mm / 25.4
height_inches = height_mm / 25.4

fig, ax = plt.subplots(
    figsize=(width_inches, width_inches),
    dpi=300,
)

# cols = ["OWL Ontology", "RDF Knowledge Graph", "Linked Data"]
cols = ["Ontology", "Knowledge Graph", "Taxonomy"]

plot_df = (
    pd.concat(
        {
            col: df_not_w3c[col].value_counts()
            for col in cols
        },
        axis=1
    )
    .T
)

plot_df.plot(
    kind="bar",
    ax=ax,
)

ax.set_ylabel("Number of Studies")
ax.set_xlabel("")
plt.legend(title="Response")
plt.tight_layout()
plt.show()


# %%
df_w3c["RDF Knowledge Graph"].value_counts(normalize=True).mul(100).round(0)

# %%
df_w3c["Linked Data"].value_counts(normalize=True).mul(100).round(0)

# %%
df_not_w3c["Taxonomy"].value_counts(normalize=True).mul(100).round(0)

# %%
df_not_w3c["Ontology"].value_counts(normalize=True).mul(100).round(0)

# %%
df_not_w3c["Knowledge Graph"].value_counts(normalize=True).mul(100).round(0)

