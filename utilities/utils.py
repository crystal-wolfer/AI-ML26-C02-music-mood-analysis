#Utility function that makes sure all kaggle datasets are downloaded and added to the data folder
import os
import sys

REQUIRED_FILES = [
    'high_popularity_spotify_data.csv',
    'low_popularity_spotify_data.csv',
    'universal_top_spotify_songs.csv',
    'mxmh_survey_results.csv',
    'World-happiness-report-2024.csv',
    'World-happiness-report-updated_2024.csv'
]

def check_datasets_availability(data_path=None):
    if data_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, '../data/')
    
    missing = [f for f in REQUIRED_FILES 
               if not os.path.exists(os.path.join(data_path, f))]

    if missing:
        print("Missing files in data/ folder:")
        for f in missing:
            print(f"  - {f}")
        print("\nSee README.md for download instructions.")
        raise FileNotFoundError("Missing datasets stopping notebook execution.")
    else:
        print("All datasets found, this notebook can be run without any issues.")