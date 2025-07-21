# Tech Stack & Data Flow

## Python Libraries:
- `pandas`: For reading and managing CSV data
- `numpy`: Efficient numerical computations
- `pyproj`: Coordinate transformations (WGS84 <-> ECEF)
- `matplotlib`: Plotting for visualization

## Data Types:
- Input: CSV file with `latitude`, `longitude`, `ellipsoidal height` (recorded using wrong base)
- Output: CSV file with corrected coordinates and plot image
- Ground Truth: TXT or CSV files with verified `latitude`, `longitude`, `height`

## Logical Flow:
1. **Load CSV** – read rover points from file
2. **Coordinate Transformation** – convert lat/lon/height to ECEF
3. **Correction Vector** – calculate difference between true and incorrect base in ECEF
4. **Apply Correction** – shift all rover points
5. **Inverse Transformation** – convert corrected points back to lat/lon/height
6. **Compare with GT** – optional height accuracy validation
7. **Output & Plot** – save and visualize results
