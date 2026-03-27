"""
This script loads the dataset, identifies relevant papers for each predefined category using
keyword matching, and computes a relevance score for each paper based on its membership across
the categories. The results are saved as a CSV file for further use.
"""

from survey_paper_helpers.utils import (
    get_papers_from_keywords,
    load_data,
    TRANSPORTATION_TERMS,
    DECARBONISATION_TERMS,
    ONTOLOGY_TERMS,
    SEMANTIC_WEB_TERMS,
    KNOWLEDGE_GRAPH_TERMS,
    LINKED_DATA_TERMS,
    COMBINED_SEMANTIC_TERMS,
)

# Load the data.
df = load_data()

# Get the EIDs of the papers that contain the keywords.
set_transport = set(get_papers_from_keywords(TRANSPORTATION_TERMS).index)
set_decarbonisation = set(get_papers_from_keywords(DECARBONISATION_TERMS).index)
set_combined_semantic = set(get_papers_from_keywords(COMBINED_SEMANTIC_TERMS).index)

set_ontology = set(get_papers_from_keywords(ONTOLOGY_TERMS).index)
set_semantic_web = set(get_papers_from_keywords(SEMANTIC_WEB_TERMS).index)
set_knowledge_graph = set(get_papers_from_keywords(KNOWLEDGE_GRAPH_TERMS).index)
set_linked_data = set(get_papers_from_keywords(LINKED_DATA_TERMS).index)

# Create a new column to say if the category is relevant for each paper.
df["transportation"] = df.index.isin(set_transport)
df["decarbonisation"] = df.index.isin(set_decarbonisation)
df["semantic_web"] = df.index.isin(set_combined_semantic)

# Calculate the sum of the relevance scores for each paper.
df["relevance"] = df["transportation"].astype(int) + df["decarbonisation"].astype(int) + df["semantic_web"].astype(int)

# Create a new column to say if the category is relevant for each paper.
df["semantic:ontology"] = df.index.isin(set_ontology)
df["semantic:semantic_web"] = df.index.isin(set_semantic_web)
df["semantic:knowledge_graph"] = df.index.isin(set_knowledge_graph)
df["semantic:linked_data"] = df.index.isin(set_linked_data)

# Save the results to a CSV file.
df.to_csv("./../artifacts/CategorisedPapers.csv")

# df_ontology = df[df.index.isin(set_ontology & set_transport & set_decarbonisation)]
#
# df_semantic_web = df[
#     df.index.isin(set_semantic_web & set_transport & set_decarbonisation)
# ]
# df_knowledge_graph = df[
#     df.index.isin(set_knowledge_graph & set_transport & set_decarbonisation)
# ]
# df_linked_data = df[
#     df.index.isin(set_linked_data & set_transport & set_decarbonisation)
# ]
