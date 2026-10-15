# Job & Placement Management System

A Python academic project for managing students, job opportunities, placement applications, job recommendations, and placement statistics. It stores records in CSV files and includes a Matplotlib dashboard.

## Features
- Add, view, and search students
- Add, view, and search jobs
- Apply for jobs and update application status
- Prevent duplicate applications
- Recommend jobs using branch, CGPA, and skills
- Order jobs using a min-heap
- Process pending applications in queue order
- Placement statistics and package analysis
- Four Matplotlib charts: branch counts, CGPA distribution, application status, and company packages

## Files
- `main.py` — main command-line application
- `dashboard.py` — visualization dashboard
- `students.csv`, `jobs.csv`, `applications.csv` — sample CSV data
- `dashboard.png` — sample dashboard image
- `requirements.txt` — Python dependency

## Run locally
Install Python 3.10+ and then run:

```bash
python -m pip install -r requirements.txt
python main.py
```

To run the dashboard separately:

```bash
python dashboard.py
```

## Data privacy
The included CSV rows are fictional sample records. Do not publish real student personal data.

## Author
Mayank Pant
