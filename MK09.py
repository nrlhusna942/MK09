import streamlit as st

# 1. Keperluan Antaramuka (UI) Streamlit
st.title("Kalkulator BMI Klinik")

st.subheader("Pengiraan BMI Pesakit")
berat_input = st.text_input("Berat (kg):")
tinggi_input = st.text_input("Tinggi (meter):")

# 2. Keperluan Pengendalian Pengecualian (BMI)
if st.button("Kira BMI"):
    try:
        # Penukaran jenis data ke float (boleh mencetuskan ValueError)
        berat = float(berat_input)
        tinggi = float(tinggi_input)
        
        # Pengiraan BMI (boleh mencetuskan ZeroDivisionError)
        bmi = berat / (tinggi * tinggi)
        
    except ValueError:
        st.error("Ralat: Sila masukkan nilai nombor yang sah untuk berat dan tinggi.")
        
    except ZeroDivisionError:
        st.error("Ralat: Tinggi tidak boleh bernilai 0.0.")
        
    except Exception as e:
        st.error(f"Ralat yang tidak dijangka berlaku: {e}")
        
    else:
        # Dipaparkan jika tiada ralat berlaku
        st.success(f"Pengiraan Berjaya! Nilai BMI Pesakit ialah: {bmi:.2f}")
        
    finally:
        # Mesej yang sentiasa dipaparkan
        st.info("Sistem selesai memproses permintaan anda.")

st.divider()

# 3. Keperluan Fail I/O (Papar Rekod Lama)
if st.button("Papar Rekod Lama"):
    try:
        with open("rekod_pesakit.txt", "r") as fail:
            kandungan = fail.read()
            st.text(kandungan)
            
    except FileNotFoundError:
        st.warning("Fail rekod belum diwujudkan.")
        
    except Exception as e:
        st.error(f"Ralat semasa membaca fail: {e}")