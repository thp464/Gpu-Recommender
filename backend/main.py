from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
from typing import List, Optional

app = FastAPI(title="GPU Recommender API", version="1.0.0")

# Add CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GPURequest(BaseModel):
    resolution: str
    min_fps: int
    max_budget: Optional[float] = None

class GPUResponse(BaseModel):
    gpu: str
    fps: float
    vram_mb: int
    price: float

class PriceRange(BaseModel):
    min_price: float
    max_price: float

def load_data():
    # Get path relative to backend folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, '..', 'data', 'processed', 'cleaned_fps_data.csv')
    return pd.read_csv(csv_path)

def recommend_gpus(df, desired_resolution, min_fps=60, max_budget=None):
    # Your existing logic from recommend.py
    res_map = {
        "1080p": "fps_1080p",
        "1440p": "fps_1440p",
        "4k": "fps_4k"
    }
    fps_col = res_map.get(desired_resolution.lower())
    if not fps_col:
        raise ValueError(f"Unsupported resolution: {desired_resolution}")
    
    # Extract FPS values and convert to numeric
    df[fps_col] = df[fps_col].str.extract(r'(\d+\.?\d*)')
    df[fps_col] = pd.to_numeric(df[fps_col], errors='coerce')
    
    # Filter out rows with missing FPS data
    df = df.dropna(subset=[fps_col])
    filtered = df[df[fps_col] >= min_fps]
    
    # Filter by budget if specified
    if max_budget is not None and max_budget > 0 and 'price' in df.columns:
        filtered = filtered[filtered['price'] <= max_budget]
    
    return filtered.sort_values(by=fps_col, ascending=False)

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "GPU Recommender API is running"}

@app.get("/api/price-range", response_model=PriceRange)
def get_price_range():
    try:
        df = load_data()
        if 'price' in df.columns:
            # Clean price data like in your Streamlit app
            df['price'] = df['price'].astype(str).str.replace(r'[\$,]', '', regex=True)
            df['price'] = pd.to_numeric(df['price'], errors='coerce')
            return PriceRange(
                min_price=float(df['price'].min()),
                max_price=float(df['price'].max())
            )
        return PriceRange(min_price=0.0, max_price=2000.0)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/recommendations", response_model=List[GPUResponse])
def get_recommendations(request: GPURequest):
    try:
        df = load_data()
        
        # Clean price data like in your Streamlit app
        if 'price' in df.columns:
            df['price'] = df['price'].astype(str).str.replace(r'[\$,]', '', regex=True)
            df['price'] = pd.to_numeric(df['price'], errors='coerce')
        
        # Get recommendations using your existing logic
        recommendations = recommend_gpus(df, request.resolution, request.min_fps, request.max_budget)
        
        if recommendations.empty:
            return []
        
        # Get the correct FPS column name
        fps_col = {
            "1080p": "fps_1080p",
            "1440p": "fps_1440p", 
            "4k": "fps_4k"
        }[request.resolution]
        
        # Convert to response format
        # Bug found dealing with Vram Data
        result = []
        for _, row in recommendations.iterrows():
            result.append(GPUResponse(
                gpu=row['gpu'],
                fps=float(row[fps_col]),
                vram_mb=int(row['vram_mb']),
                price=float(row['price'])
            ))
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)