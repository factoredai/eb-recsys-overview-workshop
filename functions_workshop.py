import numpy as np
import pandas as pd
from scipy.sparse import hstack, csr_matrix

def recommend_for_uidx_wide(u_idx, data, model, ohe_demo, mlb, top_n=10):
    # rows for this user
    u_rows = data.loc[data["u_idx"] == u_idx]
    if u_rows.empty:
        raise ValueError(f"u_idx={u_idx} not found in data.")

    # one row with this user's demographics
    user_demo = u_rows[["Age","Gender", "Occupation", "Zip-code"]].iloc[[0]]

    # all unique items (dedupe ONLY by m_idx to avoid hashing lists)
    items = (
        data.drop_duplicates(subset="m_idx")
            [["m_idx", "MovieID", "Title", "Genres_list"]]
            .reset_index(drop=True)
    )

    # filter out items the user has already seen
    seen = set(u_rows["m_idx"].unique())
    cand = items[~items["m_idx"].isin(seen)].reset_index(drop=True)
    if cand.empty:
        return []

    # --- wide features: repeat user demo + item genres ---
    user_demo_rep = pd.concat([user_demo] * len(cand), ignore_index=True)
    X_demo = ohe_demo.transform(user_demo_rep)                 # user one‑hots
    X_gen  = csr_matrix(mlb.transform(cand["Genres_list"]))    # item multi‑hot genres
    X_wide = hstack([X_demo, X_gen], format="csr").astype("float32")

    # --- model inputs ---
    u_arr = np.full(len(cand), int(u_idx), dtype=np.int32)
    i_arr = cand["m_idx"].astype("int32").to_numpy()

    preds = model.predict(
        {"user_id": u_arr, "item_id": i_arr, "wide": X_wide.toarray()},
        verbose=0
    ).ravel()

    cand["pred"] = preds
    top = cand.sort_values("pred", ascending=False).head(top_n)
    return list(top[["MovieID", "Title", "pred"]].itertuples(index=False, name=None))


def recommend_for_uidx_tt(u_idx_val, data, model, mlb, top_n=5):
    # user features (pick one representative row for this user)
    row = data[data["u_idx"] == u_idx_val].iloc[0]
    g_idx = int(row["g_idx"])
    o_idx = int(row["o_idx"])
    z_idx = int(row["z_idx"])

    # Candidate items = unseen ones
    # Include y_idx so we can pass Year into the item tower
    items = data.drop_duplicates("m_idx")[["m_idx", "MovieID", "Title", "Genres_list", "y_idx"]] 
    seen = set(data[data["u_idx"] == u_idx_val]["m_idx"].unique())
    candidates = items[~items["m_idx"].isin(seen)].reset_index(drop=True)

    # Build model inputs
    u_arr = np.full(len(candidates), u_idx_val, dtype=np.int32)
    g_arr = np.full(len(candidates), g_idx, dtype=np.int32)
    o_arr = np.full(len(candidates), o_idx, dtype=np.int32)
    z_arr = np.full(len(candidates), z_idx, dtype=np.int32)
    i_arr = candidates["m_idx"].astype(np.int32).to_numpy()
    y_arr = candidates["y_idx"].astype(np.int32).to_numpy()                     

    # Genres for candidate items (multi-hot -> float32)
    genre_mat = mlb.transform(candidates["Genres_list"]).astype("float32")

    preds = model.predict({
        "user_id": u_arr,
        "item_id": i_arr,
        "g_idx":   g_arr,
        "o_idx":   o_arr,
        "z_idx":   z_arr,
        "genres":  genre_mat,
        "y_idx":   y_arr,                                                      
    }, verbose=0).ravel()

    out = candidates.copy()
    out["pred"] = preds
    return out.sort_values("pred", ascending=False).head(top_n)