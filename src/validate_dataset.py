from pathlib import Path
import pandas as pd
p=Path(__file__).resolve().parents[1]/"data"/"dataset_part_2.csv"
if not p.exists(): raise FileNotFoundError(f"Dataset missing: {p}; see README")
df=pd.read_csv(p)
print("shape",df.shape)
print("columns",df.columns.tolist())
print("duplicates",df.duplicated().sum())
print("missing",df.isna().sum().to_dict())
if "Class" in df: print("target",df.Class.value_counts(dropna=False).to_dict())
