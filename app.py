import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Hadi Engine",
    page_icon="📄",
    layout="wide"
)

# =====================================================
# LOAD OCR MODEL
# =====================================================
@st.cache_resource
def load_ocr_model():
    return easyocr.Reader(['id', 'en'])

reader = load_ocr_model()

# =====================================================
# CUSTOM CSS (PERBAIKAN: Menambahkan penutup </style>)
# =====================================================
st.markdown("""
<style>
/* Background */
.stApp {
    background-color: #F5F5F5;
}

/* Hide Streamlit Menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Container */
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

/* Logo */
.logo-container {
    margin-bottom: 20px;
}

.logo {
    font-size: 32px;
    font-weight: 800;
    font-family: 'Segoe UI', sans-serif;
}

.logo-red {
    color: #D12B4B;
}

.logo-black {
    color: #1F2937;
}

/* Hero Title */
.hero-title {
    text-align: center;
    font-size: 50px;
    font-weight: 800;
    color: #111827;
    margin-top: 10px;
    margin-bottom: 5px;
}

/* Hero Subtitle */
.hero-subtitle {
    text-align: center;
    font-size: 20px;
    color: #4B5563;
    margin-bottom: 30px;
}

/* Upload Box */
div[data-testid="stFileUploader"] {
    background: #D12B4B;
    border: 2px dashed #FF9FB0;
    border-radius: 25px;
    padding: 40px 20px;
}

/* Upload Text */
div[data-testid="stFileUploader"] label, div[data-testid="stFileUploader"] p, div[data-testid="stFileUploader"] small {
    color: white !important;
}

/* Browse Button */
div[data-testid="stFileUploader"] button {
    background: white !important;
    color: #D12B4B !important;
    border: none !important;
    border-radius: 50px !important;
    font-weight: 700 !important;
    padding: 10px 20px !important;
}

div[data-testid="stFileUploader"] button:hover {
    background: #FFE6EC !important;
    color: #B81E43 !important;
}

/* Info Size Text inside Box */
.size-info {
    text-align: center;
    margin-top: -30px;
    margin-bottom: 30px;
    font-size: 14px;
    font-weight: 600;
    color: #FFFFFF;
    position: relative;
    z-index: 99;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="logo-container">
    <div class="logo">
        <span class="logo-red">hadi</span><span class="logo-black">engine</span>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================
st.markdown("""
<div class="hero-title">Image to Text Converter</div>
<div class="hero-subtitle">Turn photos, scans, and images (JPEG, PNG) into editable text formats.</div>
""", unsafe_allow_html=True)

# =====================================================
# UPLOAD FILE
# =====================================================
uploaded_file = st.file_uploader(
    "Upload or drag & drop your files",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

# Tulisan size diatur agar posisinya pas di dalam/bawah kotak uploader
st.markdown('<div class="size-info">Size up to 100 MB</div>', unsafe_allow_html=True)

# =====================================================
# FEATURES CONTAINER
# =====================================================
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="background:white; padding:20px; border-radius:15px; border:1px dashed #CBD5E1; text-align:center;">
        <div style="font-size:32px;">🛡️</div>
        <div style="font-size:16px; font-weight:600; color:#1F2937;">Privacy-focused</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:white; padding:20px; border-radius:15px; border:1px dashed #CBD5E1; text-align:center;">
        <div style="font-size:32px;">📝</div>
        <div style="font-size:16px; font-weight:600; color:#1F2937;">Easy to use</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background:white; padding:20px; border-radius:15px; border:1px dashed #CBD5E1; text-align:center;">
        <div style="font-size:32px;">⚡</div>
        <div style="font-size:16px; font-weight:600; color:#1F2937;">Lightning-fast</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# OCR PROCESS
# =====================================================
if uploaded_file is not None:
    image
