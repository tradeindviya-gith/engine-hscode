import streamlit as st
# import eda
import prediction

# Pengaturan Web
st.set_page_config(page_title="Automated HS Code Classifier", page_icon="📊", layout="wide")

# Header
st.title("📊 [PROTOTYPE] AUTOMATED HS CODE CLASSIFIER")

try:
    st.image('hs_code_banner.jpg', use_container_width=True)
except Exception as e:
    pass

st.write("Engine ini mengekstrak deskripsi produk untuk menentukan Kategori dan Bab HS Code secara otomatis.")
st.markdown("---")

# Menu Navigasi Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Pilih Halaman:", ["Exploratory Data Analysis (EDA)", "Model Prediction Engine"])
st.sidebar.markdown("---")

# Mengontrol Halaman Mana yang Muncul di Bawah Gambar
if page == "Exploratory Data Analysis (EDA)":
    eda.run()
elif page == "Model Prediction Engine":
    prediction.run()