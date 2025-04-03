import pandas as pd
import pickle
import streamlit as st
import numpy as np

model = pickle.load(open(r"c:\Users\Maggie\Desktop\Back acne\TrainedBA_model (1).pkl","rb"))

#main function
def main():
    st.title("Main Page")
    st.write("welcome to the back acne prediction app")
    st.write("""Are you at risk based on your environment and lifestyle?""")
    st.write("This app will help you determine the level of risk of fungal back acne base on your answers")
    st.write("Please answer the following questions")
    #st.write("please answer the following quesions")

    #Side bar for configurations
    st.sidebar.header("More deatils")
    st.sidebar.markdown("[For more facts about fungal back acne here](https://my.clevelandclinic.org/health/diseases/24341-fungal-acne)")
    st.sidebar.markdown("----check for your risk of contancting the infedction----")

    #The UI framework
    Age =st.number_input("Enter your age")
    Gender = st.selectbox("select gender:",["Male","Female"])
    if Gender =="Female":
        Gender = 1
    else:
        Gender = 0
       
    Skin_Type =st.selectbox("select your skin type:",["Oily","Combination","Dry","Oily","Normal"])
    if Skin_Type == "Oily":
        Skin_Type = 3
    elif Skin_Type == "Combination":
        Skin_Type =0
    elif Skin_Type == "Dry":
        Skin_Type =1
    else:
        Skin_Type = 2
    Climate = st.selectbox("select the type of climate in your area:",["Hot-Humid","Mild","Cold-Dry"])
    if Climate == "Hot-Humid":
        Climate = 1
    elif Climate == "Mild":
        Climate =2
    else:
        Climate = 0
    Exercise_Frequency= st.selectbox("How frequent do you exercise:",["4-5-times","2-3-times","1-2-times",
                            "6-7-times","3-4-times","5-6-times","7 times"])
    if Exercise_Frequency == "4-5-times":
        Exercise_Frequency =3
    elif Exercise_Frequency =="2-3-times":
        Exercise_Frequency =1 
    elif Exercise_Frequency == "1-2-times":
        Exercise_Frequency = 0
    elif Exercise_Frequency =="6-7-times":
        Exercise_Frequency =5
    elif Exercise_Frequency == "3-4-times":
        Exercise_Frequency = 2
    elif Exercise_Frequency == "5-6-times":
        Exercise_Frequency = 4
    else:
        Exercise_Frequency = 6

    Sweating_Level= st.selectbox("Select the level of your sweating:",["High","Moderate","Low","Very High"])
    if Sweating_Level == "High":
        Sweating_Level = 0
    elif Sweating_Level =="Moderate":
        Sweating_Level =2
    elif Sweating_Level == "Low":
        Sweating_Level = 1
    else:
        Sweating_Level =3
    Use_of_Tight_Clothing =st.selectbox("Select the tightness of the clothing you wear:",["Yes","No"])
    Use_of_Tight_Clothing=1 if Use_of_Tight_Clothing=="Yes" else 0
    Skin_Care_Routine = st.selectbox("How often and how do you do your skincare routine:",["Minimal","Regular",
                                "Frequent moisturiz","Mild cleansing"])
    if Skin_Care_Routine == "Minimal":
        Skin_Care_Routine = 2
    elif Skin_Care_Routine == "Regular":
        Skin_Care_Routine = 3
    elif Skin_Care_Routine == "Mild cleansing":
        Skin_Care_Routine = 1
    else:
        Skin_Care_Routine = 0
    Hygiene = st.selectbox("Select your frequent hygiene practices:",["no-exfoliation","exfoliate-weekly",
                           "use-hydrating-products","gentle-exfoliation",
                           "use-gentle-soap"])
    if Hygiene == "exfoliate-weekly":
        Hygiene= 0
    elif Hygiene == "use-hydrating-products":
        Hygiene =1
    elif Hygiene ==  "gentle-exfoliation":
        Hygiene =2
    elif Hygiene == "use-gentle-soap":
        Hygiene = 3
    else:
        Hygiene = 4
                           
    Diet = st.selectbox("choose your more frequent die:",["High-sugar-intake","Balanced-Diet","Low-sugar","High-fat-intake",
                     "Mostly-Plant-Based","High-Balanced-diet","Low-Carb","High-sugar-intake","Moderate-Balanced-diet"
                     "High-carb-intake"])
    if Diet == "High-sugar-intake":
        Diet = 4
    elif Diet == "Balanced-Diet":
        Diet = 0
    elif Diet =="Low-sugar":
        Diet = 6
    elif Diet == "High-fat-intake":
        Diet = 3
    elif Diet == "Mostly-Plant-Based":
        Diet =8
    elif Diet == "High-Balanced-diet":
        Diet = 1
    elif Diet == "Low-Carb":
        Diet = 5
    elif Diet == "High-sugar-intake":
        Diet = 4
    elif Diet == "Moderate-Balanced-diet":
        Diet = 7
    else:
        Diet =2
    Recent_Medications = st.selectbox("What medications have you been taking:",["None","Birth Control","Antibiotics for acne"])
    if Recent_Medications == "Birth Control":
        Recent_Medications = 1
    elif Recent_Medications == "Antibiotics for acne":
        Recent_Medications = 0
    else:
        Recent_Medications =2
    History_of_fungal_infections = st.selectbox("Do you have any history of diagnostics fungal infection:",["Yes","No"])
    History_of_fungal_infections = 1 if  History_of_fungal_infections=="Yes" else 0
    Stress_Level = st.selectbox("What is the level of stress you experience:",["Low","High","Medium"])
    if Stress_Level == "Low":
        Stress_Level = 1 
    elif Stress_Level =="High":
        Stress_Level = 0
    else:
        Stress_Level = 2   
       
    #getting and framing data
    data ={'Age':Age, 'Gender':Gender, 'Skin_Type':Skin_Type, 'Climate':Climate, 'Exercise_Frequency':Exercise_Frequency,
       'Sweating Level':Sweating_Level, 'Use_of_Tight_Clothing':Use_of_Tight_Clothing, 'Skin_Care_Routine':Skin_Care_Routine,
       ' Hygiene':Hygiene, 'Diet':Diet, 'Recent_Medications':Recent_Medications,
       'History_of_fungal_infections':History_of_fungal_infections, 'Stress_Level':Stress_Level}
    df = pd.DataFrame(data, index=[0])
    #predicting the result
    return(df)
