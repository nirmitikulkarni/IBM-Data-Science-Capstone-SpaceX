# IBM Applied Data Science Capstone — SpaceX Falcon 9 First-Stage Landing Prediction

**Student:** Nirmiti Kulkarni

**Project report:** [Data Science Capstone Project Report.pdf](reports/Data%20Science%20Capstone%20Project%20Report.pdf)

**GitHub repository:** https://github.com/nirmitikulkarni/IBM-Data-Science-Capstone-SpaceX

This project explores whether Falcon 9 first-stage landing outcomes can be predicted from mission characteristics. Workflow: data collection (SpaceX API and web scraping), wrangling, exploratory analysis and SQL, geographic visualization, dashboarding, and classification.

## Dataset

Use the standard IBM/Coursera SpaceX dataset. The main modeling file is `dataset_part_2.csv`. Public course dataset copies can be found in repositories such as https://github.com/rampal-punia/IBM-DS-Capstone-Project-SpaceX; verify licensing/provenance and file contents before redistributing. The standard course `dataset_part_2.csv` is included under `data/`, sourced from a public course dataset repository. Please check the source attribution and course terms before redistribution.

## Project files

- `src/collect_api.py`: SpaceX API request, JSON archival, normalized CSV
- `src/scrape_launch_history.py`: HTML-table scraping example using BeautifulSoup/pandas
- `src/validate_dataset.py`: schema, missing values, duplicate and target counts
- `src/analysis.py`: charts and classification evaluation (requires dataset)
- `sql/analysis.sql`: SQL queries
- `app/create_folium_map.py`: interactive launch-site map
- `app/dash_app.py`: Dash dashboard
- `reports/`: submitted report and revised PDF, when uploaded

## Reproduce

1. Install `pip install -r requirements.txt`.
2. Place the course dataset at `data/dataset_part_2.csv`.
3. Run `python src/validate_dataset.py`.
4. Run `python src/analysis.py`.
5. Run `python app/create_folium_map.py` to create `evidence/folium_launch_sites_map.html`.
6. Run `python app/dash_app.py` for the local dashboard.

## Verification status

This repository was populated with source/documentation files by an automated commit. The standard dataset and generated report/evidence binaries are not included in this commit because they were unavailable to the GitHub upload bridge. Report metrics are historical values from the submitted report, not fresh executions. See the report audit for remaining verification actions.
