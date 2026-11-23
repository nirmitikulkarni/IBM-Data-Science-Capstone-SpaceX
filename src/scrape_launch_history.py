"""Scrape Wikipedia launch history table; page layout may change."""
from pathlib import Path
from datetime import datetime,timezone
import requests,pandas as pd
from bs4 import BeautifulSoup
URL="https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"
OUT=Path(__file__).resolve().parents[1]/"data"
OUT.mkdir(exist_ok=True)
r=requests.get(URL,headers={"User-Agent":"AcademicResearch/1.0"},timeout=30)
r.raise_for_status()
soup=BeautifulSoup(r.text,"html.parser")
tables=soup.select("table.wikitable")
frames=[pd.read_html(str(t))[0] for t in tables]
if not frames: raise RuntimeError("No launch tables found")
data=pd.concat(frames,ignore_index=True,sort=False)
data.to_csv(OUT/"web_scraped_launch_tables.csv",index=False)
(OUT/"scrape_metadata.txt").write_text(f"source={URL}\nretrieved_utc={datetime.now(timezone.utc).isoformat()}\nrows={len(data)}\n")
print(f"Parsed {len(data)} rows")
