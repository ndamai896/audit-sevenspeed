
import streamlit as st
import pandas as pd

# ==========================================
# KONFIGURASI APLIKASI
# ==========================================

st.set_page_config(
    page_title="Audit Sevenspeed | COBIT 5",
    page_icon="🩵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# TEMA SOFT BLUE / SKY BLUE
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #F5FAFF;
}
[data-testid="stSidebar"] {
    background-color: #E5F2FF;
}
h1, h2, h3 {
    color: #174B78;
}
p, label, .stMarkdown {
    color: #365B7C;
}
div[data-testid="stMetric"] {
    background-color: #E6F3FF;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #C5E2FA;
}
.stButton > button,
.stFormSubmitButton > button {
    background-color: #65A9DD;
    color: white;
    border-radius: 9px;
    border: none;
    font-weight: bold;
}
.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #2878B9;
    color: white;
}
div[data-testid="stExpander"] {
    background-color: #FFFFFF;
    border: 1px solid #D4E9FA;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# INSTRUMEN AUDIT COBIT 5
# ==========================================

instrumen = {
    "EDM": [
        "Kejelasan pembagian tugas dan tanggung jawab dalam pengambilan keputusan terkait penggunaan sistem.",
        "Evaluasi manfaat penggunaan sistem terhadap pengelolaan pesanan dan pemantauan produksi.",
        "Pertimbangan risiko penggunaan sistem, seperti kehilangan data atau kesalahan informasi pesanan.",
        "Pengawasan terhadap sumber daya yang mendukung penggunaan dan pemeliharaan sistem.",
        "Ketersediaan informasi atau laporan mengenai kinerja sistem sebagai bahan pengawasan dan pengambilan keputusan."
    ],
    "APO": [
        "Kejelasan pembagian tanggung jawab pengguna dalam mengelola informasi pesanan dan produksi.",
        "Kesesuaian perencanaan penggunaan atau pengembangan sistem dengan kebutuhan operasional perusahaan.",
        "Identifikasi risiko seperti kehilangan data dan gangguan layanan sistem.",
        "Ketersediaan arahan atau pelatihan bagi pengguna dalam mengoperasikan sistem.",
        "Ketersediaan kebijakan atau prosedur untuk melindungi data pesanan dan informasi pelanggan."
    ],
    "BAI": [
        "Identifikasi kebutuhan pengguna terkait pengelolaan pesanan dan pemantauan produksi sebelum sistem diterapkan atau dikembangkan.",
        "Kesesuaian sistem dalam mendukung pencatatan dan pengelolaan informasi pesanan serta proses produksi.",
        "Penyampaian informasi dan arahan kepada pengguna ketika terdapat sistem baru atau perubahan sistem.",
        "Kejelasan persetujuan dan pencatatan dalam setiap perubahan sistem.",
        "Pelaksanaan pengujian sebelum perubahan atau sistem diterapkan dalam kegiatan operasional."
    ],
    "DSS": [
        "Pelaksanaan kegiatan operasional sistem, seperti pembaruan informasi pesanan dan status produksi secara rutin.",
        "Pencatatan dan penanganan gangguan atau permasalahan pada sistem.",
        "Analisis terhadap permasalahan sistem yang terjadi secara berulang untuk mengetahui penyebabnya.",
        "Ketersediaan prosedur pencadangan dan pemulihan data apabila terjadi kehilangan atau kerusakan data.",
        "Pembatasan akses terhadap sistem berdasarkan tugas dan kewenangan masing-masing pengguna."
    ],
    "MEA": [
        "Pelaksanaan pemantauan kinerja sistem informasi secara berkala.",
        "Ketersediaan catatan atau laporan untuk memantau pesanan dan proses produksi.",
        "Evaluasi pengendalian internal terhadap data pesanan dan produksi secara berkala.",
        "Pemeriksaan kesesuaian informasi pesanan dan status produksi dengan bukti pendukung.",
        "Pemeriksaan kesesuaian penggunaan sistem dengan kebijakan internal dan ketentuan yang berlaku."
    ]
}

# ==========================================
# ANALISIS DAN REKOMENDASI
# ==========================================

analisis_domain = {
    "EDM": {
        "analisis": "Pengawasan dan evaluasi manfaat sistem sudah berjalan cukup baik. Namun, dokumentasi pembagian tanggung jawab dan identifikasi risiko masih perlu ditingkatkan.",
        "rekomendasi": "Membuat dokumentasi pembagian tanggung jawab, melakukan evaluasi kinerja sistem secara berkala, dan menyusun identifikasi risiko penggunaan sistem."
    },
    "APO": {
        "analisis": "Perencanaan dan pengelolaan sistem telah mendukung kebutuhan operasional. Namun, pengelolaan risiko dan pembagian tanggung jawab masih perlu diperkuat.",
        "rekomendasi": "Menyusun prosedur pengelolaan risiko, memperjelas tanggung jawab pengguna, serta meningkatkan dokumentasi perlindungan data."
    },
    "BAI": {
        "analisis": "Penerapan sistem telah membantu kegiatan operasional. Namun, identifikasi kebutuhan dan dokumentasi perubahan sistem masih perlu ditingkatkan.",
        "rekomendasi": "Mendokumentasikan kebutuhan pengguna, membuat prosedur persetujuan perubahan sistem, dan menyimpan hasil pengujian sistem."
    },
    "DSS": {
        "analisis": "Operasional sistem sudah berjalan cukup baik, tetapi pencatatan gangguan, analisis masalah, dan pengaturan hak akses masih perlu diperbaiki.",
        "rekomendasi": "Membuat prosedur penanganan gangguan, melakukan analisis penyebab masalah, serta menyusun jadwal pencadangan data."
    },
    "MEA": {
        "analisis": "Pemantauan dan evaluasi sistem sudah dilakukan, tetapi belum sepenuhnya terstruktur dan terdokumentasi secara berkala.",
        "rekomendasi": "Melakukan evaluasi kinerja sistem secara rutin, menyusun laporan pemantauan, dan meningkatkan pemeriksaan pengendalian internal."
    }
}

# ==========================================
# SIDEBAR NAVIGASI
# ==========================================

st.sidebar.markdown("# 🩵 SEVENSPEED")
st.sidebar.caption("AUDIT SISTEM INFORMASI")
st.sidebar.divider()

menu = st.sidebar.radio(
    "MENU NAVIGASI",
    [
        "Dashboard",
        "Form Audit",
        "Hasil Audit",
        "Analisis & Rekomendasi"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "Kerangka kerja: COBIT 5\n\n"
    "Objek: Sevenspeed Kudus\n\n"
    "Jumlah indikator: 25"
)

# ==========================================
# HEADER APLIKASI
# ==========================================

st.title("🩵 Audit Sistem Informasi Sevenspeed")
st.caption(
    "Aplikasi Evaluasi Sistem Informasi "
    "Menggunakan Kerangka Kerja COBIT 5"
)

# ==========================================
# DASHBOARD
# ==========================================

if menu == "Dashboard":

    st.subheader("Dashboard Audit")

    st.markdown("""
    Selamat datang di aplikasi Audit Sistem Informasi Sevenspeed.
    Aplikasi ini digunakan untuk melakukan penilaian berdasarkan
    lima domain COBIT 5, yaitu EDM, APO, BAI, DSS, dan MEA.
    """)

    if "hasil_audit" in st.session_state:

        df = st.session_state["hasil_audit"]
        rekap = df.groupby("Domain").agg(
            Total_Skor=("Skor", "sum"),
            Rata_Rata=("Skor", "mean")
        ).reset_index()

        c1, c2, c3 = st.columns(3)
        c1.metric("Jumlah Indikator", len(df))
        c2.metric("Total Skor", int(df["Skor"].sum()))
        c3.metric("Rata-rata Skor", f"{df['Skor'].mean():.2f}")

        st.subheader("Ringkasan Penilaian Domain")
        st.bar_chart(
            rekap.set_index("Domain")[["Rata_Rata"]],
            y="Rata_Rata",
            y_label="Rata-rata skor"
        )

    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Jumlah Domain", "5")
        c2.metric("Jumlah Indikator", "25")
        c3.metric("Skala Penilaian", "1–5")

        st.info(
            "Belum terdapat hasil audit. "
            "Silakan buka menu Form Audit untuk memulai penilaian."
        )

# ==========================================
# FORM AUDIT
# ==========================================

elif menu == "Form Audit":

    st.header("Form Audit Sistem Informasi")
    st.write("Isi identitas dan lakukan penilaian pada seluruh indikator.")

    st.info(
        "Skala penilaian: 1 = Sangat tidak sesuai, "
        "2 = Tidak sesuai, 3 = Cukup sesuai, "
        "4 = Sesuai, 5 = Sangat sesuai."
    )

    with st.form("form_audit"):

        st.subheader("Identitas Auditor")

        auditor = st.text_input("Auditor")
        responden = st.text_input("Responden")
        unit_kerja = st.text_input("Unit kerja")

        hasil = []

        for domain, pertanyaan_list in instrumen.items():

            st.divider()
            st.subheader(f"DOMAIN {domain}")

            for i, pertanyaan in enumerate(pertanyaan_list, start=1):

                kode = f"{domain}-{i:02d}"

                st.markdown(f"**{kode}**")
                st.write(pertanyaan)

                skor = st.selectbox(
                    "Skor penilaian",
                    [1, 2, 3, 4, 5],
                    format_func=lambda x: {
                        1: "1 - Sangat tidak sesuai",
                        2: "2 - Tidak sesuai",
                        3: "3 - Cukup sesuai",
                        4: "4 - Sesuai",
                        5: "5 - Sangat sesuai"
                    }[x],
                    key=f"skor_{kode}"
                )

                bukti = st.text_area(
                    "Bukti",
                    key=f"bukti_{kode}"
                )

                catatan = st.text_area(
                    "Catatan",
                    key=f"catatan_{kode}"
                )

                hasil.append({
                    "Domain": domain,
                    "Kode": kode,
                    "Pertanyaan": pertanyaan,
                    "Skor": skor,
                    "Bukti": bukti,
                    "Catatan": catatan
                })

        proses = st.form_submit_button(
            "PROSES HASIL AUDIT",
            use_container_width=True
        )

    if proses:

        if not auditor.strip() or not responden.strip() or not unit_kerja.strip():

            st.error(
                "Mohon lengkapi identitas auditor, responden, "
                "dan unit kerja."
            )

        else:

            df = pd.DataFrame(hasil)

            st.session_state["hasil_audit"] = df
            st.session_state["identitas"] = {
                "Auditor": auditor,
                "Responden": responden,
                "Unit kerja": unit_kerja
            }

            st.success(
                "Hasil penilaian berhasil diproses. "
                "Silakan buka menu Hasil Audit."
            )

# ==========================================
# HASIL AUDIT
# ==========================================

elif menu == "Hasil Audit":

    st.header("Hasil Audit COBIT 5")

    if "hasil_audit" not in st.session_state:

        st.warning("Belum ada hasil audit yang diproses.")

    else:

        df = st.session_state["hasil_audit"]
        identitas = st.session_state["identitas"]

        c1, c2, c3 = st.columns(3)

        c1.metric("Jumlah Indikator", len(df))
        c2.metric("Total Skor", int(df["Skor"].sum()))
        c3.metric("Rata-rata", f"{df['Skor'].mean():.2f}")

        st.subheader("Identitas Audit")
        st.json(identitas)

        rekap = df.groupby("Domain").agg(
            Jumlah_Indikator=("Skor", "count"),
            Total_Skor=("Skor", "sum"),
            Rata_Rata=("Skor", "mean")
        ).reset_index()

        st.subheader("Rekapitulasi Hasil Audit")
        st.dataframe(
            rekap.round(2),
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Grafik Rata-rata Penilaian")
        st.bar_chart(
            rekap.set_index("Domain")[["Rata_Rata"]],
            y="Rata_Rata",
            y_label="Rata-rata skor"
        )

        st.subheader("Detail Hasil Penilaian")
        st.dataframe(df, use_container_width=True)

        st.download_button(
            "📥 Unduh Hasil Audit CSV",
            data=df.to_csv(index=False).encode("utf-8-sig"),
            file_name="hasil_audit_sevenspeed.csv",
            mime="text/csv"
        )

# ==========================================
# ANALISIS DAN REKOMENDASI
# ==========================================

elif menu == "Analisis & Rekomendasi":

    st.header("Analisis dan Rekomendasi Perbaikan")

    if "hasil_audit" not in st.session_state:

        st.warning(
            "Silakan isi dan proses form audit terlebih dahulu."
        )

    else:

        df = st.session_state["hasil_audit"]

        rekap = df.groupby("Domain").agg(
            Rata_Rata=("Skor", "mean")
        ).reset_index()

        for _, baris in rekap.iterrows():

            domain = baris["Domain"]
            skor = baris["Rata_Rata"]

            with st.expander(
                f"Domain {domain} — Rata-rata {skor:.2f}",
                expanded=True
            ):

                st.markdown("**Analisis:**")
                st.write(analisis_domain[domain]["analisis"])

                st.markdown("**Rekomendasi Perbaikan:**")
                st.write(analisis_domain[domain]["rekomendasi"])

        st.divider()
        st.subheader("Kesimpulan Hasil Audit")

        rata = df["Skor"].mean()

        tertinggi = rekap.loc[rekap["Rata_Rata"].idxmax()]
        terendah = rekap.loc[rekap["Rata_Rata"].idxmin()]

        st.write(
            f"Berdasarkan penilaian terhadap {len(df)} indikator "
            f"pada lima domain COBIT 5, diperoleh total skor "
            f"{df['Skor'].sum()} dengan rata-rata {rata:.2f}."
        )

        st.write(
            f"Domain dengan rata-rata tertinggi adalah "
            f"{tertinggi['Domain']} sebesar "
            f"{tertinggi['Rata_Rata']:.2f}."
        )

        st.write(
            f"Domain dengan rata-rata terendah adalah "
            f"{terendah['Domain']} sebesar "
            f"{terendah['Rata_Rata']:.2f}."
        )

        st.caption(
            "Interpretasi dan rekomendasi ini merupakan "
            "contoh analisis berdasarkan hasil penilaian. "
            "Data simulasi bukan hasil wawancara lapangan."
        )
