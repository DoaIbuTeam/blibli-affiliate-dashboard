import streamlit as st
import pandas as pd
import random

# Konfigurasi Halaman
st.set_page_config(page_title="Blibli Affiliate 2.0", page_icon="💙", layout="wide")

st.title("💙 Blibli Affiliate 2.0 Dashboard")
st.caption("Dashboard Gamifikasi & Tools Akselerasi Affiliator Interaktif")

# --- SIDEBAR: Profile & Daily Mission Dinamis (User Input) ---
with st.sidebar:
    st.header("👤 Profile Affiliator")

    # Input Data Profile User
    nama_user = st.text_input("Nama Anda:", value="Budi Affiliator")
    level_user = st.selectbox("Level Affiliator:", ["Bronze Creator 🥉", "Silver Creator 🥈", "Gold Creator 🌟", "Platinum Creator 💎"])
    target_transaksi = st.number_input("Target Transaksi Harian:", min_value=1, value=10)
    realisasi_transaksi = st.number_input("Transaksi Selesai Hari Ini:", min_value=0, value=7)

    # Progress Bar Otomatis
    progress = min(realisasi_transaksi / target_transaksi, 1.0)
    st.progress(progress, text=f"Progress: {realisasi_transaksi}/{target_transaksi} Transaksi")

    st.divider()
    st.subheader("🎯 Custom Daily Mission")

    # User membuat misi harian sendiri
    misi1 = st.text_input("Misi 1:", value="Bagikan 3 Link Produk Hari Ini")
    check1 = st.checkbox(misi1, value=True)

    misi2 = st.text_input("Misi 2:", value="Dapatkan 5 Klik")
    check2 = st.checkbox(misi2, value=True)

    misi3 = st.text_input("Misi 3:", value="Capai 1 Transaksi Harian")
    check3 = st.checkbox(misi3, value=False)

    if check1 and check2 and check3:
        st.balloons()
        st.success(f"🎉 Selamat {nama_user}! Semua Daily Mission Selesai! (+100 Poin Blibli)")

# --- MAIN CONTENT ---
col1, col2 = st.columns([1, 1])

# Fitur 1: 1-Click Link Generator
with col1:
    st.subheader("🔗 1-Click Affiliate Link Generator")
    original_link = st.text_input("Paste URL Produk Blibli di sini:", placeholder="https://www.blibli.com/p/...")
    custom_subid = st.text_input("Masukkan Sub-ID / Tag (Opsional):", placeholder="promo-instagram")

    if st.button("⚡ Generate Link Affiliate", type="primary"):
        if original_link:
            sub_tag = f"&sub_id={custom_subid}" if custom_subid else ""
            aff_link = f"https://blibli.com/aff/{random.randint(10000, 99999)}?src=dashboard{sub_tag}"

            st.success("Link Berhasil Dibuat!")
            st.code(aff_link, language="text")

            st.markdown("**Caption Promo Auto-Generated:**")
            caption = f"Promo spesial Blibli dari {nama_user}! Cek produknya di sini sebelum kehabisan: {aff_link} #BlibliAffiliate #PromoBlibli"
            st.text_area("Copy Caption:", value=caption, height=100)
        else:
            st.warning("Masukkan link produk terlebih dahulu.")

# Fitur 2: Regional Ranking Dinamis
with col2:
    st.subheader("🏆 Real-Time Regional Ranking")
    region = st.selectbox("Pilih Wilayah:", ["Nasional", "DKI Jakarta", "Jawa Barat", "Jawa Timur", "DI Yogyakarta"])

    # Menampilkan data user secara dinamis di tabel ranking
    data = {
        "Rank": [1, 2, 3, 4, 5],
        "Nama Affiliator": ["Siti A.", f"{nama_user} (Anda)", "Rian T.", "Dewi K.", "Eko P."],
        "Wilayah": [region] * 5,
        "Total Klik": [1250, 980 + (realisasi_transaksi * 10), 850, 620, 500],
        "Estimasi Komisi": ["Rp 2.500.000", f"Rp {1500000 + (realisasi_transaksi * 50000):,}", "Rp 1.700.000", "Rp 1.240.000", "Rp 1.000.000"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, hide_index=True, use_container_width=True)

st.divider()

# Fitur 3: Kalkulator Estimasi Komisi
st.subheader("🧮 Kalkulator Estimasi Komisi Blibli")
c1, c2, c3 = st.columns(3)
with c1:
    harga_produk = st.number_input("Harga Produk (Rp):", min_value=0, value=150000, step=10000)
with c2:
    kategori = st.selectbox("Kategori Produk:", ["Elektronik (3%)", "Fashion (8%)", "Kebutuhan Harian (5%)", "Otomotif (4%)"])
    persen = float(kategori.split("(")[1].replace("%)", "")) / 100
with c3:
    estimasi = harga_produk * persen
    st.metric("Estimasi Komisi per Penjualan", f"Rp {int(estimasi):,}")
