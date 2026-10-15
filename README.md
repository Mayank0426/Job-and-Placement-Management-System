# 🎓 Job & Placement Management System

### A Python-Based Placement Management & Analytics Project

A Python application designed to manage student records, job opportunities, placement applications, skill-based job recommendations, and placement analytics in one place.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Storage-CSV-success" alt="CSV Storage">
  <img src="https://img.shields.io/badge/Visualization-Matplotlib-orange" alt="Matplotlib">
  <img src="https://img.shields.io/badge/DSA-Heap%20%7C%20Queue-purple" alt="Data Structures">
  <img src="https://img.shields.io/badge/Project-Academic-blueviolet" alt="Academic Project">
</p>

---

## 🔗 Project Links

- 🚀 **[Open Project Workspace on byteXL](https://app.bytexl.ai/nimbus/455a38xrp)**
- 💻 **[View GitHub Repository](https://github.com/Mayank0426/Job-and-Placement-Management-System)**

> **Note:** The byteXL workspace may require authentication or appropriate access permissions. The GitHub repository provides access to the shared source code and documentation.

---

## 📌 Project Overview

The **Job & Placement Management System** is a Python-based academic project that simplifies common placement activities. It allows users to maintain student profiles, manage job listings, process applications, identify suitable job opportunities, and analyze placement statistics.

The application uses **Object-Oriented Programming (OOP)**, CSV file handling, data structures, and Matplotlib visualizations to demonstrate practical Python programming concepts.

## ✨ Key Features

### 👨‍🎓 1. Student Management
- Add new student records.
- View registered students.
- Search students using their student ID.
- Store branch, CGPA, skills, and graduation year.

### 💼 2. Job Management
- Add job opportunities with company and role details.
- Store eligibility criteria, required skills, location, and package.
- View and search available jobs.
- Organize job opportunities using a min-heap.

### 📄 3. Application Management
- Submit job applications.
- Prevent duplicate applications for the same student and job.
- Track application status.
- Update applications to Applied, Shortlisted, Interview, Selected, or Rejected.
- Process pending applications using queue-style processing.

### 🧠 4. Job Recommendation System
- Match students with eligible jobs.
- Check branch compatibility.
- Verify minimum CGPA requirements.
- Compare student skills with job requirements.
- Calculate a match score and rank suitable opportunities.

### 📊 5. Placement Statistics
- Count students, jobs, and applications.
- Track application statuses.
- Calculate the highest and average package.
- Calculate the selection rate.

### 📈 6. Data Visualization Dashboard
The Matplotlib dashboard generates four graphical analyses:

- Students by branch
- Student CGPA distribution
- Applications by status
- Company packages in LPA

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Object-Oriented Programming | Student and Job classes |
| CSV | Data storage and file handling |
| `heapq` | Min-heap-based job ordering |
| Lists and loops | Record management and processing |
| Sets | Comparing student and job skills |
| Matplotlib | Graphs and placement analytics |
| GitHub | Source code and project documentation |
| byteXL | Development workspace |

---

## 🧩 Data Structures & Algorithms

| Concept | Application |
|---|---|
| Classes and Objects | Represent students and jobs |
| Dictionaries | Store CSV records |
| Sets | Find common skills |
| Linear Search | Search for students and jobs by ID |
| Min-Heap | Organize jobs by minimum CGPA, with package-based tie-breaking |
| Queue-style Processing | Process pending applications in order |
| Sorting | Rank suitable jobs by match score |

### Job Matching Logic

The system first checks whether a student's branch matches the job's eligible branch and whether the student meets the minimum CGPA.

Eligible students receive a match score based on skill overlap:

**Match Score = 50 + 50 × (Common Required Skills / Total Required Skills)**

The score is calculated only after eligibility checks pass. It is a project-defined matching score, not a guarantee of selection.

---

## 📁 Project Structure

```text
Job-and-Placement-Management-System/
│
├── main.py
├── dashboard.py
├── students.csv
├── jobs.csv
├── applications.csv
├── dashboard.png
├── requirements.txt
├── .gitignore
└── README.md
```

| File | Description |
|---|---|
| `main.py` | Main application and interactive menus |
| `dashboard.py` | Matplotlib visualization dashboard |
| `students.csv` | Student records |
| `jobs.csv` | Job opportunity records |
| `applications.csv` | Application records and statuses |
| `dashboard.png` | Saved dashboard image, if generated |
| `requirements.txt` | Python dependency list |
| `.gitignore` | Files Git should ignore |
| `README.md` | Project documentation |

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10 or later
- Git (optional, for cloning the repository)
- A terminal or Python IDE

### Step 1: Clone the Repository

```bash
git clone https://github.com/Mayank0426/Job-and-Placement-Management-System.git
```

### Step 2: Open the Project Folder

```bash
cd Job-and-Placement-Management-System
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Main Application

```bash
python main.py
```

### Step 5: Open the Visualization Dashboard

```bash
python dashboard.py
```

The dashboard saves a `dashboard.png` image. Interactive graph windows depend on the local Python environment.

> **Important:** Keep all three CSV files in the same folder as `main.py` and `dashboard.py`. The application uses these files to read and save data.

---

## 📊 Dashboard Preview

The visualization dashboard provides a graphical overview of placement-related data, including student branch distribution, CGPA distribution, application progress, and company packages.

If `dashboard.png` is available in the repository, you can display it here:

```markdown
![Placement Dashboard](dashboard.png)
```

---

## 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- Python fundamentals and functions
- Object-Oriented Programming
- CSV file handling
- Input validation and error handling
- Lists, dictionaries, and sets
- Searching and sorting
- Heap-based job ordering
- Queue-style application processing
- Skill-based matching logic
- Data visualization with Matplotlib

---

## 🔮 Future Enhancements

Potential improvements include:

- SQLite or MySQL database integration
- A web-based dashboard
- Student and administrator login
- Resume upload and management
- Advanced job filtering
- Email notifications
- More detailed placement analytics
- Automated testing and improved validation

---

## 🔐 Data & Privacy

The project uses CSV files for local data storage. Use fictional sample records when publishing the repository. Do not commit private student information, passwords, API keys, or other sensitive data.

---

## 👨‍💻 Author

**Mayank Pant**

B.Tech CSE (AI & ML) Student

- GitHub: [@Mayank0426](https://github.com/Mayank0426)
- Project Repository: [Job & Placement Management System](https://github.com/Mayank0426/Job-and-Placement-Management-System)
- Development Workspace: [byteXL Project](https://app.bytexl.ai/nimbus/455a38xrp)

---

<p align="center">
  <b>Built with Python to explore placement management, data structures, and analytics.</b>
</p>
