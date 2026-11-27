# Survey Paper Helpers
This repository provides the Python code for the methodology of the survey paper.

[![DOI](https://zenodo.org/badge/github/1189506638.svg)](https://doi.org/10.5281/zenodo.24591436)

## Installation
1. Clone the repository. 
2. Set up a local Python `venv`. (For instructions on how to do this, please refer to [this tutorial](https://realpython.com/python-virtual-environments-a-primer/).) 
3. Run the following to install the source code and dependencies:
    ```bash
    pip install -e .
    ```

## Source Code
The source code is located in the [`src/survey_paper_helpers/`](src/survey_paper_helpers) folder. This is where the exported Scopus data is stored, and all functionality is coded. Visit [`utils.py`](src/survey_paper_helpers/utils.py) to see the keywords selected for each pillar.

## Scopus Data
We used the following search string to identify relevant papers on [Scopus](https://www.scopus.com/pages/home#basic):
```
TITLE-ABS-KEY ( 
        ( 
            ontolog* 
        OR  "knowledge graph" 
        OR  semantic* 
    ) 
    AND ( transport* ) 
    AND ( 
            decarbonis* 
        OR  sustain* 
        OR  "net zero" 
        OR  carbon 
    ) 
    AND NOT gene* 
) 
AND PUBYEAR > 2007 
AND PUBYEAR < 2026 
AND ( 
        LIMIT-TO ( DOCTYPE , "ar" ) 
    OR  LIMIT-TO ( DOCTYPE , "cp" ) 
    OR  LIMIT-TO ( DOCTYPE , "ch" ) 
    OR  LIMIT-TO ( DOCTYPE , "re" ) 
) 
AND ( 
        LIMIT-TO ( LANGUAGE , "English" )
)
```
We extracted the [results](src/survey_paper_helpers/data/scopus_export_Mar%2026-2026_2af2e3af-4c3f-46f6-91d5-44e7ce63ed11.csv) on `2026-03-26`, using the following steps:
1. Run the search query
2. Export the results as a CSV file.
   1. Select the `Export` button.
   2. Under `File types`, select `CSV`..
   3. Select `Documents 1 –` and put in 222.
   4. Ensure all options under `Citation information` are selected.
   5. Ensure all options under `Abstract & keywords` are selected.
   6. Select `Export` and save the file.

## Scripts
The scripts use the source code to produce artefacts, and are located in the [`scripts/`](scripts) folder. You can run these separately. Feel free to add and tinker.

- [check_no_indexed_keywords.py](scripts/check_no_indexed_keywords.py) - Checks how many studies have no indexed keywords.
- [extract_keywords.py](scripts/extract_keywords.py) - Extracts all the Scopus index keywords from the studies.
- [extract_relevant_papers.py](scripts/extract_relevant_papers.py) - Extracts relevant papers based on the keywords.
- [produce_pie_chart.py](scripts/produce_pie_chart.py) - Produces the pie chart in the discussion.
- [produce_summary_table.py](scripts/produce_summary_table.py) - Produces the summary table for the discussion.
- [produce_venn3.py](scripts/produce_venn3.py) - Produces the Venn diagram.
- [produce_wordcloud.py](scripts/produce_wordcloud.py) - Produces the word cloud.
- [produce_years_vs_number_of_papers.py](scripts/produce_years_vs_number_of_papers.py) - Produces the years vs number of papers plot.

## Artefacts

- [CategorisedPapers.csv](artefacts/CategorisedPapers.csv) - A table of all 222 studies, with boolean columns stating if they have been categorised as one of the pillars.
- [Keywords.csv](artefacts/Keywords.csv) - A table of all keywords, and the frequency they appear at.
- [SummaryTable.csv](artefacts/SummaryTable.csv) - Summarises the results against each region.
