import streamlit as st
import joblib
import pandas as pd

st.title("Heart Failure Prediction")

cadio_model = joblib.load('cardio_joblib')

# input features

col1, col2 = st.columns(2)    
type_admn = col1.radio('Type of Admission',['Emergency','OPD'])
if (type_admn == 'OPD'):
    toa = 1
else:
    toa = 0

gender = col2.radio('Gender',['Male','Female'])
if (gender == 'Male'):
    gen = 1
else:
    gen = 0    
    

age = st.slider('Age (years)', 1,100)
hb = st.number_input('Haemoglobin (g/dL)', 3.0,26.5)
glucose = st.number_input('Glucose (mg/dL)', 1.2,809.0)
urea = st.number_input('Urea (mg/dL)', 0.10,479.0)
ef = st.number_input('Ejection Fraction (%)', 14,60)



col3, col4 = st.columns(2)
diabetes = col3.radio("Diabetes Mellitus", ('Yes', 'No'))
if (diabetes == 'Yes'):
    dm = 1
else:
    dm = 0

prior_cmp = col4.radio('Prior CMP',('Yes', 'No'))
if (prior_cmp == 'Yes'):
    pcmp = 1
else:
    pcmp = 0
    

    
col5, col6 = st.columns(2)    
raised_ce = col5.radio('Raised Cardiac Enzymes',('Yes', 'No'))
if (raised_ce == 'Yes'):
    rce = 1
else:
    rce = 0  
    
stable_ang = col6.radio('Stable Angina',('Yes', 'No'))
if (stable_ang == 'Yes'):
    sa = 1
else:
    sa = 0

    
col7, col8 = st.columns(2)    
acute_cs = col7.radio('Acute Coronary Syndrome',('Yes', 'No'))
if (acute_cs == 'Yes'):
    acs = 1
else:
    acs = 0
        
atyp_cp = col8.radio('Atypical Chest Pain',('Yes', 'No'))
if (atyp_cp == 'Yes'):
    acp = 1
else:
    acp = 0


    
cor_ad = st.radio('Coronary Artery Disease',('Yes', 'No'))
if (cor_ad == 'Yes'):
    cad = 1
else:
    cad = 0    


    
def predict_heart_failure():
    column_names = [['AGE', 'HB', 'GLUCOSE', 'UREA', 'EF', 'GENDER_M',
       'TYPE OF ADMISSION-EMERGENCY/OPD_O', 'DM_1.0', 'CAD_1.0',
       'PRIOR CMP_1.0', 'RAISED CARDIAC ENZYMES_1.0', 'STABLE ANGINA_1.0',
       'ACS_1.0', 'ATYPICAL CHEST PAIN_1.0']]
    row = [age,hb,glucose,urea,ef,gen,toa,dm,cad,pcmp,rce,sa,acs,acp]
    X = pd.DataFrame([row],columns=column_names)
    prediction = cadio_model.predict(X)
    prediction = [ 0 if x < 0.5 else 1 for x in prediction]
    
    if prediction[0] ==1:
        st.warning('Heart Failure Alert')
    else:
        st.success('No Alert')
        
        

if (st.button('Predict')):
    predict_heart_failure()  
      
    
    
    
