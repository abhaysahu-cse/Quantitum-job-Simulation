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

- `app.py` - Main Dash application file
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

## Next Steps

1. Add your data files to the project
2. Update `app.py` with your visualizations
3. Build interactive components using Dash callbacks
