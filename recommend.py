import pandas as pd
import streamlit as st

df = pd.read_csv('data/processed/cleaned_fps_data.csv')

def recommend_gpus(df, desired_resolution, min_fps=60, max_budget=None):
    # Map resolution input to corresponding column in df
    res_map = {
        "1080p": "fps_1080p",
        "1440p": "fps_1440p",
        "4k": "fps_4k"
    }
    fps_col = res_map.get(desired_resolution.lower())
    if not fps_col:
        raise ValueError(f"Unsupported resolution: {desired_resolution}")
    
    df[fps_col] = df[fps_col].str.extract(r'(\d+\.?\d*)')
    df[fps_col] = pd.to_numeric(df[fps_col], errors='coerce')

    df = df.dropna(subset=[fps_col])
    filtered = df[df[fps_col] >= min_fps]

    if max_budget is not None and max_budget > 0 and 'price' in df.columns:
        filtered = filtered[filtered['price'] <= max_budget]

    return filtered.sort_values(by=fps_col, ascending=False)
