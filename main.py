import streamlit as st 
import pandas as pd  #1


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
	st.title('Welcome to my awesome data science project')
	st.text('In this project I look into the transactions of taxi in NYC')

with dataset:
	st.header('NYC taxi dataset')
	st.text('I found this data from yahoo.com')
  	
  	#taxi_data = pd.read_csv('data/taxi_data.csv')  #2
  	#distribution_pickup = pd.DataFrame(taxi_data['PULocationID'].value_counts())   #3
  	#st.bar_chart(distribution_pickup)    #4

with features:
	st.header('The features I created')
  	#st.markdown('* **first feature:** this is the explanation')
  	#st.markdown('* **second feature:** another explanation')

with model_training:
    st.header('Model training')
    st.text('In this section you can select the hyperparameters!')

    selection_col, display_col = st.columns(2)

    max_depth = selection_col.slider('What should be the max_depth of the model?',min_value=10,max_value=100,value=20,step=10)

    number_of_trees = selection_col.selectbox('How many trees should there be?',options=[100,200,300,'No limit'],index=0)

    selection_col.text('Here is a list of features: ')
    #selection_col.write(taxi_data.columns)
    input_feature = selection_col.text_input('Which feature would you like to input to the model?','PULocationID')