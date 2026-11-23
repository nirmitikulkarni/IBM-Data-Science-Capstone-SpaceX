"""Collect SpaceX launches from API v4."""
import json
from pathlib import Path
import requests
import pandas as pd
URL="https://api.spacexdata.com/v4/launches"
OUT=Path(__file__).resolve().parents[1]/"data"
OUT.mkdir(exist_ok=True)
response=requests.get(URL,timeout=45)
response.raise_for_status()
launches=response.json()
(OUT/"spacex_launches_raw.json").write_text(json.dumps(launches,indent=2),encoding="utf-8")
pd.json_normalize(launches).to_csv(OUT/"spacex_launches_api.csv",index=False)
print(f"Collected {len(launches)} launch records")
