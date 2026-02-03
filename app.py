import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = {
    'gramatur': [125, 150, 175, 150, 125, 175, 150, 125, 175, 150],
    'L': [400, 350, 300, 400, 350, 300, 400, 350, 300, 400],
    'W': [300, 280, 250, 300, 280, 250, 300, 280, 250, 300],
    'H': [250, 200, 180, 250, 200, 180, 250, 200, 180, 250],
    'RH': [70, 80, 90, 75, 85, 70, 80, 90, 75, 85],
    'BCT': [3200, 2800, 2100, 3000, 2500, 2900, 2700, 2000, 2600, 2400]
}
df = pd.DataFrame(data)
X = df[['gramatur', 'L', 'W', 'H', 'RH']]
y = df['BCT']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

st.title("HortiPack v3.0 - Prediksi BCT Kemasan")
komoditas = st.selectbox("Komoditas", ['Mangga', 'Salak', 'Jeruk', 'Tomat', 'Cabai'])
gramatur = st.slider("Gramatur (g/m²)", 100, 200, 150)
RH = st.slider("RH (%)", 60, 95, 80)

if st.button("Hitung BCT"):
    input_data = pd.DataFrame({'gramatur': [gramatur], 'L': [400], 'W': [300], 'H': [250], 'RH': [RH]})
    bct = model.predict(input_data)[0]
    st.success(f"Prediksi BCT: {bct:.0f} Newton")
    
    
