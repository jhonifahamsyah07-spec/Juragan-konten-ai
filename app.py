import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Juragan Konten AI - Studio Affiliate",
    page_icon="👑",
    layout="centered"
)

# Styling CSS: Tema Ungu Elegan & Kotak Kontras Terang untuk Sekali Copy
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
st.markdown("Pencetak storyboard & skrip video affiliate otomatis, rapi, dan **sekali copy langsung jadi!**")
st.markdown("---")

# --- FORM INPUT UTAMA (LANGSUNG MUNCUL DI MUKA) ---
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
generate_btn = st.button("🚀 GENERATE STORYBOARD JURAGAN")

# --- PROSES & HASIL OUTPUT (SEKALI COPY) ---
if generate_btn:
    if uploaded_file is not None:
        st.success(f"✅ Produk berhasil dianalisis! Gaya: **{ad_style.split(' ')[0]}** | Durasi: **{duration}**")
        st.markdown("---")
        
        loc_desc = f"Setting lokasi: {location_type}." if "Auto" not in location_type else "Setting lokasi natural."
        talent_desc = f"Karakter talent: {talent_ref}." if talent_ref else "Karakter talent profesional."
        
        # Logika Output Sesuai Pilihan Durasi
        if "10 Detik" in duration:
            full_text_f1 = f"""[FRAME 1 - 0-10s (Format Padat)]
VISUAL & SINEMATIK:
- Lokasi: {loc_desc}
- Talent: {talent_desc} Ekspresi sangat antusias, close-up produk dengan pencahayaan terang dan estetik.

NASKAH & DIALOG:
"Wah gila sih ini, bener-bener penyelamat banget buat atasi masalah kita sehari-hari! Kualitasnya juara, praktis, dan gampang banget dipakai. Mumpung lagi ada promo spesial, buruan checkout sekarang sebelum kehabisan di keranjang kuning!"

GOOGLE FLOW PROMPT:
Cinematic 4k e-commerce shot, dynamic product showcase, fast paced transition, perfect lighting."""

            st.markdown(f"""
            <div class="result-box">
                <h4><b>🎬 Frame 1 (0-10s) — Sekali Copy</b></h4>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Salin Seluruh Teks di Bawah Ini:", full_text_f1, height=220)
            
        elif "20 Detik" in duration:
            full_text_f1 = f"""[FRAME 1 - 0-10s (Hook & Masalah)]
VISUAL & SINEMATIK:
- Lokasi: {loc_desc}
- Talent: {talent_desc} Adegan unboxing cepat, ekspresi penasaran, menyorot masalah penonton.

NASKAH & DIALOG:
"Sumpah kaget banget pas paket ini datang, sebagus itu aslinya! Buat kalian yang sering banget ngalamin masalah ini, wajib banget tonton video ini sampai habis."

GOOGLE FLOW PROMPT:
Unboxing package moment, close up hands opening box, bright aesthetic room."""

            full_text_f2 = f"""[FRAME 2 - 10-20s (Solusi & CTA)]
VISUAL & SINEMATIK:
- Lokasi: {loc_desc}
- Talent: {talent_desc} Demonstrasi produk beraksi, hasil nyata, gestur menunjuk keranjang kuning.

NASKAH & DIALOG:
"Setelah dicoba sendiri, hasilnya beneran di luar dugaan! Gampang dipakai, hemat waktu, dan awet banget. Mumpung stok masih ada dan lagi diskon kilat, langsung klik keranjang kuning di bawah ya!"

GOOGLE FLOW PROMPT:
Product in action demonstration, happy smiling model pointing down, high conversion e-commerce style."""

            st.markdown(f"""
            <div class="result-box">
                <h4><b>🎬 Frame 1 (0-10s) — Bagian Awal</b></h4>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Salin Teks Frame 1:", full_text_f1, height=190)

            st.markdown(f"""
            <div class="result-box" style="margin-top: 20px;">
                <h4><b>🎬 Frame 2 (10-20s) — Bagian Akhir & CTA</b></h4>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("📋 Salin Teks Frame 2:", full_text_f2, height=190)
            
        else: # 30 Detik
            full_text_f1 = f"""[FRAME 1 - 0-10s (Hook & Unboxing)]
VISUAL & SINEMATIK: {loc_desc} {talent_desc} Pembuka sinematik memancing rasa penasaran.
NASKAH: "Jangan beli barang ini sebelum kalian tahu rahasia kelebihannya! Paketnya udah nyampe dan kita langsung buktikan sekarang." """

            full_text_f2 = f"""[FRAME 2 - 10-20s (Ulasan & Bukti)]
VISUAL & SINEMATIK: {loc_desc} {talent_desc} Close-up detail keunggulan produk secara fungsional.
NASKAH: "Tekstur dan kualitas bahannya beda banget dari pasaran. Pas dicoba, langsung terasa bedanya dalam hitungan detik aja." """

            full_text_f3 = f"""[FRAME 3 - 20-30s (Solusi Akhir & CTA)]
VISUAL & SINEMATIK: {loc_desc} {talent_desc} Penutup manis dengan gestur kuat mengarah ke keranjang kuning.
NASKAH: "Udah harganya ramah di kantong, garansi kualitas pula. Yuk buruan amankan stoknya sebelum kehabisan, klik keranjang kuning sekarang juga!"
GOOGLE FLOW PROMPT (Full): High conversion e-commerce sequence, smooth transitions, 4k."""

            st.markdown(f"<div class='result-box'><h4><b>🎬 Frame 1 (0-10s)</b></h4></div>", unsafe_allow_html=True)
            st.text_area("📋 Salin Frame 1:", full_text_f1, height=140)

            st.markdown(f"<div class='result-box' style='margin-top: 15px;'><h4><b>🎬 Frame 2 (10-20s)</b></h4></div>", unsafe_allow_html=True)
            st.text_area("📋 Salin Frame 2:", full_text_f2, height=140)

            st.markdown(f"<div class='result-box' style='margin-top: 15px;'><h4><b>🎬 Frame 3 (20-30s)</b></h4></div>", unsafe_allow_html=True)
            st.text_area("📋 Salin Frame 3:", full_text_f3, height=150)
            
    else:
        st.warning("⚠️ Boss, silakan upload foto produknya dulu di atas sebelum pencet tombol generate!")
else:
    st.info("👆 Lengkapi pilihan di atas, upload foto produk, lalu klik tombol **GENERATE STORYBOARD JURAGAN**.")
