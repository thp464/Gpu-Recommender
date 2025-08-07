import pandas as pd
import json
import os

RAW_JSON_PATH = "data/raw/gpus.json"
OUTPUT_CSV_PATH = "data/processed/cleaned_fps_data.csv"

def process_kaggle_json(raw_json_path=RAW_JSON_PATH, output_csv_path=OUTPUT_CSV_PATH):
    with open(raw_json_path, 'r') as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    print("Columns in dataset:", df.columns.tolist())

    df_clean = df[[
        "Name",
        "Price.Value",
        "Memory.Value",
        "Average 1080p Performance.Value",
        "Average 1440p Performance.Value",
        "Average 4K Performance.Value"
    ]].rename(columns={
        "Name": "gpu",
        "Price.Value": "price",
        "Memory.Value": "vram_mb",
        "Average 1080p Performance.Value": "fps_1080p",
        "Average 1440p Performance.Value": "fps_1440p",
        "Average 4K Performance.Value": "fps_4k",
    })

    # Save cleaned CSV
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    df_clean.to_csv(output_csv_path, index=False)
    print(f"Cleaned data saved to {output_csv_path}")

if __name__ == "__main__":
    process_kaggle_json()
