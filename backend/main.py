from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import sys
import os
from typing import List, Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from recommend import load_data, recommend_gpus, clean_all_data, get_price_range

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

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "GPU Recommender API is running"}

@app.get("/api/price-range", response_model=PriceRange)
def get_price_range_endpoint():
    try:
        df = load_data()
        price_data = get_price_range(df)
        return PriceRange(**price_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/recommendations", response_model=List[GPUResponse])
def get_recommendations(request: GPURequest):
    try:
        # Load and clean data using recommend.py functions
        df = load_data()
        df = clean_all_data(df)
        
        # Get recommendations using recommend.py function
        recommendations = recommend_gpus(df, request.resolution, request.min_fps, request.max_budget)
        
        if recommendations.empty:
            return []
        
        # Get the correct FPS column name
        fps_col = {
            "1080p": "fps_1080p",
            "1440p": "fps_1440p", 
            "4k": "fps_4k"
        }[request.resolution]
        
        # Convert to response format with safe handling
        result = []
        for _, row in recommendations.iterrows():
            result.append(GPUResponse(
                gpu=row['gpu'],
                fps=float(row[fps_col]),
                vram_mb=int(row['vram_mb']) if not pd.isna(row['vram_mb']) else 0,
                price=float(row['price']) if not pd.isna(row['price']) else 0.0
            ))
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))