import streamlit as st
import pickle
import pandas as pd

# Function to load the trained random forest model
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Load your trained random forest model
model_path = 'RandomForest_Model.pkl'
model = load_model(model_path)

# Define sidebar title
st.sidebar.title('Transaction Information')

# Define HTML template
html_temp = """
<div style="background-color: Green; padding:10px">
<h2 style="color: white; text-align:center;">Credit Card Fraud Detection</h2>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)

# Define slider inputs for features
v2 = st.sidebar.slider(label="V2", min_value=-72.00, max_value=22.00, step=0.01)
v3 = st.sidebar.slider(label="V3", min_value=-48.00, max_value=9.00, step=0.01)
v4 = st.sidebar.slider(label="V4", min_value=-5.00, max_value=16.00, step=0.01)
v9 = st.sidebar.slider(label="V9", min_value=-13.00, max_value=15.00, step=0.01)
v10 = st.sidebar.slider(label="V10", min_value=-24.00, max_value=23.00, step=0.01)
v11 = st.sidebar.slider(label="V11", min_value=-4.00, max_value=15.00, step=0.01)
v12 = st.sidebar.slider(label="V12", min_value=-18.00, max_value=7.00, step=0.01)
v14 = st.sidebar.slider(label="V14", min_value=-19.00, max_value=10.00, step=0.01)
v16 = st.sidebar.slider(label="V16", min_value=-14.00, max_value=17.00, step=0.01)
v17 = st.sidebar.slider(label="V17", min_value=-25.00, max_value=10.00, step=0.01)

# Create a dictionary of user inputs
coll_dict = {'V2': v2, 'V3': v3, 'V4': v4, 'V9': v9, 'V10': v10, 
             'V11': v11, 'V12': v12, 'V14': v14, 'V16': v16, 'V17': v17}

# Create a DataFrame from the dictionary
df_coll = pd.DataFrame.from_dict([coll_dict])

# Display user inputs
st.subheader('Transaction Information')
st.table(df_coll)

# Make prediction when 'PREDICT' button is clicked
# Make prediction when 'PREDICT' button is clicked
if st.button('Predict'):
    # Make prediction using the loaded model if it was loaded successfully
    if model is not None:
        st.write("Attempting to make predictions with the model...")
        try:
            prediction = model.predict(df_coll)
            st.write("Prediction:", prediction)
            if prediction[0] == 0:
                st.success('Transaction is Legitimate :)')
            elif prediction[0] == 1:
                st.warning('ALARM! Transaction is FRAUDULENT :(')
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Model was not loaded successfully. Please check the model file.")
