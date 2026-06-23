import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Set judul halaman dan layout
st.set_page_config(page_title="Web OCR App", page_icon="📝", layout="centered")

# --- CUSTOM CSS UNTUK MENIRU DESAIN GAMBAR ---
st.markdown("""
    <style>
    /* Mengubah tampilan area File Uploader Streamlit */
    div[data-testid="stFileUploader"] {
        background-color: #D12B4B; /* Warna merah seperti gambar */
        border: 2px dashed #FF8A9F;
        border-radius: 20px;
        padding: 40px 20px;
        color: white !important;
        text-align: center;
    }
    
    /* Mengubah warna teks default di dalam uploader agar kontras (Putih) */
    div[data-testid="stFileUploader"] section {
        background-color: transparent !important;
    }
    div[data-testid="stFileUploader"] label, div[data-testid="stFileUploader"] p, div[data-testid="stFileUploader"] small {
        color: white !important;
    }
    
    /* Gaya untuk bagian Fitur di bawah */
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
        padding: 8px 16px;
        border: 1px dashed #CCCCCC;
        border-radius: 12px;
        background-color: #FDFDFD;
        font-family: sans-serif;
        font-size: 14px;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi EasyOCR Reader
@st.cache_resource
def load_ocr_model():
    return easyocr.Reader(['id', 'en'])

reader = load_ocr_model()

# --- BAGIAN UTAMA WEB ---
st.title("📝 Hadi OCR Engine")
st.write("Extract text from your images smoothly.")
st.markdown("---")

# Area File Uploader (Desain Merah Custom via CSS)
uploaded_file = st.file_uploader(
    label="Upload or drag & drop your files", 
    type=["jpg", "jpeg", "png"],
    help="Size up to 100 MB"
)

# --- TAMPILAN FITUR (Mengikuti Bagian Bawah Gambar image_0a17fb.png) ---
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
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Processing OCR... Please wait..."):
        image_np = np.array(image)
        result = reader.readtext(image_np, detail=0)
        
    # Tampilkan Hasil
    st.subheader("Result:")
    if result:
        full_text = "\n".join(result)
        st.text_area("Detected Text:", full_text, height=250)
        
        # Tombol Download
        st.download_button(
            label="Download as .txt",
            data=full_text,
            file_name="ocr_result.txt",
            mime="text/plain"
        )
    else:
        st.warning("No text detected in this image.")
