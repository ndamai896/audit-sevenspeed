
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Audit Sistem Informasi Sevenspeed",
    page_icon="📊",
    layout="wide"
)

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

st.title("📊 FORM AUDIT SISTEM INFORMASI SEVENSPEED")
st.subheader("Kerangka Kerja COBIT 5")
st.caption("Instrumen evaluasi sistem informasi berdasarkan lima domain COBIT 5.")

st.info("Skala penilaian: 1 = Sangat tidak sesuai | 2 = Tidak sesuai | 3 = Cukup sesuai | 4 = Sesuai | 5 = Sangat sesuai")

with st.form("form_audit"):
    st.header("Identitas Auditor")
    auditor = st.text_input("Auditor")
    responden = st.text_input("Responden")
    unit_kerja = st.text_input("Unit kerja")

    hasil = []

    for domain, pertanyaan_list in instrumen.items():
        st.divider()
        st.header(f"DOMAIN {domain}")

        for i, pertanyaan in enumerate(pertanyaan_list, start=1):
            kode = f"{domain}-{i:02d}"
            st.subheader(kode)
            st.write(pertanyaan)

            skor = st.selectbox(
                "Skor penilaian",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: {
                    1: "1 - Sangat tidak sesuai",
                    2: "2 - Tidak sesuai",
                    3: "3 - Cukup sesuai",
                    4: "4 - Sesuai",
                    5: "5 - Sangat sesuai"
                }[x],
                key=f"skor_{kode}"
            )

            bukti = st.text_area("Bukti", key=f"bukti_{kode}")
            catatan = st.text_area("Catatan", key=f"catatan_{kode}")

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
        st.error("Mohon lengkapi identitas auditor, responden, dan unit kerja.")
    else:
        df = pd.DataFrame(hasil)
        st.session_state["hasil_audit"] = df
        st.session_state["identitas"] = {
            "Auditor": auditor,
            "Responden": responden,
            "Unit kerja": unit_kerja
        }

if "hasil_audit" in st.session_state:
    df = st.session_state["hasil_audit"]
    identitas = st.session_state["identitas"]

    st.divider()
    st.header("HASIL AUDIT COBIT 5")

    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah indikator", len(df))
    col2.metric("Total skor", int(df["Skor"].sum()))
    col3.metric("Rata-rata skor", round(df["Skor"].mean(), 2))

    st.subheader("Rekapitulasi per Domain")
    rekap = df.groupby("Domain").agg(
        Jumlah_Indikator=("Skor", "count"),
        Total_Skor=("Skor", "sum"),
        Rata_Rata=("Skor", "mean")
    ).reset_index()

    st.dataframe(rekap.round(2), use_container_width=True)

    st.subheader("Grafik Rata-rata Penilaian")
    grafik = rekap.set_index("Domain")[["Rata_Rata"]]
    st.bar_chart(grafik, y="Rata_Rata", y_label="Rata-rata skor")

    st.subheader("Detail Hasil Penilaian")
    st.dataframe(df, use_container_width=True)

    st.subheader("Identitas Audit")
    st.json(identitas)

    st.download_button(
        "Unduh hasil audit CSV",
        data=df.to_csv(index=False).encode("utf-8-sig"),
        file_name="hasil_audit_sevenspeed.csv",
        mime="text/csv"
    )
