from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import sys
import os
import logging
from typing import List, Optional
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from recommend import load_data, recommend_gpus, clean_all_data, get_price_range

app = FastAPI(title="GPU Recommender API", version="1.0.0")

# Global cache for cleaned data
class DataCache:
    def __init__(self, refresh_interval_hours=24):
        self.df = None
        self.price_range = None
        self.last_updated = None
        self.refresh_interval = timedelta(hours=refresh_interval_hours)
        self.load_and_cache_data()
    
    def load_and_cache_data(self):
        try:
            logger.info("Loading and cleaning GPU data...")
            raw_df = load_data()
            self.df = clean_all_data(raw_df.copy()) 
            self.price_range = get_price_range(self.df.copy())
            self.last_updated = datetime.now()
            logger.info(f"Data cached successfully. {len(self.df)} GPUs loaded.")
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            raise e
    
    def get_data(self):
        if self.needs_refresh():
            logger.info("Data cache expired, refreshing...")
            self.load_and_cache_data()
        return self.df.copy()  
    
    def get_price_range(self):
        if self.needs_refresh():
            logger.info("Price range cache expired, refreshing...")
            self.load_and_cache_data()
        return self.price_range
    
    def needs_refresh(self):
        if self.last_updated is None:
            return True
        return datetime.now() - self.last_updated > self.refresh_interval
    
    def force_refresh(self):
        self.load_and_cache_data()

data_cache = DataCache(refresh_interval_hours=24)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure later on 
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

class CacheStatus(BaseModel):
    last_updated: str
    gpu_count: int
    next_refresh: str


@app.on_event("startup")
async def startup_event():
    logger.info("GPU Recommender API starting up...")
    logger.info("Startup complete!")

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "message": "GPU Recommender API is running",
        "data_last_updated": data_cache.last_updated.isoformat() if data_cache.last_updated else None
    }

@app.get("/api/cache-status", response_model=CacheStatus)
def get_cache_status():
    next_refresh = data_cache.last_updated + data_cache.refresh_interval if data_cache.last_updated else None
    return CacheStatus(
        last_updated = data_cache.last_updated.isoformat() if data_cache.last_updated else "Never",
        gpu_count = len(data_cache.df) if data_cache.df is not None else 0,
        next_refresh = next_refresh.isoformat() if next_refresh else "Unknown"
    )

@app.post("/api/refresh-cache")
def refresh_cache():
    try:
        data_cache.force_refresh()
        return {"message": "Cache refreshed successfully", "gpu_count": len(data_cache.df)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to refresh cache: {str(e)}")
    
@app.get("/api/price-range", response_model=PriceRange)
def get_price_range_endpoint():
    try:
        price_data = data_cache.get_price_range()
        return PriceRange(**price_data)
    except Exception as e:
        logger.error(f"Error getting price range: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get price range")

@app.post("/api/recommendations", response_model=List[GPUResponse])
def get_recommendations(request: GPURequest):
    try:
        logger.info(f"Getting recommendations for {request.resolution} at {request.min_fps}+ FPS")
        
        # Load and clean data using recommend.py functions
        df = data_cache.get_data()
        
        # Get recommendations using recommend.py function
        recommendations = recommend_gpus(df, request.resolution, request.min_fps, request.max_budget)
        
        if recommendations.empty:
            logger.info("No GPUs found matching criteria")
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
        
        logger.info(f"Returning {len(result)} recommendations")
        return result
        
    except Exception as e:
        logger.error(f"Error getting recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get recommendations")