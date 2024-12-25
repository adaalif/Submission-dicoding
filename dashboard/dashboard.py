import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the style for seaborn
sns.set_style("darkgrid")

# Title for the dashboard
st.title('Dashboard Analisis Faktor Performa Siswa')

# Load the dataset
data = pd.read_csv("StudentPerformanceFactors.csv")

# Cleaning Data (Removes missing values)
data.dropna(inplace=True)

# Show the summary statistics of the data
st.subheader("Summary Data")
st.write(data.describe())


# Visualisasi: Distribusi Nilai Ujian
st.subheader('Distribusi Nilai Ujian')
fig, ax = plt.subplots(figsize=(14, 6))
sns.histplot(data['Exam_Score'], bins=20, kde=True, ax=ax, color='blue')
ax.set_title('Distribution of Exam Scores')
ax.set_xlabel('Exam Score')
ax.set_ylabel('Frequency')
st.pyplot(fig)
average_score = data['Exam_Score'].mean()
st.subheader(f'Rata-rata Nilai Ujian: {average_score:.2f}')

# Count how many scores are above the average
above_average_count = (data['Exam_Score'] > average_score).sum()
below_average_count = (data['Exam_Score'] <= average_score).sum()

# Plot the counts
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=['Diatas rata rata', 'Dibawah rata rata'], y=[above_average_count, below_average_count], palette='pastel', ax=ax)
plt.title('Jumlah Siswa Berdasarkan Nilai Rata-rata')
plt.ylabel('Jumlah Siswa')
plt.xlabel('Kategori')
st.pyplot(fig)

st.subheader('Jumlah data pada dataset  ')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Keterlibatan Orang Tua", "Akses ke Sumber Daya", "Pendapatan Keluarga",
    "Kualitas Guru", "Jenis Sekolah", "Gangguan Pembelajaran",
    "Akses Internet", "Gender"
])

with tab1:
    st.subheader('Jumlah Berdasarkan Keterlibatan Orang Tua')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='Parental_Involvement', palette='pastel')
    plt.title('Counts of Parental Involvement')
    plt.xlabel('Parental Involvement')
    plt.ylabel('Count')
    st.pyplot(plt)

with tab2:
    st.subheader('Jumlah Berdasarkan Akses ke Sumber Daya')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='Access_to_Resources', palette='pastel')
    plt.title('Counts of Access to Resources')
    plt.xlabel('Access to Resources')
    plt.ylabel('Count')
    st.pyplot(plt)

with tab3:
    st.subheader('Jumlah Berdasarkan Pendapatan Keluarga')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='Family_Income', palette='pastel')
    plt.title('Counts of Family Income')
    plt.xlabel('Family Income')
    plt.ylabel('Count')
    st.pyplot(plt)

with tab4:
    st.subheader('Jumlah Berdasarkan Kualitas Guru')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='Teacher_Quality', palette='pastel')
    plt.title('Counts of Teacher Quality')
    plt.xlabel('Teacher Quality')
    plt.ylabel('Count')
    st.pyplot(plt)

with tab5:
    st.subheader('Jumlah Berdasarkan Jenis Sekolah')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='School_Type', palette='pastel')
    plt.title('Counts of School Type')
    plt.xlabel('School Type')
    plt.ylabel('Count')
    st.pyplot(plt)

with tab6:
    st.subheader('Jumlah Berdasarkan Gangguan Pembelajaran')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='Learning_Disabilities', palette='pastel')
    plt.title('Counts of Learning Disabilities')
    plt.xlabel('Learning Disabilities')
    plt.ylabel('Count')
    st.pyplot(plt)

with tab7:
    st.subheader('Jumlah Berdasarkan Akses Internet')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='Internet_Access', palette='pastel')
    plt.title('Counts of Internet Access')
    plt.xlabel('Internet Access')
    plt.ylabel('Count')
    st.pyplot(plt)

with tab8:
    st.subheader('Jumlah Berdasarkan Gender')
    plt.figure(figsize=(8, 4))
    sns.countplot(data=data, x='Gender', palette='pastel')
    plt.title('Counts of Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    st.pyplot(plt)

# Visualisasi: Keterlibatan Orang Tua dan Akses ke Sumber Daya
st.subheader('Rata-rata Nilai Ujian Berdasarkan Keterlibatan Orang Tua dan Akses ke Sumber Daya')
group1 = data.groupby(['Parental_Involvement', 'Access_to_Resources'])['Exam_Score'].mean().reset_index().sort_values(by='Exam_Score', ascending=True)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=group1, x='Exam_Score', y='Parental_Involvement', palette='pastel', ax=ax)
plt.title('Average Exam Scores by Parental Involvement and Access to Resources')
st.pyplot(fig)

