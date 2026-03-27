import pandas as pd
import importlib.resources as resources

DECARBONISATION_TERMS = [
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

TRANSPORTATION_TERMS = [
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

ONTOLOGY_TERMS = [
    "Ontology",
    "Ontology's",
]

SEMANTIC_WEB_TERMS = [
    "Semantic Web",
    "Semantic Web technology",
]

KNOWLEDGE_GRAPH_TERMS = [
    "Knowledge graphs",
    "Knowledge graph",
]

LINKED_DATA_TERMS = [
    "Linked open datum",
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
