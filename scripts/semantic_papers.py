#%%
from survey_paper_helpers.utils import get_papers_from_keywords, load_data

df = load_data()

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

ontology_terms = [
    "Ontology",
    "Ontology's",
]

semantic_web_terms = [
    "Semantic Web",
    "Semantic Web technology",
]

knowledge_graph_terms = [
    "Knowledge graphs",
    "Knowledge graph",
]

linked_data_terms = [
    "Linked open datum",
]

set_transport = set(get_papers_from_keywords(transportation_terms).index)
set_decarbonisation = set(get_papers_from_keywords(transportation_terms).index)
set_ontology = set(get_papers_from_keywords(ontology_terms).index)
set_semantic_web = set(get_papers_from_keywords(semantic_web_terms).index)
set_knowledge_graph = set(get_papers_from_keywords(knowledge_graph_terms).index)
set_linked_data = set(get_papers_from_keywords(linked_data_terms).index)

df_ontology = df[df.index.isin(set_ontology & set_transport & set_decarbonisation)]
df_semantic_web = df[df.index.isin(set_semantic_web & set_transport & set_decarbonisation)]
df_knowledge_graph = df[df.index.isin(set_knowledge_graph & set_transport & set_decarbonisation)]
df_linked_data = df[df.index.isin(set_linked_data & set_transport & set_decarbonisation)]