
import pandas as pd

def load_gt_heights(path):
    """
    Load ground truth height data from a txt or csv file with columns:
    longitude, latitude, height
    """
    df = pd.read_csv(path)
    required = {'longitude', 'latitude', 'height'}
    if not required.issubset(df.columns):
        raise ValueError(f"GT file must contain columns: {required}")
    return df[['longitude', 'latitude', 'height']].values
