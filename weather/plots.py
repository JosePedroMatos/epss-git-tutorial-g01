"""Member C: plots."""


def plot_temperature(df, path="outputs/temperature.png"):
    """Save a plot of daily tmin_c and tmax_c to path and return path.

    df: one row per day, the date as index, columns tmin_c, tmax_c (deg C) and rain_mm.
    """
    from pathlib import Path
    ax = df[["tmin_c", "tmax_c"]].plot(figsize=(9, 4), ylabel="deg C", title="Daily temperature")
    Path(path).parent.mkdir(exist_ok=True)
    ax.figure.savefig(path, dpi=120)
    return path
