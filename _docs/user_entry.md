# User Entry Guide: RTK GPS Base Correction Utility

This guide explains how to use the command-line interface to correct rover GPS points using the RTK GPS Base Correction Utility.

## Prerequisites
- Python 3.8+
- All dependencies installed (see requirements.txt)
- Virtual environment activated (recommended)

## Usage

Run the program from the project root using:

```
python main.py --input_csv <path_to_rover_csv> --gt_file <path_to_ground_truth_txt> [--output_csv <output_path>] [--base_correct LON LAT HEIGHT]
```

### Arguments
- `--input_csv` (required): Path to the rover CSV file that needs correction.
- `--gt_file` (required): Path to the ground truth TXT or CSV file (must have columns: longitude, latitude, height).
- `--output_csv` (optional): Path to save the corrected CSV (default: `output/corrected.csv`).
- `--base_correct` (optional): The correct base station coordinates as three values: longitude latitude height. If not provided, the program will use the **first row** of the ground truth file as the correct base coordinates.

### Example

```
python main.py --input_csv "data/DM chard NEED TO ADJUST.csv" --gt_file "data/gt_heights/crittenden_ground_truth.txt" --base_correct -77.01510607 42.87860715 158.895
```

If you omit `--base_correct`, the program will use the first row of your ground truth file as the correct base coordinates and print them to the console.

## Output
- Corrected CSV: Saved to the path specified by `--output_csv` (default: `output/corrected.csv`)
- Plot: Saved to `output/before_after_plot.png`
- Loaded ground truth points are printed to the console.

---

For more details, see the main README in `_docs/README.md`. 