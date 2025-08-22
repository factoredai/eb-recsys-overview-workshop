
from sklearn.preprocessing import MultiLabelBinarizer
from scipy.sparse import csr_matrix, hstack

def get_wide_input(data, X_demo):
    """    Create the wide input matrix for the model by combining demographic features and movie genres.
    Args:
        data (DataFrame): DataFrame containing user and movie information.
        X_demo (csr_matrix): Sparse matrix of demographic features.
    Returns:
        csr_matrix: Combined sparse matrix of demographic features and movie genres.
        MultiLabelBinarizer: Fitted MultiLabelBinarizer for movie genres.
    """
    # === TO DO 4 ===
    # Create a multi-label binarizer for movie genres using MultiLabelBinarizer.
    # Transform the "Genres_list" column into a multi-hot encoding and wrap it 
    # with `csr_matrix` for efficiency.

    ## homework:replace:on
    mlb = ... # MultiLabelBinarizer
    X_gen  = csr_matrix(mlb.fit_transform(data["Genres_list"]))  # multi-hot genres

    ## homework:replace:off

    # Combine demographic (X_demo) and genre (X_gen) features into the wide input matrix.
    # Use `hstack` to concatenate and cast the result to float32.

    ## homework:replace:on
    X_wide = hstack([X_demo, ...], format="csr").astype("float32")
    ## homework:replace:off

    return X_wide, X_gen, mlb