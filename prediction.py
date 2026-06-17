import streamlit as st
import tensorflow as tf
import pandas as pd

def run():
    # Memuat model
    @st.cache_resource
    def load_my_model():
        return tf.keras.models.load_model('best_audit_engine_model.keras')

    try:
        classifier_model = load_my_model()
        st.sidebar.success("✅ Model Ready")
    except Exception as e:
        st.sidebar.error("System Error: Gagal memuat komponen model.")

    compliance_mapping = {
        0: {"name": "Books", "hs_chapter": 49},
        1: {"name": "Clothing & Accessories", "hs_chapter": 62},
        2: {"name": "Electronics", "hs_chapter": 85},
        3: {"name": "Household", "hs_chapter": 94}
    }

    # Konten Utama Prediksi
    st.subheader("📝 Input Deskripsi Produk")

    if 'jumlah_input' not in st.session_state:
        st.session_state.jumlah_input = 1

    input_list = []
    for i in range(st.session_state.jumlah_input):
        teks_input = st.text_input(
            f"Deskripsi Barang ke-{i+1}:", 
            key=f"input_{i}", 
            placeholder="Contoh: paper printing HVS / casual cotton t-shirt"
        )
        if teks_input.strip():
            input_list.append(teks_input.strip())

    if st.button("➕ Tambah Baris Barang"):
        st.session_state.jumlah_input += 1
        st.rerun()

    st.markdown("---")

    if st.button("Jalankan Klasifikasi"):
        if not input_list:
            st.warning("Silakan masukkan minimal satu deskripsi produk.")
        else:
            results_list = []
            for text in input_list:
                try:
                    prediction = classifier_model.predict([text])
                    pred_idx = prediction.argmax(axis=-1)[0]
                    category_info = compliance_mapping.get(pred_idx, {"name": "Unknown", "hs_chapter": 0})
                    
                    results_list.append({
                        "Product Description": text,
                        "Predicted Category": category_info["name"],
                        "HS Code Target": f"Chapter {category_info['hs_chapter']}"
                    })
                except Exception as error:
                    st.error(f"Error pada teks: '{text}'. Detail: {error}")
            
            if results_list:
                st.subheader("📋 Hasil Analisis Klasifikasi")
                df_inference = pd.DataFrame(results_list)
                st.dataframe(df_inference, use_container_width=True)
                
                st.markdown("---")
                st.info("**Note:** *This project serves as a Proof of Concept (PoC) with static mapping.*")
                st.info("*Note:** Proyek ini merupakan tahapan Proof of Concept (PoC) dengan pemetaan statis.")