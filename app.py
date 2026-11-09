import streamlit as st
from google import genai
from PIL import Image

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Juragan Konten AI - Studio Affiliate",
    page_icon="👑",
    layout="centered"
)

# Styling CSS: Tema Ungu Elegan & Kotak Kontras Terang
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7c3aed, #db2777);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        padding: 0.75rem 1rem;
        width: 100%;
        box-shadow: 0 4px 14px rgba(124, 58, 237, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #6d28d9, #be185d);
        color: #fff;
    }
    .result-box {
        background-color: #ffffff;
        color: #1f2937;
        padding: 24px;
        border-radius: 14px;
        border: 2px solid #7c3aed;
        margin-bottom: 25px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.2);
    }
    .result-box h4 {
        color: #6d28d9;
        margin-top: 0;
        font-weight: 800;
        border-bottom: 2px solid #f3e8ff;
        padding-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Utama Aplikasi
st.title("👑 Juragan Konten AI Studio")
st.markdown("Pencetak storyboard & skrip video affiliate berbasis AI nyata yang membaca foto produkmu!")
st.markdown("---")

# Masukkan API Key Gemini (Bisa ditaruh di secrets streamlit atau input manual)
# Untuk aman, kita buat input API Key di sidebar atau langsung pakai st.secrets
api_key = st.text_input("🔑 Masukkan Gemini API Key Anda:", type="password", placeholder="AIzaSy...")

# --- FORM INPUT UTAMA ---
uploaded_file = st.file_uploader("📸 Upload Foto Produk di Sini", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)
with col1:
    ad_style = st.selectbox(
        "🎯 Pilih Gaya Promosi",
        [
            "Soft Selling (Natural & Emosional)",
            "Hard Selling (Tegas & Diskon Kilat)",
            "UGC Unboxing Fast (Review Cepat & Asli)",
            "Problem-Solution (Nembak Masalah)",
            "Before-After (Transformasi Nyata)",
            "FOMO / Urgensi Ekstrem (Takut Kehabisan)",
            "POV (Point of View Pengguna)",
            "Educational / Racun Edukasi"
        ]
    )
    
    duration = st.selectbox(
        "⏱️ Pilih Durasi Video",
        [
            "10 Detik (1 Frame Padat)", 
            "20 Detik (2 Frame Bersambung)", 
            "30 Detik (3 Frame Bersambung)"
        ]
    )

with col2:
    location_type = st.selectbox(
        "📍 Pilih Lokasi Syuting (Opsional)",
        [
            "Auto / Menyesuaikan Karakter Produk",
            "Indoor (Kamar Minimalis / Studio Estetik)",
            "Outdoor (Kafe Hits / Alam Terbuka / Jalanan)"
        ]
    )
    
    talent_ref = st.text_input(
        "👤 Referensi Talent Kustom (Opsional)",
        placeholder="Cth: Model lokal, casual, hijab pastel..."
    )

st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("🚀 GENERATE STORYBOARD DENGAN AI")

# --- PROSES & HASIL OUTPUT MENGGUNAKAN GEMINI API ---
if generate_btn:
    if not api_key:
        st.error("⚠️ Masukkan Gemini API Key terlebih dahulu di kolom atas!")
    elif uploaded_file is not None:
        try:
            # Inisialisasi Gemini Client
            client = genai.Client(api_key=api_key)
            image = Image.open(uploaded_file)
            
            with st.spinner("🤖 AI sedang menganalisis foto produk secara mendalam..."):
                prompt_ai = f"""
                Bertindaklah sebagai expert affiliate content creator. Analisis foto produk yang diunggah ini.
                Buatkan storyboard video TikTok/Reels berdasarkan:
                - Gaya Promosi: {ad_style}
                - Durasi: {duration}
                - Lokasi Syuting: {location_type}
                - Referensi Talent: {talent_ref if talent_ref else 'Standar profesional'}
                
                Berikan output dengan format yang jelas terstruktur untuk setiap frame (Visual, Naskah Dialog yang natural dan sesuai produk asli, serta Prompt Video AI). Pastikan naskahnya sangat menjual dan relevan langsung dengan produk di foto!
                """
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image, prompt_ai]
                )
                
                st.success("✅ Analisis produk dan pembuatan skrip selesai!")
                st.markdown("---")
                
                # Tampilkan hasil dari AI
                st.markdown("""
                <div class="result-box">
                    <h4><b>🎬 Hasil Storyboard & Skrip Juragan Konten AI</b></h4>
                </div>
                """, unsafe_allow_html=True)
                
                st.text_area("📋 Salin Seluruh Hasil Script di Bawah Ini:", response.text, height=350)
                
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses gambar dengan AI: {e}")
    else:
        st.warning("⚠️ Boss, silakan upload foto produknya dulu di atas!")
else:
    st.info("👆 Masukkan API Key, lengkapi pilihan, upload foto produk, lalu klik **GENERATE STORYBOARD DENGAN AI**.")
