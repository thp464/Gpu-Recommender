import pandas as pd

# Load data once
gpus = pd.read_csv("data/gpus.csv")
games = pd.read_csv("data/games.csv")
benchmarks = pd.read_csv("data/benchmarks.csv")

def recommend_gpus(game_names, budget, resolution="1080p"):
    """
    Recommend GPUs that can run all listed games within the budget.
    """
    # Find game_ids for the input games
    selected_games = games[games['name'].str.lower().isin([g.lower() for g in game_names])]
    if selected_games.empty:
        return f"No games found for {game_names}"
    
    # Check VRAM requirements (take max rec_vram across selected games)
    max_vram = selected_games['rec_vram_gb'].max()

    # Filter GPUs by VRAM and budget
    candidate_gpus = gpus[(gpus['vram_gb'] >= max_vram) & (gpus['price_usd'] <= budget)]

    if candidate_gpus.empty:
        return "No GPUs match your VRAM requirements and budget."

    # Check benchmarks for all selected games at given resolution
    # We want GPUs that have benchmark entries for ALL games
    recommended = []
    for _, gpu in candidate_gpus.iterrows():
        gpu_id = gpu['gpu_id']
        # Get benchmarks for this gpu and all selected games
        gpu_benchmarks = benchmarks[
            (benchmarks['gpu_id'] == gpu_id) & 
            (benchmarks['game_id'].isin(selected_games['game_id'])) & 
            (benchmarks['resolution'] == resolution)
        ]
        # If benchmarks for all selected games are present
        if set(gpu_benchmarks['game_id']) == set(selected_games['game_id']):
            avg_fps = gpu_benchmarks['avg_fps'].mean()
            recommended.append({
                'gpu': gpu['name'],
                'vram_gb': gpu['vram_gb'],
                'price_usd': gpu['price_usd'],
                'avg_fps': round(avg_fps, 1)
            })

    if not recommended:
        return "No GPUs have benchmark data for all selected games."

    # Sort by average fps descending, then price ascending
    recommended = sorted(recommended, key=lambda x: (-x['avg_fps'], x['price_usd']))
    return recommended
