import re

import pandas as pd
import importlib.resources as resources
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase

DECARBONISATION_TERMS = [
    # "Carbon",
    # "carbon",
    # "Carbon dioxide",
    # "carbon dioxide",
    "Carbon dioxide emissions",
    "carbon emission",
    "Carbon footprint",
    # "carbon 11",
    # "carbon 14",
    # "Carbon A",
    # "carbon monoxide",
    # "carbon monoxide dehydrogenase",
    # "carbon dioxide tension",
    "CO2 emissions",
    "Decarbonisation",
    "Low-carbon",
    "Low-carbon emissions",
    "Low-carbon energy systems",
    "Low carbon energies",
    "Low carbon economy",
    # "Carbon cycle",
    # "carbon cycle",
    # "Carbon pool",
    # "Carbon cycling",
    # "Soil carbon",
    # "soil carbon",
    # "Soil carbon cycling",
    # "particulate organic carbon",
    "carbon utilization",
    # "carbon fiber",
    # "Carbon fibers",
    "Carbon emissions",
    "Carbon credits"
]

TRANSPORTATION_TERMS = [
    "Urban transportation",
    "Motor transportation",
    "Roads and streets",
    "Sustainable mobility",
    "Traffic congestion",
    "Vehicles",
    "transportation planning",
    "urban transport",
    "Intelligent vehicle highway systems",
    "transportation system",
    "Street traffic control",
    "Railroads",
    "Transportation",
    "Railroad transportation",
    "railway transport",
    "Intelligent transportation systems",
    "Traffic control",
    "Sustainable transportation",
    "Urban mobility",
    "Highway traffic control",
    "Transportation system",
    "Mass transportation",
    "Public transport",
    "Sustainable transport",
    "Public transportation",
    "transportation infrastructure",
    "traffic management",
    "Transport infrastructure",
    "traffic and transport",
    "Freight transportation",
    "Public transit",
    "transportation safety",
    "Autonomous vehicles",
    "mobility",
    "Autonomous Vehicles",
    "Road network",
    "maritime transportation",
    "Transportation routes",
    "Urban freight transport",
    "Traffic signals",
    "Light rail transit",
    "Smart mobility",
    "Advanced traffic management systems",
    "Smart transportation",
    "Vehicle detection",
    "Mobility datum",
    "railway",
    "Multimodal transportation",
    "Mobility",
    "Road extraction",
    "Autonomous vehicle technologies",
    "public transport",
    "Electric vehicles",
    "road transport",
    "Road transport systems",
    "Railroad accidents",
    "Air transportation",
    "Micro-mobility",
    "intelligent transportation system",
    "Urban transportation systems",
    "Transport performance",
    "Transport analysis",
    "Transportation distribution",
    "traffic emission",
    "Transport emissions",
    "Transport modelling",
    "Transportation process",
    "Transport operations",
    "Automotive transport",
    "Public transit networks",
    "Road type",
    "Vulnerable road user",
    "Road users",
    "Road intersections",
    "transportation",
    "Traffic demands",
    "Transportation strategies",
    "air traffic control",
    "Rapid transit",
    "road construction",
    "Carrier mobility",
    "Transportation mode prediction",
    "Transportation mode",
    "Vehicles detection",
    "Traffic surveillance",
    "Traffic networks",
    "transport at the cellular level",
    "Road monitoring",
    "Non-motor vehicle",
    "Motorized vehicles",
    "Motor vehicle",
    "Nonmotorized transportation",
    "Vehicle locating systems",
    "Urban rail transit",
    "Human mobility",
    "Emergency vehicles",
    "Light rail transit (LRT)",
    "Public transport management",
    "protein transport",
    "Intermodal transportation",
    "Traffic",
    "Road transportation",
    "Intermodal transport",
    "public transportation",
    "Traffic lanes",
    "Multi-modal transportation systems",
    "Transport strategies",
    "Smart transport strategy",
    "electric vehicle",
    "Transportation planning",
    "Transport resources",
    "transportation mode",
    "transportation technology",
    "cycle transport",
    "Transport cards",
    "Private transportation",
    "Road traffic",
    "Vehicle system",
    "transportation policy",
    "Traffic safety",
    "Traffic management strategies",
    "Traffic management",
    "Air traffic control",
    "freight transport",
    "Transport process",
    "Intelligent transport systems",
    "Urban transit system",
    "Public transit behavior",
    "Road traffic injuries",
    "Road fatalities",
    "Gravel road detection and extraction",
    "Gravel road condition monitoring",
    "Forest road networks",
    "Forest and rural road network monitoring",
    "transportation development",
    "Urban traffic management",
    "Transport operators",
    "Traffic signal control",
    "Mobility service",
    "Gravel roads",
    "Road detection",
    "Road condition monitoring",
    "Traffic speed",
    "Traffic prediction",
    "Transport security",
    "Traffic restrictions",
    "Public transportation services",
    "patient transport",
    "Sustainable transportation systems",
    "Electric Vehicles (EVs)",
    "Electric mobility",
    "Real world road networks",
    "Vehicle efficiency",
    "Transportation sustainability",
    "Transportation efficiency",
    "Vehicles collision",
    "Unmanned aerial vehicles (UAV)",
    "unmanned vehicle",
    "Electric vehicle charging infrastructures",
    "Battery-electric vehicles",
    "traffic congestion",
    "Road traffic management",
    "social mobility",
    "Futuristic vehicle",
    "Electric vehicle charging",
    "Road construction",
    "Railway transportation",
    "Railway track",
    "Global mobility",
    "Railroad tracks",
    "Transport networks",
    "Transport",
    "Seamless mobility",
    "Road pixels",
    "Automatic road extraction",
    "Transportation services",
    "Transportation fleet",
    "Transport and mobilities",
    "Transport research",
    "Railway construction",
    "Heavy haul railway",
    "Urban transit",
    "Mobility predictions",
    "Mobility graphs",
    "Mobility behavior",
    "Explainable mobility graph",
    "Taiwan high speed rails",
    "High speed rail",
    "Railway infrastructure",
    "Transportation infrastructures",
    "Vehicle technology",
    "Production and transportations",
    "Air transport",
    "Employee mobility",
    "Mobility budget",
    "Green logistics",
]

