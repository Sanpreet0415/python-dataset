import pandas as pd

# Data
data = {
    "State Name": ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar"],
    "Popular Food": ["Biryani", "Thukpa", "Assam Laksa", "Litti Chokha"],
    "Population": [54265000, 1593000, 34007000, 124799000],
    "Land Area (sq km)": [162968, 83743, 78438, 94163],
    "Capital City": ["Amaravati", "Itanagar", "Dispur", "Patna"],
    "Gender Ratio": [992, 883, 958, 919]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_file_path = 'indian_states_dataset.csv'
df.to_csv(csv_file_path, index=False)

print(f"Dataset saved to {csv_file_path}")
