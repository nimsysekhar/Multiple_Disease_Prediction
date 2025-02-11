import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# loading the saved models
kidney_model = pickle.load(open("kidney_disease_prediction.pkl",'rb'))

liver_model = pickle.load(open("liver_disease_prediction.pkl",'rb'))

parkinson_model = pickle.load(open("parkinson_prediction.pkl",'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Kidney disease Prediction',
                           'Liver Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

if (selected == 'Kidney disease Prediction'):

    st.title("🩸 Kidney Disease Prediction")

    # Input fields for Kidney Disease prediction
    st.write("Please enter the following details:")
    feature1 = st.number_input("age")
    feature2 = st.number_input("bp")
    feature3 = st.number_input("sg")
    feature4 = st.number_input("al")
    feature5 = st.number_input("su")
    feature6 = st.number_input("rbc")
    feature7 = st.number_input("pc")
    feature8 = st.number_input("pcc")
    feature9 = st.number_input("ba")
    feature10 = st.number_input("bgr")
    feature11 = st.number_input("bu")
    feature12 = st.number_input("sc")
    feature13 = st.number_input("pot")
    feature14 = st.number_input("wc")
    feature15 = st.number_input("rc")
    feature16 = st.number_input("htn")
    feature17 = st.number_input("dm")
    feature18 = st.number_input("cad")
    feature19 = st.number_input("appet")
    feature20 = st.number_input("pe")
    feature21 = st.number_input("ane")
# Add more features as needed

    if st.button("Predict"):
        input_data = np.array([[feature1, feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,
                                feature12,feature13,feature14,feature15,feature16,feature17,feature18,feature19,feature20,feature21]])
        prediction = kidney_model.predict(input_data)
        
        if prediction[0] == 1:
            st.error("The model predicts that the patient has Kidney disease.")
        else:
            st.success("The model predicts that the patient does not have Kidney disease.")

if (selected == 'Liver Disease Prediction'):
    st.title("🍷 Liver Disease Prediction")

    # Input fields for Liver Disease prediction
    st.write("Please enter the following details:")
    feature1 = st.number_input("Age")
    feature2 = st.number_input("Gender")
    feature3 = st.number_input("Total_Bilirubin")
    feature4 = st.number_input("Direct_Bilirubinl")
    feature5 = st.number_input("Alkaline_Phosphotase")
    feature6 = st.number_input("Alamine_Aminotransferase")
    feature7 = st.number_input("Aspartate_Aminotransferase")
    feature8 = st.number_input("Total_Protiens")
    feature9 = st.number_input("Albumin")
    feature10 = st.number_input("Albumin_and_Globulin_Ratio")
    # Add more features as needed

    if st.button("Predict"):
        input_data = np.array([[feature1, feature2,feature3,feature4,feature5,feature6,feature7,feature8,
                                feature9,feature10]])  
        prediction = liver_model.predict(input_data)
        
        if prediction[0] == 1:
            st.error("The model predicts that the patient has Liver disease.")
        else:
            st.success("The model predicts that the patient does not have Liver disease.")

if (selected == 'Parkinsons Prediction'):
    st.title("🧠 Parkinson's Disease Prediction")

    st.write("Please enter the following details:")
    feature1 = st.number_input("MDVP:Fo(Hz)")
    feature2 = st.number_input("MDVP:Fhi(Hz)")
    feature3 = st.number_input("MDVP:Flo(Hz)")
    feature4 = st.number_input("MDVP:Jitter(%)")
    feature5 = st.number_input("MDVP:Jitter(Abs)")
    feature6 = st.number_input("MDVP:RAP")
    feature7 = st.number_input("MDVP:PPQ")
    feature8 = st.number_input("Jitter:DDP")
    feature9 = st.number_input("MDVP:Shimmer")
    feature10 = st.number_input("MDVP:Shimmer(dB)")
    feature11 = st.number_input("Shimmer:APQ3")
    feature12 = st.number_input("Shimmer:APQ5")
    feature13 = st.number_input("MDVP:APQ")
    feature14 = st.number_input("Shimmer:DDA")
    feature15 = st.number_input("NHR")
    feature16 = st.number_input("HNR")
    feature17 = st.number_input("RPDE")
    feature18 = st.number_input("DFA")
    feature19 = st.number_input("spread1")
    feature20 = st.number_input("spread2")
    feature21 = st.number_input("D2")
    feature22 = st.number_input("PPE")

    if st.button("Predict"):
        input_data = np.array([[feature1, feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11,feature12,feature13,feature14,feature15,feature16,
                                feature17,feature18,feature19,feature20,
                                feature21,feature22]])  
        prediction = parkinson_model.predict(input_data)
        
        if prediction[0] == 1:
            st.error("The model predicts that the patient has Parkinson's disease.")
        else:
            st.success("The model predicts that the patient does not have Parkinson's disease.")