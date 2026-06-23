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

# CUSTOM CSS

# =====================================================

st.markdown("""

<style>



/* Background */

.stApp{

    background-color:#F5F5F5;

}



/* Hide Streamlit Menu */

#MainMenu {visibility:hidden;}

footer {visibility:hidden;}

header {visibility:hidden;}



/* Container */

.block-container{

    padding-top:2rem;

    max-width:1200px;

}



/* Logo */

.logo-container{

    margin-bottom:40px;

}



.logo{

    font-size:42px;

    font-weight:800;

    font-family:'Segoe UI',sans-serif;

}



.logo-red{

    color:#D12B4B;

}



.logo-black{

    color:#1F2937;

}



/* Hero Title */

.hero-title{

    text-align:center;

    font-size:64px;

    font-weight:800;

    color:#111827;

    margin-top:20px;

    margin-bottom:10px;

}



/* Hero Subtitle */

.hero-subtitle{

    text-align:center;

    font-size:24px;

    color:#4B5563;

    margin-bottom:40px;

}



/* Upload Box */

div[data-testid="stFileUploader"]{

    background:#D12B4B;

    border:2px dashed #FF9FB0;

    border-radius:40px;

    padding:60px 20px;

}



/* Upload Text */

div[data-testid="stFileUploader"] label{

    color:white !important;

    font-size:24px !important;

    font-weight:700 !important;

}



/* Browse Button */

div[data-testid="stFileUploader"] button{

    background:white !important;

    color:#D12B4B !important;

    border:none !important;

    border-radius:50px !important;

    font-weight:700 !important;

    padding:10px 20px !important;

}



div[data-testid="stFileUploader"] button:hover{

    background:#FFE6EC !important;

    color:#B81E43 !important;

}



# =====================================================
# FEATURES
# =====================================================



st.markdown("<br>", unsafe_allow_html=True)



col1, col2, col3 = st.columns(3)



with col1:

    st.markdown("""

    <div style="

        background:white;

        padding:20px;

        border-radius:15px;

        border:1px dashed #CBD5E1;

        text-align:center;

    "> </style>

        <div style="font-size:32px;">🛡️</div>

        <div style="font-size:18px;font-weight:600;">

            Privacy-focused

        </div>

    </div>

    """, unsafe_allow_html=True)



with col2:

    st.markdown("""

    <div style="

        background:white;

        padding:20px;

        border-radius:15px;

        border:1px dashed #CBD5E1;

        text-align:center;

    ">

        <div style="font-size:32px;">📝</div>

        <div style="font-size:18px;font-weight:600;">

            Easy to use

        </div>

    </div>

    """, unsafe_allow_html=True)



with col3:

    st.markdown("""

    <div style="

        background:white;

        padding:20px;

        border-radius:15px;

        border:1px dashed #CBD5E1;

        text-align:center;

    ">

        <div style="font-size:32px;">⚡</div>

        <div style="font-size:18px;font-weight:600;">

            Lightning-fast

        </div>

    </div>

    """, unsafe_allow_html=True)



# =====================================================

# HEADER

# =====================================================

st.markdown("""

<div class="logo-container">

    <div class="logo">

        <span class="logo-red">hadi</span>

        <span class="logo-black">engine</span>

    </div>

</div>

""", unsafe_allow_html=True)



# =====================================================

# HERO SECTION

# =====================================================

st.markdown("""

<div class="hero-title">

Image to Text Converter

</div>



<div class="hero-subtitle">

Turn photos, scans, and images (JPEG, PNG) into Word, TXT, or PDF formats.

</div>

""", unsafe_allow_html=True)



# =====================================================

# UPLOAD FILE

# =====================================================

uploaded_file = st.file_uploader(

    "Upload or drag & drop your files",

    type=["jpg", "jpeg", "png"]

)



st.markdown(

"""

<div style="

text-align:center;

margin-top:-10px;

font-size:14px;

font-weight:600;

color:#FFFFFF;">

Size up to 100 MB

</div>

""",

unsafe_allow_html=True

)



# =====================================================

# FEATURES

# =====================================================

st.markdown("""

<div class="feature-container">



    <div class="feature-item">

        <div class="icon-box">🛡️</div>

        <div class="feature-text">Privacy-focused</div>

    </div>



    <div class="feature-item">

        <div class="icon-box">📝</div>

        <div class="feature-text">Easy to use</div>

    </div>



    <div class="feature-item">

        <div class="icon-box">⚡</div>

        <div class="feature-text">Lightning-fast</div>

    </div>



</div>

""", unsafe_allow_html=True)



# =====================================================

# OCR PROCESS

# =====================================================

if uploaded_file is not None:



    image = Image.open(uploaded_file)



    col1, col2 = st.columns([1, 1])



    with col1:

        st.subheader("Uploaded Image")

        st.image(image, use_container_width=True)



    with st.spinner("Extracting text..."):



        image_np = np.array(image)

        result = reader.readtext(image_np, detail=0)



        extracted_text = "\n".join(result)



    with col2:

        st.subheader("OCR Result")



        st.text_area(

            "",

            value=extracted_text,

            height=400

        )



        st.download_button(

            label="📥 Download TXT",

            data=extracted_text,

            file_name="ocr_result.txt",

            mime="text/plain",

            use_container_width=True

        )



    if not extracted_text:

        st.warning("No text detected in image.")
