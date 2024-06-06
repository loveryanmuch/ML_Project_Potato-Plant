#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 1 2024

@author: Sihyun

This script contains a function for analyzing Disney movies dataset. The function calculates the total gross and the inflation-adjusted gross for movies grouped by their genre.
"""

import pandas as pd

def analyze_disney_movies_genre_gross(filepath):
    """
    Analyzes Disney movies data to calculate the total and inflation-adjusted gross by genre.

    Parameters:
    - filepath: str, the path to the Disney movies CSV file.

    Returns:
    - DataFrame: A pandas DataFrame containing the sum of total gross and inflation-adjusted gross for each genre.
    """

    # Load the dataset
    disney_movies = pd.read_csv(filepath)

    # Clean and prepare the data
    # Removing the dollar sign and commas from 'total_gross' and 'inflation_adjusted_gross' columns
    disney_movies["total_gross"] = disney_movies["total_gross"].replace("[\$,]", "", regex=True).astype(float)
    disney_movies["inflation_adjusted_gross"] = disney_movies["inflation_adjusted_gross"].replace("[\$,]", "", regex=True).astype(float)

    # Grouping the data by genre and calculating the sum of 'total_gross' and 'inflation_adjusted_gross'
    genre_gross_summary = disney_movies.groupby("genre").agg({"total_gross":"sum", "inflation_adjusted_gross":"sum"}).reset_index()

    return genre_gross_summary
