import argparse
from src.io_utils import load_rover_csv, save_corrected_csv
from src.corrector import compute_correction_vector, correct_rover_points
from src.plot_utils import plot_before_after
from src.gt_utils import load_gt_heights

def main():
    parser = argparse.ArgumentParser(description="RTK GPS Base Correction Utility")
    parser.add_argument('--input_csv', required=True, help='Path to rover CSV file (needs correction)')
    parser.add_argument('--gt_file', required=True, help='Path to ground truth TXT file')
    parser.add_argument('--output_csv', help='Path to save corrected CSV (default: output/<input filename>)')
    parser.add_argument('--base_correct', nargs=3, type=float, metavar=('LON', 'LAT', 'HEIGHT'),
                        help='Correct base station coordinates: LON LAT HEIGHT')
    args = parser.parse_args()

    input_csv = args.input_csv
    import os
    if args.output_csv:
        output_csv = args.output_csv
    else:
        output_basename = os.path.basename(input_csv)
        output_csv = os.path.join('output', output_basename)
    gt_file = args.gt_file

    df, rover_coords = load_rover_csv(input_csv)
    base_wrong = (
        df['Base longitude'].iloc[0],
        df['Base latitude'].iloc[0],
        df['Base ellipsoidal height'].iloc[0]
    )
    if args.base_correct:
        base_correct = tuple(args.base_correct)
    else:
        gt_data = load_gt_heights(gt_file)
        base_correct = tuple(gt_data[0])
        print(f"Using first ground truth point as correct base: {base_correct}")
    correction_vector = compute_correction_vector(base_wrong, base_correct)
    corrected_coords = correct_rover_points(rover_coords, correction_vector)
    save_corrected_csv(df, corrected_coords, output_csv)
    plot_before_after(rover_coords, corrected_coords)
    gt_data = load_gt_heights(gt_file)
    print("Loaded GT points:", gt_data)
    print(f"Corrected CSV saved to {output_csv}")
    print("Plot saved to output/before_after_plot.png")

if __name__ == "__main__":
    main()
