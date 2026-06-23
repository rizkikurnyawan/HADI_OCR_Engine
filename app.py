import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Set judul halaman
st.set_page_config(page_title="Web OCR App", page_icon="📝")
st.title("📝 Aplikasi Web OCR (Gambar ke Teks)")
st.write("Unggah foto dokumen atau gambar untuk mengekstrak teks di dalamnya.")

# Inisialisasi EasyOCR Reader (mendukung Bahasa Indonesia & Inggris)
@st.cache_resource
def load_ocr_model():
    return easyocr.Reader(['id', 'en'])

reader = load_ocr_model()

# Komponen Upload File Gambar
uploaded_file = st.file_uploader("Pilih gambar atau foto dokumen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)
    
    with st.spinner("Sedang memproses teks... Mohon tunggu..."):
        # Konversi gambar ke format numpy array untuk EasyOCR
        image_np = np.array(image)
        
        # Jalankan OCR
        result = reader.readtext(image_np, detail=0) # detail=0 hanya mengembalikan teks
        
    # Tampilkan Hasil
    st.subheader("Hasil Ekstraksi Teks:")
    if result:
        # Gabungkan hasil teks dengan baris baru
        full_text = "\n".join(result)
        st.text_area("Teks Terdeteksi:", full_text, height=250)
        
        # Tombol Download Teks
        st.download_button(
            label="Download sebagai File .txt",
            data=full_text,
            file_name="hasil_ocr.txt",
            mime="text/plain"
        )
    else:
        st.warning("Tidak ada teks yang terdeteksi dalam gambar tersebut.")
