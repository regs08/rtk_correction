
from pyproj import Transformer
import numpy as np

# Define global transformers
# WGS84 (EPSG:4979) <-> ECEF (EPSG:4978)
wgs84_to_ecef = Transformer.from_crs("epsg:4979", "epsg:4978", always_xy=True)
ecef_to_wgs84 = Transformer.from_crs("epsg:4978", "epsg:4979", always_xy=True)

def geodetic_to_ecef(lon, lat, h):
    x, y, z = wgs84_to_ecef.transform(lon, lat, h)
    return np.array([x, y, z])

def ecef_to_geodetic(x, y, z):
    lon, lat, h = ecef_to_wgs84.transform(x, y, z)
    return np.array([lon, lat, h])