#call the main dataframe and store the returned datadframe
data = main()

#check if data is None or empty
if data is None or data.empty:
    st.error("Data unavailable for prediction")
else:
    #prediction
    if st.button("predict"):
        #load the model
        try:
            result = model.predict(data)
            proba = model.predict_proba(data)

            #display the result
            if result[0] == 0:
                st.success("SAFE!!! *you are at no risk of cgetting the infection*")
                st.image(r"c:\Users\Maggie\Desktop\Back acne\back image.jpeg")
                st.write("Probability of getting infection: 'NO': {}% 'YES': {}%".format(round((proba[0, 0]) * 100, 2), round((proba[0, 1]) * 100, 2)))
            else:
                st.error("You are at a high risk of getting the infection!!!! *seek medical attention from a dermatologist*")
                st.image(r"c:\Users\Maggie\Desktop\Back acne\fungall.jpeg")
                st.write("Probability of getting infection: 'NO': {}% 'YES': {}%".format(round((proba[0, 0]) * 100, 2), round((proba[0, 1]) * 100, 2)))
        except Exception as e:
            st.error(f"An error occurred during the prediction:{e}")

#predict button and configuration
st.markdown("### **predict button and configuration**")
if st.button("Working"):
            st.write("The button is working")
            st.image(r"c:\Users\Maggie\Desktop\Back acne\malassezia.jpeg")