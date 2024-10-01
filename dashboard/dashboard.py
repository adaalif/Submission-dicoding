import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import streamlit as st
sns.set_style("darkgrid")
st.title('Dashboard Data Pengguna Sepeda Sewa')
df = pd.read_csv('dashboard/all_data.csv')
min_date = pd.to_datetime(df["dteday"]).min()
max_date = pd.to_datetime(df["dteday"]).max()
with st.sidebar:
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
 
main_df = df[(df["dteday"] >= str(start_date)) & 
                (df["dteday"] <= str(end_date))]

st.subheader("Jumlah Penggunaan Sepeda")
col1, col2, col3 = st.columns(3)
pie_data = main_df[['casual','registered']].sum()
total_usage = pie_data.sum()
with col1:
    st.metric(f"Total Pengguna Casual ", pie_data['casual'])
with col2:
    st.metric(f"Total Pengguna Registered ", pie_data['registered'])
with col3:
    st.metric(f"Total Pegguna ", total_usage)

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(x=pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.3})
ax.axis('equal')
st.pyplot(fig)
st.subheader("Rata-rata Pengguna berdasarkan faktor")
tab1, tab2, tab3 = st.tabs(["Cuaca", "Musim","Bulan"])

with tab1:
    st.subheader("Rata-rata Pengguna Kasual dan Terdaftar berdasarkan Cuaca")
    fig, ax = plt.subplots(figsize=(10, 6))
    sorted_df = main_df.sort_values(by='cnt', ascending=False)
    sns.barplot(x=sorted_df['cnt'], y=sorted_df['weathersit'], color='#BA3B46')
    ax.set_ylabel('Kondisi Cuaca', fontsize=14)
    ax.set_xlabel('Total rental sepeda', fontsize=14)
    st.pyplot(fig)

with tab2:
    st.subheader('Rata-Rata Pengguna per hari berdasarkan Musim')
    data_musim = main_df.groupby('season')[['cnt']].mean().round(1).sort_values('cnt', ascending=False)
    fig, ax = plt.subplots(figsize = (8,6))
    sns.barplot(y = data_musim.index, x = data_musim['cnt'], color='#BA3B46')
    ax.set_ylabel('Musim', fontsize=14)
    ax.set_xlabel('Total rental sepeda', fontsize=14)
    ax.set_yticks(data_musim.index)
    st.pyplot(fig)
with tab3:
    st.title('Rata-Rata Pengguna per hari berdasarkan Bulan')
    data_perbulan = df.groupby('mnth')[['casual','registered','cnt']].mean().round(1)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=data_perbulan.index, y=data_perbulan['cnt'], hue=data_perbulan['cnt'], palette="Greens_d", dodge=False)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total rental sepeda', fontsize=14)
    ax.set_xticks(range(len(data_perbulan.index)))  
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    st.pyplot(fig) 

st.subheader("Perbandingan pengguna casual dan registered berdasarkan faktor")
tab1, tab2, tab3, tab4 = st.tabs(["Cuaca", "Hari Libur","Hari Kerja", "Bulan"])
with tab1:
    st.subheader('Rata-rata Pengguna Casual dan Registered berdasarkan Cuaca')
    data_cuaca = main_df.groupby('weathersit')[['casual','registered','cnt']].mean().round(1)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(data_cuaca.index, data_cuaca['casual'], label='Pengguna Kasual')
    ax.bar(data_cuaca.index, data_cuaca['registered'], bottom=data_cuaca['casual'], label='Pengguna Terdaftar', color = ['#20BF55'])
    ax.set_title('Rata-rata Pengguna Kasual dan Terdaftar berdasarkan Cuaca', fontsize=16)
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Rata-rata Jumlah Pengguna', fontsize=14)
    ax.set_xticks(data_cuaca.index)
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)
with tab2:
    st.subheader('Rata-rata Pengguna Kasual dan Terdaftar berdasarkan Hari Libur')
    grouped_data = main_df.groupby('holiday')[['casual', 'registered']].mean().round(1)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(grouped_data.index, grouped_data['casual'], label='Pengguna Kasual')
    ax.bar(grouped_data.index, grouped_data['registered'], bottom=grouped_data['casual'], label='Pengguna Terdaftar', color = ['#20BF55'])
    ax.set_ylabel('Rata-rata Jumlah Pengguna', fontsize=14)

    ax.set_xticks(grouped_data.index)
    ax.set_xticklabels(['Bukan Hari Libur', 'Hari Libur'])

    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)
with tab3:
    grouped_data = main_df.groupby('workingday')[['casual', 'registered']].mean().round(1)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(grouped_data.index, grouped_data['casual'], label='Pengguna Kasual')
    ax.bar(grouped_data.index, grouped_data['registered'], bottom=grouped_data['casual'], label='Pengguna Terdaftar', color = ['#20BF55'])
    st.title('Rata-rata Pengguna Kasual dan Terdaftar berdasarkan Hari Kerja')
    ax.set_ylabel('Rata-rata Jumlah Pengguna', fontsize=14)
    ax.set_xticks(grouped_data.index)
    ax.set_xticklabels(['Bukan Hari Kerja', 'Hari Kerja'])
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)
with tab4:
    st.title('Rata-Rata Pengguna Kasual vs Terdaftar Berdasarkan Bulan')
    data_perbulan = df.groupby('mnth')[['casual','registered','cnt']].mean().round(1).sort_values('cnt',  ascending=False)
    fig , ax = plt.subplots(figsize=(10,6))
    ax.bar(data_perbulan.index,data_perbulan['casual'], label = 'Pengguna Kasual')
    ax.bar(data_perbulan.index, data_perbulan['registered'], label = 'Pengguna Terdaftar', bottom=data_perbulan['casual'])
    plt.legend()
    plt.tight_layout()
    ax.set_xlabel = "Bulan"
    ax.set_ylabel('Rata-rata Jumlah Pengguna', fontsize=14)
    ax.set_xticks(data_perbulan.index)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    st.pyplot(fig)

st.subheader('Segmentasi Pengguna Sepeda Berdasarkan Kondisi Operasional')
col1, col2 = st.columns(2)
cluster_counts = df['Cluster'].value_counts()
col_iter = iter([col1, col2])
for cluster, count in cluster_counts.items():
    col = next(col_iter)
    with col:
        st.metric(label=f"Jumlah Cluster {cluster}", value=count)
    if col is col2:
        col_iter = iter([col1, col2])
fig, ax = plt.subplots()
def custom_autopct(pct):
    return ('%.1f%%' % pct) if pct > 5 else ''
wedges, texts, autotexts = ax.pie(cluster_counts, autopct=custom_autopct , startangle=90)
ax.axis('equal')  
ax.legend(wedges, cluster_counts.index, title="Cluster", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

st.pyplot(fig)