import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Set judul halaman tanpa emoji kaku
st.set_page_config(page_title="Hadi OCR Engine", page_icon="📝", layout="centered")

# --- CUSTOM CSS PERBAIKAN (MINIMALIS & FIX TOMBOL WHITEOUT) ---
st.markdown("""
    <style>
    /* 1. Mengubah Font Judul Utama agar Minimalis, Bersih, dan Lebih Tipis */
    .minimal-title {
        font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
        font-weight: 300; /* Membuat font lebih tipis / tidak kaku */
        font-size: 2.5rem;
        color: #1E293B;
        margin-bottom: 2px;
        letter-spacing: -0.5px;
    }
    .minimal-subtitle {
        font-family: 'Inter', 'Segoe UI', sans-serif;
        font-weight: 400;
        color: #64748B;
        font-size: 1rem;
        margin-bottom: 25px;
    }

    /* 2. Mengubah Tampilan Area Upload (Kotak Merah) */
    div[data-testid="stFileUploader"] {
        background-color: #D12B4B; 
        border: 2px dashed #FF8A9F;
        border-radius: 16px;
        padding: 30px 20px;
        text-align: center;
    }
    
    /* Memastikan teks petunjuk di dalam kotak berwarna putih */
    div[data-testid="stFileUploader"] label, 
    div[data-testid="stFileUploader"] p, 
    div[data-testid="stFileUploader"] small {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* 3. FIX TOMBOL: Mengubah warna tombol "Browse files" agar teksnya kelihatan jelas */
    div[data-testid="stFileUploader"] button {
        background-color: #FFFFFF !important; /* Latar belakang tombol tetap putih */
        color: #D12B4B !important;            /* Teks tombol diubah jadi merah agar kontras */
        border: none !important;
        border-radius: 8px !important;
        padding: 6px 16px !important;
        font-weight: 600 !important;
    }
    
    /* Efek ketika tombol disorot kursor (Hover) */
    div[data-testid="stFileUploader"] button:hover {
        background-color: #FFEAEF !important; /* Berubah pink muda saat di-hover */
        color: #A31D36 !important;
    }
    
    /* 4. Gaya Komponen Fitur di Bagian Bawah */
    .feature-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .feature-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 18px;
        border: 1px dashed #E2E8F0;
        border-radius: 20px;
        background-color: #F8FAFC;
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #475569;
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi EasyOCR Reader
@st.cache_resource
def load_ocr_model():
    return easyocr.Reader(['id', 'en'])

reader = load_ocr_model()

# --- BAGIAN ATAS (Sudah Dibuat Minimalis & Tanpa Gambar Buku) ---
st.markdown('<h1 class="minimal-title">Hadi OCR Engine</h1>', unsafe_allow_html=True)
st.markdown('<p class="minimal-subtitle">Extract text from your images smoothly.</p>', unsafe_allow_html=True)
st.markdown("---")

# Area File Uploader (Tombol sudah diperbaiki tidak "whiteout" lagi)
uploaded_file = st.file_uploader(
    label="Upload or drag & drop your files", 
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed" # Menyembunyikan label bawaan agar tidak double text
)

# --- TAMPILAN FITUR BAWAH ---
st.markdown("""
    <div class="feature-container">
        <div class="feature-item">🛡️ Privacy-focused</div>
        <div class="feature-item">📝 Easy to use</div>
        <div class="feature-item">⏱️ Lightning-fast</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- PROSES OCR ---
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Processing OCR... Please wait..."):
        image_np = np.array(image)
        result = reader.readtext(image_np, detail=0)
        
    st.subheader("Result:")
    if result:
        full_text = "\n".join(result)
        st.text_area("Detected Text:", full_text, height=250)
        
        st.download_button(
            label="Download as .txt",
            data=full_text,
            file_name="ocr_result.txt",
            mime="text/plain"
        )
    else:
        st.warning("No text detected in this image.")
