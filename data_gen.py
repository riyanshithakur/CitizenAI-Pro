import pandas as pd
import random

def generate_csv():
    TOTAL_ROWS = 5000
    categories = {
        "Road": "Public Works Department (PWD)",
        "Water": "Jal Vibhag (Water Board)",
        "Sanitary": "Nagar Nigam (Waste Management)",
        "Public Lighting": "Electricity Department"
    }
    complaints_pool = {
        "Road": ["Big potholes on main road", "Damaged divider", "Streetlight not working", "Road cracks", "Sinking pavement"],
        "Water": ["Main pipeline burst", "No water supply", "Contaminated muddy water", "Low water pressure", "Pipe leakage"],
        "Sanitary": ["Garbage bin overflowing", "Blocked sewage line", "Dead animal on street", "Open drainage", "Manhole cover missing"],
        "Public Lighting": ["Streetlight blinking", "Short circuit in pole", "Dark spot near park", "Broken electric wire"]
    }

    data = []
    for i in range(1, TOTAL_ROWS + 1):
        cat = random.choice(list(categories.keys()))
        issue = random.choice(complaints_pool[cat])
        data.append({"Complaint_Text": issue, "Category": cat, "Department": categories[cat]})
    
    df = pd.DataFrame(data)
    df.to_csv("dataset.csv", index=False)
    print("✅ Step 1: dataset.csv successfully created!")

if __name__ == "__main__":
    generate_csv()