import pandas as pd

file_path = "1.csv"  
df = pd.read_csv(file_path)

def check_absences(df):
    need_attention = []

    for index, row in df.iterrows():
        name = row["Employee Name"]
        attendance = row.drop("Employee Name").values  

        count = 0
        for status in attendance:
            if status == "Absent":
                count += 1
                if count > 3:
                    need_attention.append(name)
                    break  
            else:
                count = 0  

    return need_attention

employees = check_absences(df)

if employees:
    print("Employees needing attention:")
    for emp in employees:
        print(f"- {emp}")
else:
    print("All employees are okay.")


