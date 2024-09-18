import streamlit as st
import joblib
import pandas as pd

st.title("Heart Failure Prediction")

cardio_model = joblib.load('cvnn_joblib')

# input features    
    
urea = st.number_input('Urea (mg/dL)', 0.10,479.0)
ef = st.number_input('Ejection Fraction (%)', 14,60)
hb = st.number_input('Haemoglobin (g/dL)', 3.0,26.5)
creatinine = st.number_input('Creatinine (mg/dL)', 0.65,15.63)


col1, col2 = st.columns(2)

acute_cs = col1.radio('Acute Coronary Syndrome',('Yes', 'No'))
if (acute_cs == 'Yes'):
    acs = 1
else:
    acs = 0

prior_cmp = col2.radio("Prior Cardiomyopathy", ('Yes', 'No'))
if (prior_cmp == 'Yes'):
    pcmp = 1
else:
    pcmp = 0
    
col3, col4 = st.columns(2)

cor_ad = col3.radio('Coronary Artery Disease',('Yes', 'No'))
if (cor_ad == 'Yes'):
    cad = 1
else:
    cad = 0 

dia_m = col4.radio('Diabetes Mellitus',('Yes', 'No'))
if (dia_m == 'Yes'):
    dm = 1
else:
    dm = 0 
    
stable_sa = st.radio('Stable Angina',('Yes', 'No'))
if (stable_sa == 'Yes'):
    sa = 1
else:
    sa = 0       

                
def predict_heart_failure():
    column_names = [['EF', 'ACS_1.0', 'PRIOR CMP_1.0', 'UREA', 'HB', 'CREATININE', 'CAD_1.0',
       'DM_1.0', 'STABLE ANGINA_1.0']]
    row = [ef,acs,pcmp,urea,hb,creatinine,cad,dm,sa]
    X = pd.DataFrame([row],columns=column_names)
    prediction = cardio_model.predict(X)
    prediction = [ 0 if x < 0.5 else 1 for x in prediction]
    
    if prediction[0] ==1:
        st.warning('Heart Failure Alert')
    else:
        st.success('No Alert')
        
        

if (st.button('Predict')):
    predict_heart_failure()  
      
    
    
    
