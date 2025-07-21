
import numpy as np
from .geo_utils import geodetic_to_ecef, ecef_to_geodetic

def compute_correction_vector(base_wrong, base_correct):
    ecef_wrong = geodetic_to_ecef(*base_wrong)
    ecef_correct = geodetic_to_ecef(*base_correct)
    return ecef_correct - ecef_wrong

def correct_rover_points(rover_coords, correction_vector):
    corrected_coords = []
    for lon, lat, h in rover_coords:
        ecef = geodetic_to_ecef(lon, lat, h)
        corrected_ecef = ecef + correction_vector
        corrected_coords.append(ecef_to_geodetic(*corrected_ecef))
    return corrected_coords
