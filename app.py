import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Heart Disease Prediction App

    On the basis of the given factors this app can predict if you
    have heart disease
""")

st.sidebar.header('User Input Features')

def user_input_features():
    age = st.sidebar.slider('Age', 1, 99, 18)
    sex = st.sidebar.selectbox('Sex',('male','female'))
    if(sex == 'male'):
        sex = 0
    else:
        sex = '1'

    cp = st.sidebar.selectbox('Constrictive pericarditis',('0', '1', '2', '3'))
    trtbps = st.sidebar.slider('TRTBPS', 90, 200,150)
    chol = st.sidebar.slider('Cholestrol', 120,600,250)
    fbs = st.sidebar.selectbox('FBS', ('0', '1'))
    rest_ecg = st.sidebar.selectbox('Rest ECG', ('0', '1', '2'))
    thalachh = st.sidebar.slider('Thal Acch', 50, 250, 100)
    exng = st.sidebar.selectbox('Exchange ', ('0', '1'))
    oldpeak = st.sidebar.slider('Old Peak', 0, 200, 100)
    oldpeak /= 100
    slp = st.sidebar.selectbox('SLP', ('0', '1', '2'))
    caa = st.sidebar.selectbox('CAA', ('0', '1', '2', '3', '4'))
    thall = st.sidebar.selectbox('Thall', ('0', '1', '2', '3'))
    data = {'age': age,
                'sex': sex,
                'cp': cp,
                'trtbps': trtbps,
                'chol': chol,
                'fbs': fbs,
                'restecg': rest_ecg,
                'thalachh': thalachh,
                'exng': exng,
                'oldpeak': oldpeak,
                'slp': slp,
                'caa': caa,
                'thall': thall
                }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()




# Reads in saved classification model
load_clf = pickle.load(open('heardisease.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(input_df)


st.subheader('Prediction')
if(prediction == 0):
    st.write('You do not have health disease')
else:
    st.write('You might have health disease')

