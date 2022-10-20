# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 23:44:50 2022

@author: 60112
"""

import streamlit as st
def get_mood():
    dic = {'Select your mood here':0, 'Fatigued':1,'Sleepy':2,'Hungry':3,'Angry':4,'Lonely':5,'Sad':6,'Happy':7,'Bored':8,\
      'Overweight':9,'Underweight':9,'High Glucose':11,'Headache':12}
    feel = []
    for i in dic.keys():
        feel.append(i)
    return feel,dic

def process_mood(mood):
    
    _,di=get_mood()
    return di[mood]


#mood_list,_=get_mood()
#st.selectbox("Select Your mood today", ['a','b'])
#mood=st.radio("How are you feeling today?", mood_list)
#st.write(process_mood(mood))

selected = st.selectbox('Select one option:', ['', 'First one', 'Second one'], format_func=lambda x: 'Select an option' if x == '' else x)

#if selected:
 #   st.success('Yay! 🎉')
#else:
 #   st.warning('No option is selected')