ONTOLOGY_TERMS = [
    "Ontology",
    "Ontology's",
    "Ontology-based",
    "Formal ontology",
    "Core ontology",
    "Smart city ontology",
    "Emergy ontology",
    "Ontology mapping",
    "Ontology design",
    "Ontology engineering",
    "Ontology-guided modeling",
    "Knowledge ontology",
]

SEMANTIC_WEB_TERMS = [
    "Semantic Web",
    "Semantic Web technology",
    "Semantic technologies",
    "Semantic Web rule language (SWRL)",
    "RDF",
]

KNOWLEDGE_GRAPH_TERMS = [
    "Knowledge graphs",
    "Knowledge graph",
]

LINKED_DATA_TERMS = [
    "Linked open datum",
    "Linked open data (LOD)",
    "Linked datum",
    "Linked data",
    "Linked data fragment",
]

COMBINED_SEMANTIC_TERMS = (
    ONTOLOGY_TERMS + SEMANTIC_WEB_TERMS + KNOWLEDGE_GRAPH_TERMS + LINKED_DATA_TERMS
)

def __load_bibtex() -> BibDatabase:
    """
    Loads the bibtex bibliography file.
    :return: A bibtex database containing the bibliography entries.
    """

    with (
        resources.files("survey_paper_helpers.data")
        .joinpath(
            "references.bib"
        )
        .open("r") as f
    ):
        bib_db = bibtexparser.load(f)

    return bib_db


def load_data() -> pd.DataFrame:
    """
    Loads the extracted Scopus CSV file and performs some basic preprocessing.

    :return: A pandas DataFrame containing the processed survey data.
    :rtype: pandas.DataFrame
    """
    # Load the CSV.
    with (
        resources.files("survey_paper_helpers.data")
        .joinpath(
            # "scopus_export_Jan 9-2026_19a095d2-8a21-46fc-8196-1d2e1f3d1199.csv"
            "scopus_export_Mar 26-2026_2af2e3af-4c3f-46f6-91d5-44e7ce63ed11.csv"
        )
        .open("r") as f
    ):
        df = pd.read_csv(f)

    # Set the index to the EID.
    df = df.set_index("EID")

    # Load the bibtex database and extract the titles and DOIs.
    bib_db = __load_bibtex()

    bib_lookup = {}
    for entry in bib_db.entries:
        key = entry["ID"]

        if "doi" in entry:
            bib_lookup[entry["doi"].lower()] = key
        elif "title" in entry:
            bib_lookup[entry["title"].lower()] = key

    # Add a new column to the DataFrame with the bibtex key.
    def lookup_bibkey(row):
        if pd.notna(row["DOI"]):
            key = bib_lookup.get(row["DOI"].lower())
            if key:
                return key

        title = row["Title"].lower()
        return bib_lookup.get(title)

    df["bibtex_key"] = df.apply(lookup_bibkey, axis=1)

    # Deal with some of the edge cases!
    df.loc[
        "2-s2.0-84858691157", "bibtex_key"] = "pillmannMetamodellingEuropeanEnvironmental2010"
    df.loc["2-s2.0-85029034008", "bibtex_key"] = "burghardtDevelopingOntologyK122010a"
    df.loc[
        "2-s2.0-84905721438", "bibtex_key"] = "koblerDesigningInterpersonalPersuasion2013a"
    df.loc["2-s2.0-84891273882", "bibtex_key"] = "kelpinUsingDublinCore2013a"
    df.loc["2-s2.0-84926314925", "bibtex_key"] = "consoliEmergencyVehicleRouting2014a"
    df.loc[
        "2-s2.0-84912567480", "bibtex_key"] = "houOntologybasedSemanticModelling2014a"
    df.loc[
        "2-s2.0-84975740642", "bibtex_key"] = "khalilModelResearchEntrepreneurial2015a"
    df.loc["2-s2.0-105018631710", "bibtex_key"] = "tomassiHealthcareSupplyChain2025a"
    df.loc[
        "2-s2.0-105016776176", "bibtex_key"] = "treviranusFacialEmotionalFeedback2025a"

    # Convert the keyword columns into lists.
    df["Index Keywords"] = df["Index Keywords"].str.split("; ")
    df["Author Keywords"] = df["Author Keywords"].str.split("; ")

    return df


