# Quantium Job Simulation - Dash Development Environment

This project sets up a local development environment for building interactive data visualizations using the Dash framework.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhaysahu-cse/Quantitum-job-Simulation.git
   cd Quantitum-job-Simulation
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python app.py
```

Then open your browser to `http://127.0.0.1:8050`

## Project Structure

- `app.py` - Main Dash visualisation application
- `process.py` - Data processing script (filters Pink Morsel data and computes sales)
- `data/` - Raw CSV files (3 files with transaction data)
- `output/` - Processed data (`processed_sales.csv`)
- `requirements.txt` - Python dependencies
- `venv/` - Virtual environment (not tracked in git)

## Technologies

- **Dash 4.1.0** - Python framework for building analytical web applications
- **Pandas 3.0.2** - Data manipulation and analysis
- **Plotly 6.7.0** - Interactive graphing library

## Development

The app runs in debug mode by default, which enables:
- Hot reloading when you save changes
- Detailed error messages
- Dev tools in the browser

## Data Processing

To regenerate the processed output from raw data:

```bash
python process.py
```

This reads the three raw CSV files from `data/`, filters for Pink Morsel only, computes `sales = quantity × price`, and writes `output/processed_sales.csv` with columns: `sales`, `date`, `region`.

## Visualisation Features

- Line chart of daily Pink Morsel sales over time (Feb 2018 – Feb 2022)
- Dashed red vertical line marking the **price increase on 15 Jan 2021**
- Region filter (All / North / South / East / West)
- Hover tooltips with exact date and sales value

## Business Question Answered

> "Were sales higher before or after the Pink Morsel price increase on 15 January 2021?"

| Period | Total Sales |
|--------|------------|
| Before 15 Jan 2021 | $7,092,843 |
| After 15 Jan 2021  | $3,552,740 |

Sales were significantly higher **before** the price increase.
