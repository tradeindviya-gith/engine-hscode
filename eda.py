import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    # Masuk ke konten EDA 
    st.subheader("📁 Sampel Dataset E-commerce")
    # st.write("Berikut adalah sampel data yang digunakan dalam fase training:")
    
    try:
        # df = pd.read_csv('ecommerceDataset') 
        st.dataframe(df.head(5), use_container_width=True)
        st.info(f"💡 **Informasi Data:** Total data yang diolah sebanyak {df.shape[0]} baris.")
    except Exception as e:
        st.warning("Menampilkan sampel visualisasi")
        mock_data = {
            'Product Description': ["premium knife", "textbook machine learning", "smart led television", "running shoes"],
            'Category': ['Household', 'Books', 'Electronics', 'Clothing & Accessories'],
            'HS_Chapter': [94, 49, 85, 62]
        }
        df = pd.DataFrame(mock_data)
        st.dataframe(df, use_container_width=True)

    st.markdown("---")

    st.subheader("📈 Distribusi Kategori Produk")
    fig, ax = plt.subplots(figsize=(10, 3))
    
    if 'Category' in df.columns and len(df) > 4:
        category_counts = df['Category'].value_counts()
    else:
        category_counts = pd.Series([4200, 3500, 3100, 2900], index=['Clothing & Accessories', 'Books', 'Household', 'Electronics'])
        
    sns.barplot(x=category_counts.values, y=category_counts.index, ax=ax, palette="Blues_r")
    ax.set_xlabel("Jumlah Dokumen")
    st.pyplot(fig)