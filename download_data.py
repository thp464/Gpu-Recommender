import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_data(dataset="baraazaid/gpus-fps-on-games", download_path="data/raw"):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    print(f"Dataset downloaded to {download_path}")

if __name__ == "__main__":
    download_kaggle_data()
