# Project Organization

```
rtk_correction/
├── src/
│   ├── __init__.py             # Makes src a package
│   ├── io_utils.py             # Load and save CSV files
│   ├── geo_utils.py            # Coordinate conversions (WGS84 <-> ECEF)
│   ├── corrector.py            # Compute and apply correction vector
│   ├── plot_utils.py           # Plotting functions
│   └── gt_utils.py             # Load ground truth height data
├── data/
│   ├── input/                  # User input rover CSV files
│   ├── DM chard NEED TO ADJUST.csv  # (example input, may be moved to input/)
│   └── gt_heights/
│       └── crittenden_ground_truth.txt  # Verified GT coordinates
├── output/
│   ├── corrected.csv           # Corrected coordinate output
│   └── before_after_plot.png   # Visualization
├── _docs/
│   ├── README.md               # Project summary
│   ├── TECH_STACK.md           # Libraries, data types, and flow
│   ├── ORGANIZATION.md         # Folder structure and file roles
│   └── user_entry.md           # How to run the program
├── main.py                    # Entry point to run the correction
└── requirements.txt           # Python dependencies
```

- `data/input/`: Place your rover CSV files here for processing.
- `data/gt_heights/`: Store ground truth coordinate files here.
- `output/`: All results and plots are saved here.
- See `_docs/user_entry.md` for usage instructions.
