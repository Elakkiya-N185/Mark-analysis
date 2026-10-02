import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Arun", "Priya", "Kavin", "Meena", "Ravi", "Divya"],
    "Python": [85, 92, 70, 88, 65, 95],
    "DBMS": [78, 88, 75, 91, 72, 89],
    "Maths": [90, 95, 68, 85, 70, 92]
}

df = pd.DataFrame(data)

# Calculate total and average
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

# Display student details
print("===== STUDENT MARKS ANALYSIS =====")
print(df)

# Highest scorer
highest = df.loc[df["Total"].idxmax()]
print("\nHighest Scorer:")
print(highest["Name"], "-", highest["Total"])

# Lowest scorer
lowest = df.loc[df["Total"].idxmin()]
print("\nLowest Scorer:")
print(lowest["Name"], "-", lowest["Total"])

# Class average
print("\nClass Average:")
print(round(df["Average"].mean(), 2))

# Bar chart
plt.bar(df["Name"], df["Total"])
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Student Total Marks")
plt.show()
