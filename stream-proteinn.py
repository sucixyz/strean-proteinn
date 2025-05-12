import streamlit as st
import numpy as np

# Fungsi untuk menghitung persamaan regresi linier dan koefisien korelasi
def calculate_regression_equation(X, Y, var_name_x='x', var_name_y='y'):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_xy = np.sum(X * Y)
    sum_x_squared = np.sum(X**2)

    # Menghitung koefisien regresi
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n

    # Menghitung koefisien korelasi
    r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x_squared - sum_x**2) * (n * np.sum(Y**2) - np.sum(Y)**2))

    equation = f'{var_name_y} = {a:.2f} + {b:.2f}{var_name_x}'
    regression_info = {'equation': equation, 'intercept': a, 'slope': b, 'r_value': r}
    return regression_info

# Halaman aplikasi Streamlit
def main():
    st.title('Penentuan Persamaan Regresi Linearitas')

    # CSS untuk mengubah warna latar belakang, sidebar, dan ukuran font
    background_color = "#A60404"
    font_size = "25px"  # Ukuran font untuk teks biasa
    header_font_size = "40px"  # Ukuran font untuk header
    subheader_font_size = "30px"  # Ukuran font untuk subheader
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {background_color} !important;
            font-size: {font_size} !important;
        }}
        .st-bd {{
            background-color: {background_color} !important;
        }}
        h1 {{
            font-size: {header_font_size} !important;
        }}
        h2 {{
            font-size: {subheader_font_size} !important;
        }}
        </style>
        """, unsafe_allow_html=True)


    # Menambahkan opsi baru di select box
    menu = st.sidebar.selectbox("Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.write('Masukkan data X dan Y dalam bentuk tabel dengan dua kolom.')

        # Input data X dan Y dari pengguna dalam bentuk tabel
        data_input = st.text_area('Masukkan nilai X dan Y (pisahkan nilai X dan Y dengan koma, setiap pasangan nilai di baris baru):', height=150)
        var_name_x = st.text_input('Masukkan nama variabel untuk X:', 'x').strip()
        var_name_y = st.text_input('Masukkan nama variabel untuk Y:', 'y').strip()

        if data_input:
            data_lines = data_input.split('\n')
            X = np.array([float(line.split(',')[0].strip()) for line in data_lines if line])
            Y = np.array([float(line.split(',')[1].strip()) for line in data_lines if line])

            # Menghitung persamaan regresi linier dan koefisien korelasi
            regression_info = calculate_regression_equation(X, Y, var_name_x, var_name_y)

            # Menampilkan persamaan regresi linier, nilai slope (b), nilai intercept (a), dan nilai koefisien korelasi (r)
            st.markdown('### Persamaan Regresi Linier:')
            st.markdown(f'```{regression_info["equation"]}```', unsafe_allow_html=True)

            st.markdown('### Nilai Slope (b):')
            st.write(f'{regression_info["slope"]:.2f}')

            st.markdown('### Nilai Intercept (a):')
            st.write(f'{regression_info["intercept"]:.2f}')

            st.markdown('### Nilai Koefisien Korelasi (r):')
            st.write(f'{regression_info["r_value"]:.4f}')

    elif menu == 'Perkenalan Kelompok':
        st.subheader('Kelompok 3 (1E-PMIP)')
        st.write('Anggota:')
        st.write('1. Dhika Nurafliansyah (2320517)')
        st.write('2. Herni Khairunisa (2320528)')
        st.write('3. Ibnu Rafif (2320530)')
        st.write('4. Khaira Mutya Arrahman (2320533)')
        st.write('5. Marsya Kaila Avridita Mulyono (2320535)')

    elif menu == 'Tentang Aplikasi':
        st.subheader('Tentang Aplikasi')
        st.markdown('<style>.my-gif { width: 500px; height: auto; }</style>', unsafe_allow_html=True)
        st.markdown('<img src="https://lottiefiles.com/free-animation/dish-of-protein-foods-vvsS9mdShy" class="my-gif">', unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        st.write('Aplikasi penentu persamaan linear ini dirancang untuk memudahkan pengguna dalam melakukan perhitungan dalam penentuan persamaan linear dan mengurangi kesalahan penempatan data saat menghitung secara manual. Pengguna dapat memilih menu kalkulator untuk dapat menghitung persamaan regresi linear, nilai slope (b), nilai intersept (a), dan nilai koefisien regresi korelasi (r).')

if __name__ == '__main__':
    main()
