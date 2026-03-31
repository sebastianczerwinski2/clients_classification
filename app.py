import streamlit as st
import pandas as pd
import joblib


model = joblib.load('model_klientow.pkl')
kolumny = joblib.load('column_names.pkl')


st.title("Predykcja Odejścia Klienta (Telco Churn)")
st.write("Wprowadź dane klienta, aby sprawdzić ryzyko rezygnacji z usług.")

st.subheader("Dane klienta:")
tenure = st.slider("Staż klienta (w miesiącach):", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("Miesięczne opłaty ($):", min_value=15.0, max_value=120.0, value=50.0)

st.subheader("Usługi:")
contract = st.selectbox("Rodzaj umowy:", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Rodzaj internetu:", ["DSL", "Fiber optic", "No"])


if st.button("Oblicz ryzyko odejścia"):
    
    dane_wejsciowe = pd.DataFrame(columns=kolumny)
    dane_wejsciowe.loc[0] = 0 
    
    dane_wejsciowe['tenure'] = tenure
    dane_wejsciowe['MonthlyCharges'] = monthly_charges
    

    if f'Contract_{contract}' in kolumny:
        dane_wejsciowe[f'Contract_{contract}'] = 1
        
    if f'InternetService_{internet}' in kolumny:
        dane_wejsciowe[f'InternetService_{internet}'] = 1


    prawdopodobienstwo = model.predict_proba(dane_wejsciowe)[0][1]
    
    st.markdown("---")
    
    if prawdopodobienstwo > 0.5:
        st.error(f"Ryzyko odejścia wynosi: **{prawdopodobienstwo * 100:.1f}%**")
        st.write("Sugerowane działanie: Skontaktuj się z klientem i zaoferuj zniżkę na przedłużenie umowy.")
    else:
        st.success(f"Klient jest lojalny. Ryzyko odejścia: **{prawdopodobienstwo * 100:.1f}%**")