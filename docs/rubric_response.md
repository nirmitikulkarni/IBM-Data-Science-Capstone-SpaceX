# Response to grading feedback (10/15; 67%)

The grader identified these main gaps: verified project repository contents/links; methodology coverage and verified execution evidence; incomplete Folium proximity evidence; and limitations in the report's methodology/results verification.

## Changes made after the feedback

- Verified the public repository and confirmed push permission.
- Added project scaffold, scripts, SQL, dashboard/map source, requirements and README.
- Added `data/dataset_part_2.csv` (90-record course dataset) with source attribution.
- Added a revised report PDF and project ZIP locally (download links in chat).
- The report now explicitly distinguishes report-derived results from newly verified evidence.

## Verification status

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Repository URL and project contents | **Addressed** | https://github.com/nirmitikulkarni/IBM-Data-Science-Capstone-SpaceX; main branch updated |
| Dataset availability | **Addressed** | `data/dataset_part_2.csv` committed; source documented |
| API collection | **Partial** | Script provided; needs actual run output/log |
| Web scraping | **Partial** | Script provided; needs actual run output and retrieval timestamp |
| Wrangling | **Partial** | Validation script provided; needs run and before/after evidence |
| EDA charts and interpretations | **Existing report evidence** | Original report retained; results should be rerun against included CSV |
| SQL analysis | **Existing report evidence** | Query file included; fresh query outputs not yet generated |
| Folium | **Partial** | Interactive HTML source/map scaffold; launch-level and infrastructure proximity evidence needs data and browser verification |
| Dash | **Partial** | App source included; run locally and capture a genuine browser screenshot |
| Predictive models | **Partial** | Original metrics preserved; not independently re-executed in this workspace |
| Precision/recall and confusion matrices | **Partial** | Existing confusion matrices; rerun models to produce full fresh metric table |
| Final consistency check | **Pending** | Align final PDF, ZIP and repository after execution evidence is captured |

## Reproduction

1. Install `requirements.txt`.
2. Run `python src/validate_dataset.py`.
3. Run `python src/analysis.py` (ensure it uses the committed CSV and saves outputs).
4. Run the SQL queries using SQLite after loading the dataset.
5. Run the Folium map generator.
6. Run Dash locally and save screenshots of the working interface.
7. Replace historical metrics and partial evidence in the report with the verified outputs.

**Do not describe the historical model metrics as newly rerun results.** The project is improved and better documented, but the remaining execution evidence is needed before claiming the rubric gaps are fully closed.
