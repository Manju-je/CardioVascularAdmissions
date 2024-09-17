import streamlit as st
import joblib
import pandas as pd

st.title("Heart Failure Prediction")

cardio_model = joblib.load('cv_joblib')

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
    
urea = st.number_input('Urea (mg/dL)', 0.10,479.0)
ef = st.number_input('Ejection Fraction (%)', 14,60)


col3, col4 = st.columns(2)
prior_cmp = col3.radio("Prior Cardiomyopathy", ('Yes', 'No'))
if (prior_cmp == 'Yes'):
    pcmp = 1
else:
    pcmp = 0
    
raised_ce = col4.radio('Raised Cardiac Enzymes',('Yes', 'No'))
if (raised_ce == 'Yes'):
    rce = 1
else:
    rce = 0 
    
col5, col6 = st.columns(2)    
stable_sa = col5.radio('Stable Angina',('Yes', 'No'))
if (stable_sa == 'Yes'):
    sa = 1
else:
    sa = 0  
     

acute_cs = col6.radio('Acute Coronary Syndrome',('Yes', 'No'))
if (acute_cs == 'Yes'):
    acs = 1
else:
    acs = 0
        
col7, col8 = st.columns(2)    
atyp_cp = col7.radio('Atypical Chest Pain',('Yes', 'No'))
if (atyp_cp == 'Yes'):
    acp = 1
else:
    acp = 0  
     

shock = col8.radio('Shock',('Yes', 'No'))
if (shock == 'Yes'):
    sk = 1
else:
    sk = 0    
    
def predict_heart_failure():
    column_names = [['UREA', 'EF', 'GENDER_M', 'TYPE OF ADMISSION-EMERGENCY/OPD_O',
       'PRIOR CMP_1.0', 'RAISED CARDIAC ENZYMES_1.0', 'STABLE ANGINA_1.0',
       'ACS_1.0', 'ATYPICAL CHEST PAIN_1.0', 'SHOCK_1.0']]
    row = [urea,ef,gen,toa,pcmp,rce,sa,acs,acp,sk]
    X = pd.DataFrame([row],columns=column_names)
    prediction = cardio_model.predict(X)
    
    if prediction[0] ==1:
        st.warning('Heart Failure Alert')
    else:
        st.success('No Alert')
        
        

if (st.button('Predict')):
    predict_heart_failure()  
      
    
    
    
