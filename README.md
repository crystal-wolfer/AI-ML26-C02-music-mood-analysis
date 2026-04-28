# Exploratory Analysis of Music Listening Behaviour as a Signal of Population and Individual Mental State

## Setup and Running

> **Important:** Please follow these steps before opening any notebook. Notebooks NB01 and NB02 include a file-existence check at the top and will raise an error if the datasets are not in place.

### Prerequisites

- [Anaconda](https://www.anaconda.com/download) (Python 3.10+)
- Jupyter Notebook or JupyterLab (included with Anaconda)
- A free [Kaggle account](https://www.kaggle.com) to download the datasets

### Step 1 - Create the required folders

In the repository root, create two empty folders:

```
data/
figures/
```

### Step 2 - Download the datasets from Kaggle

Download each dataset manually from the links below and place all CSV files directly inside the `data/` folder (no subfolders).

| Dataset | Kaggle URL |
|---|---|
| DS1 - Spotify Music Dataset | https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset |
| DS2 - Top Spotify Songs in 73 Countries | https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated |
| DS3 - Music and Mental Health Survey (MxMH) | https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results |
| DS4 - World Happiness Report 2024 | https://www.kaggle.com/datasets/jainaru/world-happiness-report-2024-yearly-updated |

After downloading, the `data/` folder should contain:

```
data/
  high_popularity_spotify_data.csv
  low_popularity_spotify_data.csv
  universal_top_spotify_songs.csv
  mxmh_survey_results.csv
  World-happiness-report-2024.csv
  World-happiness-report-updated_2024.csv
```

### Step 3 - Run the notebooks in order

Open the notebooks in the `notebooks/` folder and run each one **from top to bottom**, in sequence:

1. `01-data profiling.ipynb` - loads and reviews all four datasets
2. `02-data cleaning.ipynb` - cleans, fixes, and joins the datasets
3. `03-eda and mood profiles.ipynb` - exploratory analysis and mood visualisations
4. `04-hypothesis testing.ipynb` - formal statistical experiments

Each notebook depends on outputs from the previous one, so the order matters.

## Project Definition and Significance
In our increasingly connected world, music streaming platforms like Spotify have become a daily companion for millions, offering not just entertainment but a potential window into emotional life. As someone who listens to music extensively, I have noticed how my choices shift based on mood switching from upbeat pop and house when I am energized to more reflective tracks during challenging moments. This observation raises a question: Is this pattern purely personal, or do people generally vary their music according to emotional state? And can large-scale listening data reveal broader patterns linking music with wellbeing at both societal and individual levels?

This project explores those questions by treating music listening behaviour as a signal rather than the primary object of study. The intention is to use streaming data as one source of evidence about collective and personal mental state, much like clinicians combine multiple observations to form a broader understanding of wellbeing. The aim is not to replace existing research on music and emotion, but to complement it with an analysis of natural listening behaviour and population-level trends.

The purpose of this project is to investigate whether data-driven analysis of Spotify listening habits can uncover meaningful patterns. These patterns may be useful for psychologists studying emotional regulation, sociologists examining cultural trends, music industry professionals designing recommendations, and individuals looking for insight into their own listening behaviour. By combining national listening charts with happiness reports and personal mental health surveys, this project asks: Do happier societies listen to happier music? Do listeners with higher anxiety or depression prefer different genres? And how consistent are these patterns across cultures and idividuals?

## Context: Music, Emotion, and Evidence
Research on music and emotional wellbeing spans psychology, neuroscience, and music therapy. Those fields offer evidence that music can influence mood, support emotional regulation, and contribute to mental health. This project does not challenge those findings; instead, it seeks to add a complementary perspective by examining how everyday listening behaviour is reflected in large observational datasets.

The data sources used here are not experimental interventions. They are observational records of what people listen to in natural settings. That means the work should be understood as exploratory and descriptive, rather than causal. The analysis aims to connect established ideas about music and emotion with patterns that emerge in actual streaming behaviour across countries and individuals.

## The Three Experiments: Digging Deeper into Music's Role in Wellbeing
This project is structured around three interconnected experiments, each exploring music’s relationship with wellbeing at a different level. The experiments are designed to be data-driven and exploratory, with an emphasis on controlled comparisons, careful interpretation, and transparency about uncertainty.

### Experiment 1: Geographic and Seasonal Mood Fingerprints
This experiment examines whether different regions show distinct emotional signatures in their collective listening habits, and whether those signatures vary with the seasons. By aggregating Spotify chart data across countries and time, I will create "mood fingerprints" using audio features such as valence and energy. Comparisons may include regions like Scandinavia and the Balkans, where seasonal patterns differ because of climate and cultural context. The question is whether seasonal changes are reflected in the emotional characteristics of top-streamed music.

### Experiment 2: National Wellbeing vs. Collective Audio Mood
This experiment evaluates country-level relationships between national happiness and the emotional tone of top-charted music. By joining World Happiness Report scores with aggregated mood profiles, I will investigate whether any relationship is present and how strong it may be. The analysis is intentionally open-ended: happier countries may not always prefer happier music, and the data will determine which patterns emerge.

### Experiment 3: Mental Health Profiles vs. Genre Preferences
This experiment focuses on individual survey responses to explore whether people with higher scores in anxiety, depression, insomnia, or OCD show different genre preferences than those with lower scores. Using self-reported mental health and music habit data, I will apply statistical methods to look for associations. Although nationality data is unavailable, this survey-based analysis provides a personal-level perspective that complements the population-level experiments.

Together, these experiments form a layered investigation: regional and seasonal listening patterns, national wellbeing correlations, and individual mental health associations. Each experiment varies assumptions about how mood is represented in music and how patterns are aggregated, which supports a more nuanced and exploratory analysis.

## Dataset Overview
The project relies on four complementary datasets, each selected for its ability to illuminate different aspects of music listening as an emotional signal.

### DS1: [Spotify Music Dataset](https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset)
This dataset comprises two CSV files: `high_popularity_spotify_data.csv` and `low_popularity_spotify_data.csv` containing track metadata, popularity measures, and audio features such as valence, energy, and danceability. DS1 provides the musical attributes needed to build mood profiles and compare tracks across popularity levels.

### DS2: [Top Spotify Songs in 73 Countries - Daily](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated)
This dataset contains daily charts for top Spotify songs in 73 countries, including Spotify ID, rank, and date. It can be joined to DS1 via Spotify ID to aggregate mood profiles by country and time period. DS2 enables analysis of geographical and seasonal patterns in collective listening behaviour.

### DS3: [Music & Mental Health Survey - MxMH](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results)
This survey dataset includes responses from 736 individuals, with self-reported scores for anxiety, depression, insomnia, and OCD on a 0–10 scale, along with genre preferences. No location data is available. DS3 is used to explore individual-level associations between mental health and music taste, providing a different perspective from the country-level datasets.

### DS4: [World Happiness Report - 2024](https://www.kaggle.com/datasets/jainaru/world-happiness-report-2024-yearly-updated)
This dataset also includes two CSV files: `World-happiness-report-2024.csv` and `World-happiness-report-updated_2024.csv`. `World-happiness-report-2024.csv` gives the world happiness country rankings and relevant factors for 2024 while `World-happiness-report-updated_2024.csv` gives the country and relevant factors affecting the happiness score from 2005 to 2024. DS4 introduces an external measure of national happiness that can be compared with aggregate musical mood scores from DS2 and DS1.

These four sources ensure the project uses multiple independent data sources, supporting a broader range of methods and comparisons.

## Analytical Levels
The datasets operate at two analytical levels. DS1, DS2, and DS4 function at the national or regional aggregate level, capturing collective listening behaviour and national wellbeing across countries and time periods. DS3 operates at the individual psychological level, focusing on self-reported mental health and genre preferences. The lack of location data in DS3 means it cannot be directly joined to the other datasets, but it provides a valuable micro-level lens that complements the macro-level analysis and is interesting to be explored.

Together, these levels create a layered investigation: empirical patterns in population listening behaviour supported by personal-level evidence from mental health and music preferences. This approach encourages cautious interpretation and avoids overreaching conclusions.