import streamlit as st
import pandas as pd
from recommend import recommend_gpus

@st.cache_data
def load_data():
    return pd.read_csv('data/processed/cleaned_fps_data.csv')

def main():
    st.title("GPU Recommender")

    df = load_data()

    resolution = st.selectbox("Select your target game resolution:", ["1080p", "1440p", "4k"])
    min_fps = st.slider("Minimum desired FPS:", 30, 240, 60)
    st.write(f"Filtering GPUs for {resolution} at least {min_fps} FPS...")

    if 'price' in df.columns:
        df['price'] = df['price'].astype(str).str.replace(r'[\$,]', '', regex=True)
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        max_price = df['price'].max()
        max_budget = st.slider("Maximum budget ($):", 0.0, max_price, 200.0)
        if max_budget == max_price:
            max_budget = None

    if st.button("Get Recommendations"):
        recommendations = recommend_gpus(df, resolution, min_fps, max_budget)
        if recommendations.empty:
            st.warning("No GPUs found matching your criteria.")
        else:
            fps_col = {
                "1080p": "fps_1080p",
                "1440p": "fps_1440p",
                "4k": "fps_4k"
            }[resolution]
            st.dataframe(recommendations[['gpu', fps_col, 'vram_mb', 'price']])

if __name__ == "__main__":
    main()
