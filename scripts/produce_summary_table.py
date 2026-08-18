#%% Imports
import pandas as pd
import numpy as np

from survey_paper_helpers.utils import load_studies_against_definitions_df, \
    load_categorised_data

#%% Load the crosschecked studies.
df_crosschecked = load_studies_against_definitions_df()

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
    "tomassiHealthcareSupplyChain2025a",
    "juEmbodiedEnergyEmergy2011",
    "wozniakEverydayProblemsVs2012a",
    "watanabeEstimatingQOLCar2023a"
]

df_crosschecked = df_crosschecked[~df_crosschecked["Study"].isin(out_of_scope)]

#%% Load the categorised studies and sort by year
df_categorised_studies = load_categorised_data()
df_categorised_studies = df_categorised_studies.sort_values(by="Year", ascending=True)

#%% Merge the dataframes
df_res = pd.merge(
    left=df_crosschecked,
    right=df_categorised_studies[["bibtex_key", "transportation", "semantic_web", "decarbonisation", "semantic:semantic_web", "semantic:ontology", "semantic:knowledge_graph", "semantic:linked_data"]],
    left_on="Study",
    right_on="bibtex_key",
    suffixes=("_survey", "_2"),
    how="inner",
)

#%%  Label the regions

conditions = [
    ~df_res["transportation"] & ~df_res["semantic_web"] & ~df_res["decarbonisation"],
    ~df_res["transportation"] & ~df_res["semantic_web"] &  df_res["decarbonisation"],
     df_res["transportation"] & ~df_res["semantic_web"] & ~df_res["decarbonisation"],
    ~df_res["transportation"] &  df_res["semantic_web"] & ~df_res["decarbonisation"],
     df_res["transportation"] &  df_res["semantic_web"] & ~df_res["decarbonisation"],
     df_res["transportation"] & ~df_res["semantic_web"] &  df_res["decarbonisation"],
    ~df_res["transportation"] &  df_res["semantic_web"] &  df_res["decarbonisation"],
     df_res["transportation"] &  df_res["semantic_web"] &  df_res["decarbonisation"],
]

choices = [
    "None",
    "D",
    "T",
    "S",
    "TS",
    "TD",
    "DS",
    "TDS",
]

df_res["Region"] = np.select(conditions, choices, default="Unknown")

#%%
# cols = [
#     "Ontology",
#     "Knowledge Graph",
#     "OWL Ontology",
#     "RDF Knowledge Graph",
# ]
#
# region_sizes = df_res.groupby("Region").size()
#
# summary = pd.DataFrame(index=region_sizes.index)
# summary["N"] = region_sizes
#
# for col in cols:
#     counts = df_res.groupby("Region")[col].sum()
#     pct = 100 * counts / region_sizes
#
#     summary[col] = (
#         counts.astype(int).astype(str)
#         + " ("
#         + pct.round(1).astype(str)
#         + r"\%)"
#     )
#
# print(summary)

#%% Create the summary table
cols = [
    "Ontology",
    "Knowledge Graph",
    "OWL Ontology",
    "RDF Knowledge Graph",
    "Artefact",
]

def make_row(label, subset):
    row = {
        "Region / Category": label,
        "N": len(subset),
    }

    for col in cols:
        count = subset[col].sum()
        pct = 100 * count / len(subset) if len(subset) else 0

        row[f"{col} (n)"] = int(count)
        row[f"{col} (%)"] = round(pct, 1)

    return row

rows = []

# Main regions
for region in ["TS", "DS", "TDS"]:
    subset = df_res[df_res["Region"] == region]
    rows.append(make_row(region, subset))

# TS subcategories
semantic_categories = {
    "semantic:semantic_web": "  Semantic Web",
    "semantic:ontology": "  Ontology",
    "semantic:knowledge_graph": "  Knowledge Graph",
}

for col, label in semantic_categories.items():
    subset = df_res[
        (df_res["Region"] == "TS")
        & (df_res[col])
    ]

    rows.append(make_row(label, subset))

summary = pd.DataFrame(rows)

print(summary)

summary.to_csv("./../artefacts/SummaryTable.csv")