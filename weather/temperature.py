"""Member B: mean temperature."""


def add_tmean(df):
    """Copy of df with a new column tmean_c = (tmin_c + tmax_c) / 2.

    df: one row per day, the date as index, columns tmin_c, tmax_c (deg C) and rain_mm.
    """
    out = df.copy()
    out["tmean_c"] = (out["tmin_c"] + out["tmax_c"]) / 2
    return out
