import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
  def __init__(self,user_controls_input):
    self.user_controls_input = user_controls_input

  def get_llm_model(self):
    try:
      groq_api_key =  self.user_controls_input['GROQ_API_KEY']

      if groq_api_key=='' and os.environ['GROQ_API_KEY'] =='':
        st.error("Please enter Groq API Key")
      selected_groq_model = self.user_controls_input['selected_groq_model']
      llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

    except Exception as e:
      return ValueError(f"Error occurred :{e}")
    return llm

