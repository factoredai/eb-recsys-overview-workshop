
from sklearn.preprocessing import LabelEncoder

def get_year_embedding(data):
    """    Extract the release year from the "Title" column and encode it as an integer index.
    Args:
        data (DataFrame): DataFrame containing the "Title" column with movie titles.
    Returns:
        DataFrame: DataFrame with a new column "y_idx" containing the encoded year indices.
    """
    # === TO DO 5 ===
    # Extract the release year from the "Title" column and encode it for use as a side feature.
    # Steps:
    # 1. Extract the year (4 digits inside parentheses) and store it in a new column "Year".
    # 2. Use LabelEncoder to convert the "Year" column into integer indices.
    # 3. Save the result in a new column "y_idx", which will be used for year embeddings.

    ## homework:replace:on
    data["Year"] = ...
    data["y_idx"] = ...
    ## homework:replace:off
    return data