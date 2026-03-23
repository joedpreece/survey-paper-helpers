import pandas as pd
import importlib.resources as resources

def load_data() -> pd.DataFrame:

    # Load the CSV.
    with resources.files("survey_paper_helpers.data").joinpath(
            "scopus_export_Jan 9-2026_19a095d2-8a21-46fc-8196-1d2e1f3d1199.csv"
    ).open("r") as f:
        df = pd.read_csv(f)

    # Set the index to the EID.
    df = df.set_index("EID")

    # Split the keyword columns into lists.
    df['Index Keywords'] = df['Index Keywords'].str.split(';')
    df['Author Keywords'] = df['Author Keywords'].str.split(';')

    return df

def load_key_words() -> pd.DataFrame:

    df = load_data()

    df = df.explode(column=["Author Keywords"])
    df = df.explode(column=["Index Keywords"])

    return df[["Author Keywords", "Index Keywords"]]