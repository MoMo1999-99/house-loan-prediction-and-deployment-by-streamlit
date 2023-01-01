import streamlit as st
import joblib 
import pandas as pd
import numpy as np



Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")



def predict(Gender, Married,Dependents, Education, Self_Employed,
       Credit_History, Property_Area, TotalIncome, amountpermonth,
       remainFromPaying):
    df.at[0,"Gender"] = Gender
    df.at[0,"Married"] = Married
    df.at[0,"Dependents"] = Dependents
    df.at[0,"Education"] = Education
    df.at[0,"Self_Employed"] = Self_Employed
    df.at[0,"Credit_History"] = Credit_History
    df.at[0,"amountpermonth"] = amountpermonth
    df.at[0,"TotalIncome"] = TotalIncome
    df.at[0,"Property_Area"] = Property_Area
    df.at[0,"remainFromPaying"] = remainFromPaying
    result = model.predict(df)[0]
    return result
    
def main():
    st.title("loan prediction")
    Gender = st.selectbox("Gender" , ['Male', 'Female'])
    Married = st.selectbox("Married" , ['No', 'Yes'])
    Dependents = st.selectbox("Dependents" , [ 0,  1,  2,  3])
    Education = st.selectbox("Education" , ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox("Self_Employed" , ['No', 'Yes'])
    ApplicantIncome = st.number_input("Enter Your Income")
    CoapplicantIncome = st.number_input("Enter Your CoapplicantIncome")
    Credit_History = st.number_input("Enter Your Credit_History")
    Property_Area = st.selectbox("Property_Area" , ['Urban', 'Rural', 'Semiurban'])
    TotalIncome = ApplicantIncome + CoapplicantIncome
    LoanAmount = st.slider("LoanAmount" , min_value=0.0 , max_value=700.0 , step = 5.0 , value = 200.0)
    Loan_Amount_Term = st.slider("Loan_Amount_Term" , min_value=0.0 , max_value=480.0 , step = 5.0 , value = 200.0)

    
    amountpermonth = LoanAmount * 1000 / Loan_Amount_Term
    remainFromPaying = TotalIncome - amountpermonth
    
    
    TotalIncome = np.log(TotalIncome)
    amountpermonth = np.log(amountpermonth)
    remainFromPaying = np.log(remainFromPaying)
    
    
    if st.button("Predict"):
        result = predict(Gender, Married,Dependents, Education, Self_Employed,Credit_History, Property_Area, TotalIncome, amountpermonth,remainFromPaying)
        list_res = ["Rejected" , "Accepted"]
        st.text(f"Your Loan is {list_res[result]}")

        
        
if __name__ == '__main__':
    main()
