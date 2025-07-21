# RTK GPS Base Correction Utility

This project provides a programmatic way to correct rover GPS points collected using an incorrect RTK base station. By applying a 3D transformation based on the correct and incorrect base positions, this utility outputs an updated and corrected set of coordinates.

This tool is useful in any situation where base station coordinates during data acquisition were misconfigured, and a correction based on known true coordinates is required.

### Features:
- Modular and scalable codebase
- Uses ECEF transformation for precise correction
- Generates corrected rover points
- Plots before/after for validation
- Supports loading **ground truth height values** from external `.txt` files
- **Place your input rover CSV files in `data/input/` for processing**
