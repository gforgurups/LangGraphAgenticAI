import streamlit as st
import json
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graphs.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
  ui = LoadStreamlitUI()
  user_input = ui.load_streamlit_ui()

  if not user_input:
    st.error("Error: Failed to load user input from the UI")
    return

  if st.session_state.IsFetchButtonClicked:
    user_message = st.session_state.timeframe
  elif st.session_state.IsSDLC:
    user_message = st.session_state.state
  else:
    user_message = st.chat_input("Enter your message")

  if user_message:
    try:
      llm_class = GroqLLM(user_controls_input=user_input)
      llm_model = llm_class.get_llm_model()

      if not llm_model:
        st.error("Error: LLM model could not be initialized")
        return

      usecase = user_input.get('selected_usecase')
      if not usecase:
        st.error("Error: No usecase is selected")
        return

      ##Graph builder
      try:
        graph_builder = GraphBuilder(llm_model)
        graph = graph_builder.setup_graph(usecase)
        DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
      except Exception as e:
        raise ValueError(f"Exception during Graph initialization: {e}")


    except Exception as e:
      raise ValueError(f"Exception occurred: {e}")