def load_categorised_data() -> pd.DataFrame:

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
    df["relevance"] = df["transportation"].astype(int) + df["decarbonisation"].astype(
        int) + df["semantic_web"].astype(int)

    # Create a new column to say if the category is relevant for each paper.
    df["semantic:ontology"] = df.index.isin(set_ontology)
    df["semantic:semantic_web"] = df.index.isin(set_semantic_web)
    df["semantic:knowledge_graph"] = df.index.isin(set_knowledge_graph)
    df["semantic:linked_data"] = df.index.isin(set_linked_data)

    return df


def load_keywords() -> pd.DataFrame:

    df = load_data()

    df = df.explode(column=["Author Keywords"])
    df = df.explode(column=["Index Keywords"])

    return df[["Author Keywords", "Index Keywords"]]


def load_scopus_indexed_keywords() -> pd.DataFrame:
    """
    Loads the Scopus indexed keywords from the CSV file.

    :return: A pandas DataFrame containing all the Scopus indexed keywords for each study.
    """

    # Load the dataset.
    df = load_data()

    # Explode the keyword columns into separate rows.
    df = df.explode(column=["Index Keywords"])

    return df.loc[:, ["Index Keywords"]].copy()


def __get_eids_from_keywords(keywords: list[str]) -> set:

    df = load_scopus_indexed_keywords()

    df = df[df["Index Keywords"].isin(keywords)]

    df = df[~df.index.duplicated(keep="first")]

    return set(df.index)

def __get_eids_from_abstract(keywords: list[str]) -> set:
    pattern = r"|".join(map(re.escape, keywords))

    df = load_data()

    df = df[df["Index Keywords"].isna()]

    mask = (
        df["Abstract"]
        .fillna("")
        .str.contains(pattern, case=False, regex=True)
    )
    return set(df.loc[mask].index)

def get_eids_with_keywords(keywords: list[str]) -> set:
    """
    Returns a set of the EIDs of the papers that match with the provided keywords.

    :param keywords: The keywords to check against.
    :return: A set of EIDs that match against the keywords.
    """

    return (
            __get_eids_from_keywords(keywords)
            | __get_eids_from_abstract(keywords)
    )


def create_latex_citation_command(df: pd.DataFrame) -> str:
    """
    Creates a LaTeX citation command for all studies within the provided dataframe.

    :param df: The dataframe containing the studies.
    :return: A LaTeX citation command for all studies.
    """

    keys = (
        df["bibtex_key"].fillna("empty").astype(str)
    )

    return r"\cite{" + ",".join(keys) + "}"


def load_studies_against_definitions_df() -> pd.DataFrame:
    """
    Load a table of the studies that have been crosschecked against the definitions.
    """

    with (
        resources.files("survey_paper_helpers.data")
        .joinpath(
            "crosscheck.csv"
        )
        .open("r") as f
    ):
        df = pd.read_csv(f)

    df = df.iloc[0:, 4:]

    df.columns = [
        "Study",
        "Ontology",
        "Knowledge Graph",
        "OWL Ontology",
        "RDF Knowledge Graph",
        # "Taxonomy",
        # "Linked Data",
        "Artefact"
    ]

    df["Study"] = df["Study"].str.replace(r"\\textcite{", "", regex=True)
    df["Study"] = df["Study"].str.replace(r"\\mbox{", "", regex=True)
    df["Study"] = df["Study"].str.replace(r"\\sout{", "", regex=True)
    df["Study"] = df["Study"].str.replace(r"}", "", regex=True)

    df = df.drop_duplicates(subset="Study")

    cols = list(df.columns)[1:]

    df[cols] = (
        df[cols]
        .replace(r'\\checkmark', 1, regex=True)
        .fillna(0)
        .astype(int)
    )

    df["W3C"] = df["OWL Ontology"] | df["RDF Knowledge Graph"]

    return df