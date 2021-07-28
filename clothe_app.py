import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np 
st.header("Clothe size prediction")
model = pickle.load(open('model.pkl','rb'))
data=[[0,0,0]]

wt = float(st.text_input("Enter the weight"))
age = float(st.text_input("Enter age"))
ht = float(st.text_input("Enter height"))
data[0][0]=wt
data[0][1]=age
data[0][2]=ht
pred = model.predict(data)
key1 = np.round(pred)
key = int(key1)
dict = {1:'XXS', 2:'S', 3:'M',  4:'L', 5:'XL', 6:'XXL', 7:'XXXL'}
  
if key in dict.keys():
    st.write("size =", dict[key])
else:
    st.write("Sizes do not match")
