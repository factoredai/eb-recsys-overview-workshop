import pandas as pd

def load_movielens_data():
    """
    Load the MovieLens dataset from the CSV files into Pandas DataFrames.
    
    Returns:
        users (DataFrame): DataFrame containing user information.
        movies (DataFrame): DataFrame containing movie information.
        ratings (DataFrame): DataFrame containing ratings information.
    """
    # === TO DO 1 ===
    # Load the MovieLens dataset from the CSV files into Pandas DataFrames
    # The function should return three DataFrames: users, movies, and ratings

    ## homework:replace:on
    # users = ...
    # movies = ...
    # ratings = ...
    users = pd.read_csv("../data/users.csv")
    movies = pd.read_csv("../data/movies.csv")
    ratings = pd.read_csv("../data/ratings.csv")
    ## homework:replace:off
    
    return users, movies, ratings