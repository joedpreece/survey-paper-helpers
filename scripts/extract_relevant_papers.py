"""
This script identifies relevant studies for each pillar using keyword matching.
The results are saved as a CSV file for further use.
"""

#%%
from survey_paper_helpers.utils import (
    load_data,
    TRANSPORTATION_TERMS,
    DECARBONISATION_TERMS,
    ONTOLOGY_TERMS,
    SEMANTIC_WEB_TERMS,
    KNOWLEDGE_GRAPH_TERMS,
    LINKED_DATA_TERMS,
    COMBINED_SEMANTIC_TERMS, get_eids_with_keywords, create_latex_citation_command,
)

# Load the Scopus extracted data.
df = load_data()

set_eids_decarbonisation = get_eids_with_keywords(DECARBONISATION_TERMS)
set_eids_transportation = get_eids_with_keywords(TRANSPORTATION_TERMS)
set_eids_combined_semantic = get_eids_with_keywords(COMBINED_SEMANTIC_TERMS)

set_ontology = get_eids_with_keywords(ONTOLOGY_TERMS)
set_semantic_web = get_eids_with_keywords(SEMANTIC_WEB_TERMS)
set_knowledge_graph = get_eids_with_keywords(KNOWLEDGE_GRAPH_TERMS)
set_linked_data = get_eids_with_keywords(LINKED_DATA_TERMS)

# Create a new column to say if the category is relevant for each paper.
df["transportation"] = df.index.isin(set_eids_transportation)
df["decarbonisation"] = df.index.isin(set_eids_decarbonisation)
df["semantic_web"] = df.index.isin(set_eids_combined_semantic)

# Calculate the sum of the relevance scores for each paper.
df["relevance"] = df["transportation"].astype(int) + df["decarbonisation"].astype(int) + df["semantic_web"].astype(int)

# Create a new column to say if the category is relevant for each paper.
df["semantic:ontology"] = df.index.isin(set_ontology)
df["semantic:semantic_web"] = df.index.isin(set_semantic_web)
df["semantic:knowledge_graph"] = df.index.isin(set_knowledge_graph)
df["semantic:linked_data"] = df.index.isin(set_linked_data)

# Save the results to a CSV file.
df.to_csv("./../artifacts/CategorisedPapers.csv")

df = df.sort_values(by="Year", ascending=True)

df_none = df[~df["transportation"] & ~df["semantic_web"] & ~df["decarbonisation"]]

df_d = df[~df["transportation"] & ~df["semantic_web"] & df["decarbonisation"]]
df_t = df[df["transportation"] & ~df["semantic_web"] & ~df["decarbonisation"]]
df_s = df[~df["transportation"] & df["semantic_web"] & ~df["decarbonisation"]]

df_st = df[df["transportation"] & df["semantic_web"] & ~df["decarbonisation"]]
df_dt = df[df["transportation"] & ~df["semantic_web"] & df["decarbonisation"]]
df_ds = df[~df["transportation"] & df["semantic_web"] & df["decarbonisation"]]

df_st_ontology = df[df["semantic:ontology"] & df["transportation"] & ~df["decarbonisation"]]
df_st_semantic_web = df[df["semantic:semantic_web"] & df["transportation"] & ~df["decarbonisation"]]
df_st_knowledge_graph = df[df["semantic:knowledge_graph"] & df["transportation"] & ~df["decarbonisation"]]
df_st_linked_data = df[df["semantic:linked_data"] & df["transportation"] & ~df["decarbonisation"]]

df_dst = df[df["transportation"] & df["semantic_web"] & df["decarbonisation"]]

# %% Create the citation commands
command_none = create_latex_citation_command(df_none)

command_d = create_latex_citation_command(df_d)
command_t = create_latex_citation_command(df_t)
command_s = create_latex_citation_command(df_s)

command_st = create_latex_citation_command(df_st)
command_dt = create_latex_citation_command(df_dt)
command_ds = create_latex_citation_command(df_ds)

command_st_ontology = create_latex_citation_command(df_st_ontology)
command_st_semantic_web = create_latex_citation_command(df_st_semantic_web)
command_st_knowledge_graph = create_latex_citation_command(df_st_knowledge_graph)
command_st_linked_data = create_latex_citation_command(df_st_linked_data)

command_dst = create_latex_citation_command(df_dst)