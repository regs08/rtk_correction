
import pandas as pd

def load_rover_csv(path):
    df = pd.read_csv(path)
    rover_coords = df[['Longitude', 'Latitude', 'Ellipsoidal height']].dropna().values
    return df, rover_coords

def save_corrected_csv(df, corrected_coords, output_path):
    corrected_df = df.copy()
    corrected_df['Longitude'] = [c[0] for c in corrected_coords]
    corrected_df['Latitude'] = [c[1] for c in corrected_coords]
    corrected_df['Ellipsoidal height'] = [c[2] for c in corrected_coords]
    corrected_df.to_csv(output_path, index=False)
