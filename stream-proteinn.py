import streamlit as st
import base64

# Fungsi untuk encode audio dan tampilkan autoplay
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Fungsi menampilkan gambar avocado
def show_avocado_image(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <img src="data:image/webp;base64,{b64}" width="300">
        """
        st.markdown(md, unsafe_allow_html=True)

# Fungsi perhitungan protein
def calculate_protein_requirement(weight, activity_level, gender, age, goal):
    multiplier = {
        'Sedentary (tidak aktif)': 0.8,
        'Moderate (cukup aktif)': 1.2,
        'Active (sangat aktif)': 1.6
    }

    gender_age_adj = 0
    if gender == 'Perempuan' and age >= 60:
        gender_age_adj = -0.1
    elif gender == 'Laki-laki' and age >= 60:
        gender_age_adj = 0.1

    goal_adj = {
        'Menurunkan berat badan': -0.1,
        'Mempertahankan berat badan': 0,
        'Meningkatkan massa otot': 0.2
    }

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan = weight * goal_adj[goal]
    total = dasar + tambahan

    return total, dasar, tambahan

# Rekomendasi makanan
def show_food_recommendations():
    st.markdown("🍽 *Rekomendasi Makanan Tinggi Protein:*")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- 🥩 Daging ayam tanpa kulit")
        st.markdown("- 🐟 Ikan salmon atau tuna")
        st.markdown("- 🥚 Telur rebus")
    with col2:
        st.markdown("- 🧀 Tahu / Tempe")
        st.markdown("- 🥛 Susu rendah lemak / greek yogurt")
        st.markdown("- 🥜 Kacang almond / edamame")

# Fungsi utama
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    st.markdown("""
        <style>
        .stApp, html, body {
            background-color: #E6CCF5;
            font-family: 'Comic Sans MS', cursive;
            color: black !important;
        }
        label, .stSidebar, .css-1v3fvcr, .css-1d391kg {
            color: black !important;
        }
        button[kind="secondary"] {
            background-color: #7D5BA6 !important;
            color: white !important;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('🍳 Kalkulator Kebutuhan Protein Harian 😸')

    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        age = st.number_input('📅 Masukkan umur Anda (tahun):', min_value=1, step=1)
        gender = st.selectbox('🚻 Pilih jenis kelamin Anda:', ['Laki-laki', 'Perempuan'])
        height = st.number_input('📏 Masukkan tinggi badan Anda (cm):', min_value=50, step=1)
        weight = st.number_input('⚖ Masukkan berat badan Anda (kg):', min_value=1.0, step=0.1)
        activity_level = st.selectbox('🏃‍♀ Pilih tingkat aktivitas Anda:', [
            'Sedentary (tidak aktif)', 
            'Moderate (cukup aktif)', 
            'Active (sangat aktif)'
        ])
        goal = st.selectbox('🎯 Apa tujuan Anda?', [
            'Menurunkan berat badan', 
            'Mempertahankan berat badan', 
            'Meningkatkan massa otot'
        ])
        health_condition = st.selectbox('⚕ Apakah Anda memiliki kondisi medis tertentu?', [
            'Tidak ada', 
            'Diabetes', 
            'Penyakit ginjal', 
            'Penyakit hati',
            'Lainnya'
        ])

        if weight > 0 and height > 0 and age > 0:
            total, dasar, tambahan = calculate_protein_requirement(weight, activity_level, gender, age, goal)

            if health_condition == 'Penyakit ginjal':
                total *= 0.7
            elif health_condition == 'Penyakit hati':
                total *= 0.8
            elif health_condition == 'Diabetes':
                total *= 1.0

            with st.expander("📊 Lihat Hasil Perhitungan Kebutuhan Protein Anda"):
                st.success(f"🍗 Kebutuhan protein harian Anda untuk {goal.lower()} adalah sekitar {total:.1f} gram per hari! 😋")

                st.markdown(f"""
                    <ul>
                    <li><b>Berat badan:</b> {weight} kg</li>
                    <li><b>Tinggi badan:</b> {height} cm</li>
                    <li><b>Kebutuhan dasar:</b> {dasar:.1f} gram</li>
                    <li><b>Penyesuaian tujuan:</b> {tambahan:+.1f} gram</li>
                    <li><b>Kondisi medis:</b> {health_condition}</li>
                    </ul>
                    <p><b>Keterangan:</b> Angka ini merupakan estimasi total kebutuhan protein Anda. Jika Anda memiliki penyakit kronis, sebaiknya konsultasikan dengan ahli gizi atau dokter terlebih dahulu.</p>
                """, unsafe_allow_html=True)

                show_avocado_image("avocado.webp")
                autoplay_audio("snd_fragment_retrievewav-14728.mp3")

                st.markdown("### 🍛 Rekomendasi Makanan Lokal + Kandungan Protein")
                st.markdown("""
                <table style="width:100%">
                    <tr><th>Makanan</th><th>Kandungan Protein (per porsi)</th></tr>
                    <tr><td>Telur rebus (1 butir)</td><td>6 gram</td></tr>
                    <tr><td>Tempe goreng (2 potong)</td><td>10 gram</td></tr>
                    <tr><td>Tahu kukus (2 potong)</td><td>8 gram</td></tr>
                    <tr><td>Ikan kembung bakar (1 ekor)</td><td>20 gram</td></tr>
                    <tr><td>Daging ayam panggang (100 gram)</td><td>30 gram</td></tr>
                    <tr><td>Susu kedelai (1 gelas)</td><td>7 gram</td></tr>
                    <tr><td>Kacang tanah sangrai (1 genggam)</td><td>8 gram</td></tr>
                </table>
                """, unsafe_allow_html=True)

                show_food_recommendations()

    elif menu == 'Perkenalan Kelompok':
        st.subheader('👩‍🏫 Kelompok 5 (PMIP 1-E1)')
        st.write('📚 Anggota:')
        st.write('1. Chelsea Naila Darmayanti (2420581) 🐣')
        st.write('2. Fadliansyah (2420499) 🐈')
        st.write('3. Nabila Kirania Siti Saleha (2420629) 🦩')
        st.write('4. Sopian Darul Kamal (2420666) 🐿')
        st.write('5. Suci Rahma Safitri (2420668) 🦭')

    elif menu == 'Tentang Aplikasi':
        st.subheader('🌈 Tentang Aplikasi')
        st.image("foto patrik.gif", caption="Patrick makan demi protein!", use_container_width=True)
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, tinggi badan, usia, jenis kelamin, tingkat aktivitas, dan tujuan. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

if _name_ == '_main_':
    main()