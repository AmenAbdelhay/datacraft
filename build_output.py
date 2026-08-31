from pathlib import Path

import pandas as pd

from Dag.transformations import clean_sales, aggregate_by_category


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
ARTIFACT_DIR = BASE_DIR / "artifact"

INPUT_FILE = DATA_DIR / "raw_sales.csv"


def main():
    ARTIFACT_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    cleaned = clean_sales(df)
    cleaned.to_csv(
        ARTIFACT_DIR / "clean_sales.csv",
        index=False
    )

    print(f"Cleaned: {len(cleaned)} rows")

    aggregated = aggregate_by_category(cleaned)
    aggregated.to_csv(
        ARTIFACT_DIR / "sales_by_category.csv",
        index=False
    )

    print(f"Aggregated: {len(aggregated)} categories")


if __name__ == "__main__":
    main()