# Visualisasi: Pengaruh Teman Sebaya dan Tingkat Motivasi
st.subheader('Distribusi Tingkat Motivasi Berdasarkan Pengaruh Teman Sebaya')
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Peer_Influence', hue='Motivation_Level', palette='pastel')
plt.title('Distribution of Motivation Levels by Peer Influence')
plt.xlabel('Peer Influence')
plt.ylabel('Count')
st.pyplot(plt)

# Visualisasi: Gender dan Nilai Ujian
st.subheader('Rata-rata Nilai Ujian Berdasarkan Gender')
gender_grouped = data.groupby('Gender')['Exam_Score'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
barplot = sns.barplot(data=gender_grouped, x='Gender', y='Exam_Score', palette='pastel', ax=ax)
for index, row in gender_grouped.iterrows():
    barplot.text(index, row['Exam_Score'] + 0.5, round(row['Exam_Score'], 2), color='black', ha="center")
plt.ylim(60, 70)
plt.title('Average Exam Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Exam Score')
st.pyplot(fig)

# Visualisasi: Pengaruh Sesi Bimbingan terhadap Nilai Ujian
st.subheader('Pengaruh Jumlah Sesi Bimbingan terhadap Nilai Ujian')
tutoring_sessions_grouped = data.groupby('Tutoring_Sessions')['Exam_Score'].mean().reset_index().sort_values(by='Exam_Score', ascending=True)
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(data=tutoring_sessions_grouped, x='Tutoring_Sessions', y='Exam_Score', marker='o', ax=ax)
ax.set_title('Pengaruh Jumlah Sesi Bimbingan terhadap Nilai Ujian')
ax.set_xlabel('Jumlah Sesi Bimbingan')
ax.set_ylabel('Rata-rata Nilai Ujian')
st.pyplot(fig)

# Visualisasi: Pengaruh Jarak Rumah terhadap Nilai Ujian
st.subheader('Pengaruh Jarak Rumah terhadap Nilai Ujian')
distance_exam_score = data.groupby(['Distance_from_Home'])['Exam_Score'].mean().reset_index().sort_values(by='Exam_Score', ascending=True)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=distance_exam_score, x='Distance_from_Home', y='Exam_Score', palette='viridis', ax=ax)
for index, row in distance_exam_score.iterrows():
    ax.text(index, row['Exam_Score'] + 0.5, round(row['Exam_Score'], 2), color='black', ha="center")
plt.ylim(60, 70)
plt.title('Average Exam Score by Distance from Home')
plt.xlabel('Distance from Home')
plt.ylabel('Average Exam Score')
st.pyplot(fig)

# Visualisasi: Distribusi Nilai Ujian Berdasarkan Tingkat Motivasi
st.subheader('Distribusi Nilai Ujian Berdasarkan Tingkat Motivasi')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data, x='Motivation_Level', y='Exam_Score', palette='pastel', ax=ax)
plt.title('Distribution of Exam Scores by Motivation Level')
plt.xlabel('Motivation Level')
plt.ylabel('Exam Score')
plt.xticks(rotation=0)  
plt.tight_layout()
st.pyplot(fig)

# Visualisasi: Distribusi Nilai Ujian Berdasarkan Jenis Sekolah dan Kualitas Pengajaran

st.subheader('Distribusi Nilai Ujian Berdasarkan Jenis Sekolah dan Kualitas Pengajaran')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data, x='School_Type', y='Exam_Score', hue='Teacher_Quality', palette='pastel', ax=ax)
plt.title('Distribution of Exam Scores by School Type and Teacher Quality')
plt.xlabel('School Type')
plt.ylabel('Exam Score')
plt.legend(title='Teacher Quality')
plt.tight_layout()
st.pyplot(fig)


# Visualisasi: Rata-rata Nilai Ujian Berdasarkan Kehadiran

st.subheader('Rata-rata Nilai Ujian Berdasarkan Kehadiran')

# Group by attendance
kerajinan = data.groupby('Attendance')['Exam_Score'].mean().reset_index()

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=kerajinan, y='Attendance', x='Exam_Score', marker='o', ax=ax)
plt.title('Average Exam Score by Attendance')
plt.ylabel('Attendance')
plt.xlabel('Average Exam Score')
plt.ylim(0, 100)
plt.grid(True)
st.pyplot(fig)