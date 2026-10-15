import csv
import heapq
import os
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
STUDENTS = os.path.join(BASE, "students.csv")
JOBS = os.path.join(BASE, "jobs.csv")
APPLICATIONS = os.path.join(BASE, "applications.csv")

STUDENT_FIELDS = ["student_id", "name", "branch", "cgpa", "skills", "graduation_year"]
JOB_FIELDS = ["job_id", "company", "role", "branch", "min_cgpa", "package", "skills", "location"]
APP_FIELDS = ["application_id", "student_id", "job_id", "date", "status", "match_score"]

def read_file(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def write_file(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def next_id(prefix, rows, field):
    nums = [int(r[field][len(prefix):]) for r in rows
            if r[field].startswith(prefix) and r[field][len(prefix):].isdigit()]
    return f"{prefix}{max(nums, default=0) + 1:03d}"

class Student:
    def __init__(self, d):
        self.id, self.name, self.branch = d["student_id"], d["name"], d["branch"]
        self.cgpa = float(d["cgpa"])
        self.skills = {x.strip().lower() for x in d["skills"].split(",")}
    def show(self):
        print(f"{self.id:<9}{self.name:<20}{self.branch:<8}{self.cgpa:<7}{', '.join(sorted(self.skills))}")

class Job:
    def __init__(self, d):
        self.id, self.company, self.role, self.branch = d["job_id"], d["company"], d["role"], d["branch"]
        self.min_cgpa, self.package = float(d["min_cgpa"]), float(d["package"])
        self.skills = {x.strip().lower() for x in d["skills"].split(",")}
        self.location = d["location"]
    def show(self):
        print(f"{self.id:<9}{self.company:<16}{self.role:<22}{self.branch:<8}{self.min_cgpa:<8}{self.package} LPA")

def match_score(student, job):
    if student.branch.lower() != job.branch.lower() or student.cgpa < job.min_cgpa:
        return 0
    return round(50 + 50 * len(student.skills & job.skills) / max(len(job.skills), 1), 2)

def find(items, item_id):
    return next((x for x in items if x.id.lower() == item_id.lower()), None)

def add_student():
    rows = read_file(STUDENTS)
    name = input("Student name: ").strip()
    branch = input("Branch: ").strip().upper()
    cgpa = input("CGPA (0-10): ").strip()
    skills = input("Skills separated by commas: ").strip()
    year = input("Graduation year: ").strip()
    try:
        score = float(cgpa)
        if not name or not branch or not skills or not year.isdigit() or not 0 <= score <= 10:
            raise ValueError("Enter valid details; CGPA must be 0-10.")
    except ValueError as e:
        print("Invalid input:", e); return
    sid = next_id("STU", rows, "student_id")
    rows.append(dict(student_id=sid, name=name, branch=branch, cgpa=cgpa, skills=skills, graduation_year=year))
    write_file(STUDENTS, rows, STUDENT_FIELDS)
    print("Student added. ID:", sid)

def view_students():
    print("\nSTUDENT LIST")
    print(f"{'ID':<9}{'Name':<20}{'Branch':<8}{'CGPA':<7}Skills")
    for row in read_file(STUDENTS): Student(row).show()

def add_job():
    rows = read_file(JOBS)
    company = input("Company: ").strip()
    role = input("Job role: ").strip()
    branch = input("Eligible branch: ").strip().upper()
    minimum = input("Minimum CGPA: ").strip()
    package = input("Package in LPA: ").strip()
    skills = input("Required skills: ").strip()
    location = input("Location: ").strip()
    try:
        cg, sal = float(minimum), float(package)
        if not all([company, role, branch, skills, location]) or not 0 <= cg <= 10 or sal < 0:
            raise ValueError("Please enter valid values for all fields.")
    except ValueError as e:
        print("Invalid input:", e); return
    jid = next_id("JOB", rows, "job_id")
    rows.append(dict(job_id=jid, company=company, role=role, branch=branch, min_cgpa=minimum,
                     package=package, skills=skills, location=location))
    write_file(JOBS, rows, JOB_FIELDS)
    print("Job added. ID:", jid)

def view_jobs():
    print("\nAVAILABLE JOBS")
    for row in read_file(JOBS): Job(row).show()

def show_job_heap():
    heap = []
    for row in read_file(JOBS):
        job = Job(row)
        heapq.heappush(heap, (job.min_cgpa, -job.package, job.id, job))
    print("\nJOBS IN MIN HEAP ORDER")
    while heap:
        j = heapq.heappop(heap)[3]
        print(j.id, "|", j.company, "|", j.role, "| Min CGPA:", j.min_cgpa, "| Package:", j.package, "LPA")

def apply_job():
    students = [Student(x) for x in read_file(STUDENTS)]
    jobs = [Job(x) for x in read_file(JOBS)]
    apps = read_file(APPLICATIONS)
    student = find(students, input("Student ID: ").strip())
    job = find(jobs, input("Job ID: ").strip())
    if not student: print("Student not found."); return
    if not job: print("Job not found."); return
    if any(a["student_id"] == student.id and a["job_id"] == job.id for a in apps):
        print("Student has already applied for this job."); return
    score = match_score(student, job)
    if not score: print("Student does not meet job requirements."); return
    aid = next_id("APP", apps, "application_id")
    apps.append(dict(application_id=aid, student_id=student.id, job_id=job.id, date=str(date.today()),
                     status="Applied", match_score=str(score)))
    write_file(APPLICATIONS, apps, APP_FIELDS)
    print("Application submitted:", aid, "| Match score:", score, "%")

def view_applications():
    apps = read_file(APPLICATIONS)
    if not apps: print("No applications found."); return
    for a in apps:
        print(a["application_id"], "| Student:", a["student_id"], "| Job:", a["job_id"],
              "| Date:", a["date"], "| Status:", a["status"], "| Score:", a["match_score"])

def update_application():
    apps = read_file(APPLICATIONS); aid = input("Application ID: ").strip()
    statuses = {"1":"Applied", "2":"Shortlisted", "3":"Interview", "4":"Selected", "5":"Rejected"}
    for a in apps:
        if a["application_id"].lower() == aid.lower():
            for k, v in statuses.items(): print(k + ".", v)
            choice = input("New status: ").strip()
            if choice not in statuses: print("Invalid status."); return
            a["status"] = statuses[choice]; write_file(APPLICATIONS, apps, APP_FIELDS)
            print("Application updated."); return
    print("Application not found.")

def process_queue():
    apps = read_file(APPLICATIONS)
    pending = next((a for a in apps if a["status"] == "Applied"), None)
    if not pending: print("No pending applications."); return
    pending["status"] = "Shortlisted"
    write_file(APPLICATIONS, apps, APP_FIELDS)
    print("Processed:", pending["application_id"], "-> Shortlisted")

def recommend_jobs():
    students = [Student(x) for x in read_file(STUDENTS)]
    jobs = [Job(x) for x in read_file(JOBS)]
    student = find(students, input("Student ID: ").strip())
    if not student: print("Student not found."); return
    results = [(match_score(student, j), j) for j in jobs]
    results = sorted(((s, j) for s, j in results if s > 0), reverse=True, key=lambda x: x[0])
    if not results: print("No suitable jobs found."); return
    print("\nRECOMMENDED JOBS")
    for score, j in results:
        print(j.id, "|", j.company, "|", j.role, "|", j.package, "LPA | Match:", score, "% |", j.location)

def statistics():
    students, jobs, apps = read_file(STUDENTS), read_file(JOBS), read_file(APPLICATIONS)
    print("\nPLACEMENT STATISTICS")
    print("Total Students:", len(students), "| Total Jobs:", len(jobs), "| Total Applications:", len(apps))
    for status in ["Applied", "Shortlisted", "Interview", "Selected", "Rejected"]:
        print(status + ":", sum(a["status"] == status for a in apps))
    packages = [float(j["package"]) for j in jobs]
    if packages: print("Highest Package:", max(packages), "LPA | Average Package:", round(sum(packages)/len(packages), 2), "LPA")
    if apps: print("Selection Rate:", round(sum(a["status"] == "Selected" for a in apps)/len(apps)*100, 2), "%")

def dashboard():
    import subprocess, sys
    path = os.path.join(BASE, "dashboard.py")
    if not os.path.exists(path): print("dashboard.py not found."); return
    subprocess.Popen([sys.executable, path], cwd=BASE)

def main():
    actions = {
        "1": ("Student Management", [
            ("1", "Add student", add_student), ("2", "View students", view_students),
            ("3", "Search student", lambda: search_students()), ("4", "Back", None)]),
        "2": ("Job Management", [
            ("1", "Add job", add_job), ("2", "View jobs", view_jobs),
            ("3", "Search job", lambda: search_jobs()), ("4", "Min heap job order", show_job_heap), ("5", "Back", None)]),
        "3": ("Application Management", [
            ("1", "Apply for job", apply_job), ("2", "View applications", view_applications),
            ("3", "Update application", update_application), ("4", "Process application queue", process_queue), ("5", "Back", None)])
    }
    while True:
        print("\n" + "="*44 + "\nJOB & PLACEMENT MANAGEMENT SYSTEM\n" + "="*44)
        print("1. Student Management\n2. Job Management\n3. Application Management\n4. Job Recommendation\n5. Placement Statistics\n6. Open Visualization Dashboard\n7. Exit")
        choice = input("Enter choice: ").strip()
        try:
            if choice in actions:
                title, options = actions[choice]
                while True:
                    print("\n" + title.upper())
                    for key, label, _ in options: print(key + ".", label)
                    sub = input("Choice: ").strip()
                    selected = next((fn for key, _, fn in options if key == sub), "invalid")
                    if selected is None: break
                    if selected == "invalid": print("Invalid choice.")
                    else: selected()
            elif choice == "4": recommend_jobs()
            elif choice == "5": statistics()
            elif choice == "6": dashboard()
            elif choice == "7": print("Thank you for using the system."); break
            else: print("Invalid choice.")
        except (FileNotFoundError, ValueError, KeyError) as e:
            print("Please check required files/data:", e)

def search_students():
    student_id = input("Student ID: ").strip()
    student = find([Student(x) for x in read_file(STUDENTS)], student_id)
    student.show() if student else print("Student not found.")

def search_jobs():
    job_id = input("Job ID: ").strip()
    job = find([Job(x) for x in read_file(JOBS)], job_id)
    if job:
        job.show(); print("Location:", job.location, "| Skills:", ", ".join(sorted(job.skills)))
    else: print("Job not found.")

if __name__ == "__main__":
    main()
