# Survey Paper

Python code to aid the survey paper. In particular, it produces the figures for the methodology.

## Installation
1. Clone the repository. 
2. Set up a local Python `venv`. (For instructions on how to do this, please refer to [this tutorial](https://realpython.com/python-virtual-environments-a-primer/).) 
3. Run the following to install the dependencies:
```bash
pip install -e .
```

## Source Code
The source code is located in the [`src/survey_paper_helpers/`](src/survey_paper_helpers) folder. This is where the exported Scopus data is stored, and all functionality. Visit [`utils.py`](src/survey_paper_helpers/utils.py) to see the keywords selected for each pillar.

## Scripts
The scripts use the source code to produce artifacts, and are located in the [`scripts/`](scripts) folder. You can run these separately. Feel free to add and tinker.

- [`extract_keywords.py`](scripts/extract_keywords.py) - Extracts all the Scopus index keywords from the studies.
- [`extract_relevant_papers.py`](scripts/extract_relevant_papers.py) - Extracts relevant papers based on the keywords.
- [`venn3.py`](scripts/venn3.py) - Produces the Venn diagram.
- [`word_cloud.py`](scripts/word_cloud.py) - Produces the word cloud.

## Artifacts

- [`CategorisedPapers.csv`](artifacts/CategorisedPapers.csv) - A table of all 222 studies, with boolean columns stating if they have been categorised as one of the pillars.
- [`Papers.csv`](artifacts/Keywords.csv) - A table of all keywords, and the frequency they appear at.