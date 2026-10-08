import pandas as pd

print("==================================================")
print("PART 1: DATA MANIPULATION")
print("==================================================")

df_students = pd.read_csv('students.csv')

print("\n--- 1. First 5 Rows ---")
print(df_students.head())

num_rows, num_cols = df_students.shape
print(f"\n--- 2. Dataset Shape: {num_rows} rows, {num_cols} columns ---")

print("\n--- 3. Select Name and GPA Columns (First 5 Rows) ---")
print(df_students[['name', 'GPA']].head())

print("\n--- 4. Students with GPA >= 3.5 ---")
high_gpa_students = df_students[df_students['GPA'] >= 3.5]
print(high_gpa_students)

print("\n--- 5. Students Sorted by GPA (Descending) ---")
sorted_students = df_students.sort_values(by='GPA', ascending=False)
print(sorted_students)

print("\n--- 6. Average GPA by Major ---")
avg_gpa_by_major = df_students.groupby('major')['GPA'].mean()
print(avg_gpa_by_major)


print("\n\n==================================================")
print("PART 2: FROM RAW DATA TO USEFUL INFO")
print("==================================================")

df_scores = pd.read_csv('scores.csv')

print("\n--- 1. Missing Values Check ---")
print("In students.csv:")
print(df_students.isnull().sum())
print("\nIn scores.csv:")
print(df_scores.isnull().sum())

df_students['age'] = df_students['age'].fillna(df_students['age'].mean())
df_students['GPA'] = df_students['GPA'].fillna(df_students['GPA'].mean())

df_scores['math'] = df_scores['math'].fillna(df_scores['math'].mean())
df_scores['database'] = df_scores['database'].fillna(df_scores['database'].mean())

df_merged = pd.merge(df_students, df_scores, on='student_id')
print("\n--- 2. Merged Dataset Sample (First 5 Rows) ---")
print(df_merged.head())

df_merged['avg_score'] = df_merged[['python', 'math', 'database']].mean(axis=1)
print("\n--- 3. Students Average Scores (First 5 Rows) ---")
print(df_merged[['student_id', 'name', 'major', 'avg_score']].head())

print("\n--- 4. Top 5 Students by Average Score ---")
top_5_students = df_merged[['student_id', 'name', 'major', 'avg_score']].sort_values(by='avg_score', ascending=False).head(5)
print(top_5_students)

print("\n--- 5. Average Score by Major ---")
avg_score_by_major = df_merged.groupby('major')['avg_score'].mean()
print(avg_score_by_major)

df_merged.to_csv('merged_student_scores.csv', index=False)
top_5_students.to_csv('top_5_students.csv', index=False)
print("\n[INFO] Successfully processed and saved results to CSV files!")