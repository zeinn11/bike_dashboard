import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data():
    df = pd.read_csv('day.csv', sep=';')
    df['dteday'] = pd.to_datetime(df['dteday'])

    df['weather_label'] = df['weathersit'].map({
        1: 'Cerah',
        2: 'Berawan',
        3: 'Hujan Ringan',
        4: 'Hujan Lebat'
    })
    return df

df = load_data()

# ======================
# SIDEBAR
# ======================
st.sidebar.title("Dashboard Bike Sharing")
menu = st.sidebar.selectbox(
    "Pilih Analisis",
    ["Pengaruh Cuaca", "Tren Penyewaan"]
)

# ======================
# DASHBOARD 1
# ======================
if menu == "Pengaruh Cuaca":
    st.title("📊 Pengaruh Cuaca terhadap Penyewaan Sepeda")

    weather_avg = df.groupby('weather_label')['cnt'].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(x='weather_label', y='cnt', data=weather_avg, ax=ax)

    ax.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig)

    st.write("### Insight")
    st.write("""
    - Penyewaan tertinggi terjadi saat cuaca cerah  
    - Menurun saat berawan  
    - Turun drastis saat hujan  
    """)

# ======================
# DASHBOARD 2
# ======================
elif menu == "Tren Penyewaan":
    st.title("📈 Tren Penyewaan Sepeda (2011–2012)")

    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(df['dteday'], df['cnt'])

    ax.set_title("Trend Penyewaan Sepeda")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig)

    st.write("### Insight")
    st.write("""
    - Pola fluktuatif  
    - Ada indikasi musiman  
    - Terdapat periode naik dan turun  
    """)