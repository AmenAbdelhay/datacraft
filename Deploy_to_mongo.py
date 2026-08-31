import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote_plus

import pandas as pd
from pymongo import MongoClient


host = os.environ["MONGO_HOST"]
db_name = os.environ["MONGO_DB"]
user = os.environ["MONGO_USER"]
password = os.environ["MONGO_PASSWORD"]


uri = (
    f"mongodb+srv://{quote_plus(user)}:{quote_plus(password)}"
    f"@{host}/?appName=Cluster0"
)

client = MongoClient(uri)
db = client[db_name]


artifact_folder = Path("artifact")

if not artifact_folder.exists():
    raise FileNotFoundError("artifact/ folder does not exist")


for csv_file in artifact_folder.glob("*.csv"):
    collection_name = csv_file.stem

    df = pd.read_csv(csv_file)
    records = df.to_dict("records")

    loaded_at = datetime.now(timezone.utc)

    for record in records:
        record["loaded_at"] = loaded_at

    collection = db[collection_name]

    collection.delete_many({})

    if records:
        collection.insert_many(records)

    print(
        f"Deployed {len(records)} records "
        f"→ {db_name}.{collection_name}"
    )


client.close()