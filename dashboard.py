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

    df['year'] = df['yr'].map({0: 2011, 1: 2012})

    return df

df = load_data()

# ======================
# SIDEBAR FILTER
# ======================
st.sidebar.title("Filter Data")

selected_year = st.sidebar.multiselect(
    "Pilih Tahun",
    options=sorted(df['year'].unique()),
    default=sorted(df['year'].unique())
)

selected_month = st.sidebar.multiselect(
    "Pilih Bulan",
    options=sorted(df['mnth'].unique()),
    default=sorted(df['mnth'].unique())
)

# APPLY FILTER
filtered_df = df[
    (df['year'].isin(selected_year)) &
    (df['mnth'].isin(selected_month))
]

# ======================
# MAIN DASHBOARD
# ======================
st.title("🚴 Bike Sharing Dashboard")

st.write(f"Menampilkan {filtered_df.shape[0]} data")

# ======================
# DASHBOARD 1 - CUACA
# ======================
st.subheader("📊 Pengaruh Cuaca")

weather_avg = filtered_df.groupby('weather_label')['cnt'].mean().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(x='weather_label', y='cnt', data=weather_avg, ax=ax1)

ax1.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig1)

# ======================
# DASHBOARD 2 - TREND
# ======================
st.subheader("📈 Tren Penyewaan")

fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(filtered_df['dteday'], filtered_df['cnt'])

ax2.set_title("Trend Penyewaan Sepeda")
ax2.set_xlabel("Tanggal")
ax2.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig2)