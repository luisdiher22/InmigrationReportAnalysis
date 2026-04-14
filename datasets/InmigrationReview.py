from pathlib import Path

import pandas as pd


DATASET_DIR = Path(__file__).resolve().parent
RAW_XLSX_PATH = DATASET_DIR / "arrests-latest.xlsx"
CLEANED_CSV_PATH = DATASET_DIR / "arrests-latest-cleaned.csv"


def load_dataset(source_path: Path) -> pd.DataFrame:
	"""Load a dataset from CSV or Excel into a pandas DataFrame."""
	if source_path.suffix.lower() == ".xlsx":
		return pd.read_excel(source_path)
	if source_path.suffix.lower() == ".csv":
		return pd.read_csv(source_path)
	raise ValueError(f"Unsupported file format: {source_path.suffix}")


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
	"""Drop unused columns and enrich the detail table for Power BI."""
	columns_to_drop = ["departed_date", "file_original", "sheet_original", "row_original"]
	clean_df = df.drop(columns=columns_to_drop, errors="ignore").copy()

	if "apprehension_date" in clean_df.columns:
		clean_df["apprehension_date"] = pd.to_datetime(clean_df["apprehension_date"], errors="coerce")
		clean_df["Anio"] = clean_df["apprehension_date"].dt.year
		clean_df["Mes"] = clean_df["apprehension_date"].dt.month
		clean_df["AnioMes"] = clean_df["apprehension_date"].dt.to_period("M").astype(str)

	if "apprehension_state" in clean_df.columns:
		clean_df["State"] = clean_df["apprehension_state"].fillna("Unknown").astype(str).str.strip().str.title()

	return clean_df


def choose_source_path() -> Path:
	"""Prefer the cleaned CSV if present; otherwise, fallback to the raw Excel source."""
	if CLEANED_CSV_PATH.exists():
		return CLEANED_CSV_PATH
	if RAW_XLSX_PATH.exists():
		return RAW_XLSX_PATH
	raise FileNotFoundError("No source dataset found in datasets folder")


def main() -> None:
	"""Run the full data pipeline: load, clean, enrich, and export the final detail table."""
	source_path = choose_source_path()
	raw_df = load_dataset(source_path)
	clean_df = clean_dataset(raw_df)

	clean_df.to_csv(CLEANED_CSV_PATH, index=False)

	print(f"Source used: {source_path.name}")
	print(f"Cleaned file: {CLEANED_CSV_PATH}")
	print(f"Final shape: {clean_df.shape}")


if __name__ == "__main__":
	main()
