import streamlit as st
from recommend import recommend_gpus

st.title("🎮 GPU Recommender")

st.write("Enter games you want to play and your budget to get GPU recommendations.")

# Input games as a comma-separated list
games_input = st.text_input("Games (comma separated)", "Cyberpunk 2077, Elden Ring")

budget_input = st.number_input("Budget (USD)", min_value=50, max_value=2000, value=400, step=10)

resolution = st.selectbox("Target Resolution", ["1080p", "1440p", "4K"])

if st.button("Recommend GPUs"):
    game_list = [g.strip() for g in games_input.split(",")]
    results = recommend_gpus(game_list, budget_input, resolution)

    if isinstance(results, str):
        st.warning(results)
    else:
        st.success(f"Found {len(results)} suitable GPUs!")
        for gpu in results:
            st.write(f"**{gpu['gpu']}** — VRAM: {gpu['vram_gb']}GB, Price: ${gpu['price_usd']}, Avg FPS: {gpu['avg_fps']}")
