import pandas as pd

from Dag.transformations import clean_sales, aggregate_by_category


def test_clean_sales():
    df = pd.DataFrame({
        "customer_id": [1, 2, None, 4],
        "product_category": ["Electronics", "Clothes", "Books", None],
        "revenue": [100, -50, 200, 300]
    })

    result = clean_sales(df)

    assert len(result) == 1
    assert result.iloc[0]["customer_id"] == 1
    assert result.iloc[0]["revenue"] == 100


def test_aggregate_by_category():
    df = pd.DataFrame({
        "product_category": [
            "Electronics",
            "Electronics",
            "Clothes"
        ],
        "revenue": [100, 200, 50]
    })

    result = aggregate_by_category(df)

    assert len(result) == 2
    assert result.iloc[0]["product_category"] == "Electronics"
    assert result.iloc[0]["revenue"] == 300