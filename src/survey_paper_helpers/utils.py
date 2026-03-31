import pandas as pd
import importlib.resources as resources

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
    "Mobility budget"
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


def load_data() -> pd.DataFrame:
    """
    Loads survey data from a predefined CSV file, processes it to set the index to EID, and
    converts keyword columns into lists for further analysis.

    The function reads a CSV file packaged within the module and processes the data by joining
    it with the index EID column. Both the 'Index Keywords' and 'Author Keywords' columns are
    transformed from strings into lists based on a separator.

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

    # Convert the keyword columns into lists.
    df["Index Keywords"] = df["Index Keywords"].str.split("; ")
    df["Author Keywords"] = df["Author Keywords"].str.split("; ")

    return df


def load_key_words() -> pd.DataFrame:

    df = load_data()

    df = df.explode(column=["Author Keywords"])
    df = df.explode(column=["Index Keywords"])

    return df[["Author Keywords", "Index Keywords"]]


def load_index_key_words() -> pd.DataFrame:

    # Load the dataset.
    df = load_data()

    # Explode the keyword columns into separate rows.
    df = df.explode(column=["Index Keywords"])

    return df[["Index Keywords"]]


def get_papers_from_keywords(keywords: list[str]) -> pd.DataFrame:

    df = load_index_key_words()

    df = df[df["Index Keywords"].isin(keywords)]

    df = df[~df.index.duplicated(keep="first")]

    return df
