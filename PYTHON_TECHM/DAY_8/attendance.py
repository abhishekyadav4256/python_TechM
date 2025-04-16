import tkinter as tk
from tkinter import messagebox
import pandas as pd
import qrcode
import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
import os
import numpy as np

employee_file = 'employees.csv'
attendance_file = 'attendance.csv'

if not os.path.exists(employee_file):
    pd.DataFrame(columns=["Employee ID", "Employee Name", "Department"]).to_csv(employee_file, index=False)

if not os.path.exists(attendance_file):
    pd.DataFrame(columns=["Employee ID", "Date", "Time"]).to_csv(attendance_file, index=False)

def add_employee(emp_id, name, dept):
    if not emp_id or not name or not dept:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    df = pd.read_csv(employee_file)
    if emp_id not in df["Employee ID"].values:
        new_row = pd.DataFrame([[emp_id, name, dept]], columns=["Employee ID", "Employee Name", "Department"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(employee_file, index=False)
        generate_qr(emp_id)
        messagebox.showinfo("Success", f"{name} ({emp_id}) added & QR generated.")
    else:
        messagebox.showwarning("Duplicate", f"Employee ID {emp_id} already exists!")

def generate_qr(data):
    img = qrcode.make(data)
    img.save(f"{data}.png")

def mark_attendance(student_id):
    df = pd.read_csv(attendance_file)
    today = datetime.now().strftime('%Y-%m-%d')
    existing = df[(df['Employee ID'] == student_id) & (df['Date'] == today)]
    
    if existing.empty:
        now = datetime.now()
        new_row = pd.DataFrame([[student_id, now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S')]],
                               columns=["Employee ID", "Date", "Time"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(attendance_file, index=False)
        print(f"✅ Attendance marked for {student_id}")
    else:
        print(f"⚠️ {student_id} already marked for today.")

def start_qr_scanner():
    cap = cv2.VideoCapture(0)
    messagebox.showinfo("QR Scanner", "Press 'Q' to quit the scanner window.")
    while True:
        success, frame = cap.read()
        for barcode in decode(frame):
            student_id = barcode.data.decode('utf-8')
            mark_attendance(student_id)
            pts = barcode.polygon
            pts = [(pt.x, pt.y) for pt in pts]
            cv2.polylines(frame, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 3)

        cv2.imshow('QR Code Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def generate_absence_report():
    emp_df = pd.read_csv(employee_file)
    att_df = pd.read_csv(attendance_file)
    report = []

    for emp_id in emp_df["Employee ID"]:
        total_days = att_df[att_df["Employee ID"] == emp_id]["Date"].nunique()
        if total_days < 3:  # Alert if fewer than 3 attendance entries
            emp_name = emp_df.loc[emp_df["Employee ID"] == emp_id, "Employee Name"].values[0]
            report.append(f"{emp_name} ({emp_id}) - Days Attended: {total_days}")

    if report:
        messagebox.showinfo("Absence Report", "\n".join(report))
    else:
        messagebox.showinfo("Absence Report", "All employees have sufficient attendance!")

# GUI Setup
app = tk.Tk()
app.title("Employee Attendance System")
app.geometry("400x400")

label = tk.Label(app, text="Employee Attendance Manager", font=("Helvetica", 16))
label.pack(pady=10)

tk.Label(app, text="Employee ID").pack()
emp_id_entry = tk.Entry(app, width=30)
emp_id_entry.pack(pady=5)

tk.Label(app, text="Employee Name").pack()
emp_name_entry = tk.Entry(app, width=30)
emp_name_entry.pack(pady=5)

tk.Label(app, text="Department").pack()
dept_entry = tk.Entry(app, width=30)
dept_entry.pack(pady=5)

def add_employee_btn():
    emp_id = emp_id_entry.get().strip()
    name = emp_name_entry.get().strip()
    dept = dept_entry.get().strip()
    add_employee(emp_id, name, dept)

add_btn = tk.Button(app, text="Add Employee & Generate QR", command=add_employee_btn)
add_btn.pack(pady=10)

scan_btn = tk.Button(app, text="Start QR Code Attendance Scanner", command=start_qr_scanner)
scan_btn.pack(pady=5)

report_btn = tk.Button(app, text="Generate Absence Report", command=generate_absence_report)
report_btn.pack(pady=5)

exit_btn = tk.Button(app, text="Exit", command=app.quit)
exit_btn.pack(pady=20)

app.mainloop()