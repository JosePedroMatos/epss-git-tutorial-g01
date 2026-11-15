"""Member A: monthly statistics."""


def monthly_summary(df):
    """One row per month: mean tmin_c, mean tmax_c and total rain_mm.

    df: one row per day, the date as index, columns tmin_c, tmax_c (deg C) and rain_mm.
    """
    monthly = df.resample("MS").agg({"tmin_c": "mean", "tmax_c": "mean", "rain_mm": "sum"})
    return monthly.round(1)