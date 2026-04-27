import os
import sys
import pandas as pd

# Dataset availability check
REQUIRED_FILES = [
    'high_popularity_spotify_data.csv',
    'low_popularity_spotify_data.csv',
    'universal_top_spotify_songs.csv',
    'mxmh_survey_results.csv',
    'World-happiness-report-2024.csv'
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


# Data profiling and quality checks
def missing_audit(df, name):
    """Audit missing values in a dataframe and display a summary."""
    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(3)
    report = pd.DataFrame({"missing_count": missing, "missing_pct%": pct})
    result = report[report.missing_count > 0]

    if result.empty:
        print(f"{name}: no missing values")
    else:
        print(f"{name} - missing values found:")
        display(result)


def compare_schemas(df1, df2, name1, name2):
    """Compare column schemas and dtypes between two dataframes.

    Displays:
    - Schema match confirmation and column list
    - Full dtype comparison table for all columns
    - Highlighted dtype mismatches (if any)
    """
    print(f"{name1} popularity set:", df1.shape)
    print(f"{name2} popularity set:", df2.shape)

    cols1 = set(df1.columns)
    cols2 = set(df2.columns)

    only_in_1 = cols1 - cols2
    only_in_2 = cols2 - cols1

    if only_in_1 or only_in_2:
        print(f"Datasets schema mismatch:")
        if only_in_1:
            print(f"Columns only in {name1}: {only_in_1}")
        if only_in_2:
            print(f"Columns only in {name2}: {only_in_2}")
    else:
        print(f"Datasets schema is matching! Both sets share the same {len(cols1)} columns:")
        print(df1.columns.tolist())

    # Compare dtypes
    dtype_comp = pd.DataFrame({
        f"{name1}_dtype": df1.dtypes,
        f"{name2}_dtype": df2.dtypes
    })

    mismatches = dtype_comp[dtype_comp[f"{name1}_dtype"] != dtype_comp[f"{name2}_dtype"]]

    if mismatches.empty:
        print("\nAll columns dtypes match between both files!")
    else:
        print("\nDtype mismatches present:")
        display(mismatches)

    print()
    display(dtype_comp)

# Mood categorization and analysis based on Thayer's model
def categorize_mood(valence, energy, v_threshold=0.5, e_threshold=0.5):
    """Categorize a track into one of four moods based on Thayer's model.

    Args:
        valence: Musical positiveness (0.0-1.0)
        energy: Perceptual intensity (0.0-1.0)
        v_threshold: Valence threshold for happy/sad split (default 0.5)
        e_threshold: Energy threshold for energetic/calm split (default 0.5)

    Returns:
        One of: 'Joyful/Energetic', 'Content/Peaceful', 'Tense/Angry', 'Sad/Melancholic'
    """
    if valence >= v_threshold and energy >= e_threshold:
        return "Joyful/Energetic"
    elif valence >= v_threshold and energy < e_threshold:
        return "Content/Peaceful"
    elif valence < v_threshold and energy >= e_threshold:
        return "Tense/Angry"
    else:
        return "Sad/Melancholic"


def analyze_mood_distribution(df, name, v_threshold=0.5, e_threshold=0.5):
    """Analyze mood distribution in a dataframe based on valence and energy.

    Args:
        df: Dataframe with 'valence' and 'energy' columns
        name: Label for output (e.g., 'HIGH popularity set')
        v_threshold: Valence threshold (default 0.5)
        e_threshold: Energy threshold (default 0.5)

    Returns:
        Tuple of (dataframe with mood column, distribution summary dataframe)
    """
    df_temp = df.copy()
    df_temp['mood'] = df_temp.apply(
        lambda row: categorize_mood(
            row['valence'], row['energy'], v_threshold, e_threshold
        ),
        axis=1
    )

    mood_dist = df_temp['mood'].value_counts().sort_index()
    mood_pct = (mood_dist / len(df_temp) * 100).round(1)

    result = pd.DataFrame({'count': mood_dist, 'percentage': mood_pct})
    print(f"\nMood distribution: {name}")
    display(result)

    return df_temp, result

# Data profiling for numeric columns
def profile_numeric_columns(df1, df2, columns, name1, name2):
    """
    Args:
        df1: First dataframe
        df2: Second dataframe
        columns: List of column names to profile
        name1: Label for first dataframe
        name2: Label for second dataframe
    """
    print(f"\n{name1}:")
    display(df1[columns].describe().round(3))

    print(f"\n{name2}:")
    display(df2[columns].describe().round(3))