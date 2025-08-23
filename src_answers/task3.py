
from sklearn.preprocessing import LabelEncoder


def encode_user_movie_ids(data):
    """Encode userId and movieId as integer indices for embeddings/one-hot encoding.
    Args:
        data (DataFrame): DataFrame containing userId and movieId columns.
    Returns:
        DataFrame: DataFrame with two new columns: u_idx (encoded userId) and m_idx (encoded movieId).
    """
    # Encode userId and movieId as integer indices for embeddings/one-hot encoding
    # Add two new columns to `data`: 
    #   - u_idx (encoded userId)
    #   - m_idx (encoded movieId)
    #
    # Example:
    # encoder = LabelEncoder()
    # data["col_encoded"] = encoder.fit_transform(data["col_to_encode"])

    ## homework:replace:on
    
    # data["u_idx"] = ...
    # data["m_idx"] = ...

    u_le = LabelEncoder()
    m_le = LabelEncoder()
    data["u_idx"] = u_le.fit_transform(data["UserID"])
    data["m_idx"] = m_le.fit_transform(data["MovieID"])
    ## homework:replace:off
    return data