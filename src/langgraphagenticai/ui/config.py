from configparser import ConfigParser
import os

class Config:
  def __init__(self):
    dir = os.path.abspath(os.getcwd())
    config_file = dir+"/uiconfigfile.ini"
    self.config = ConfigParser()
    self.config.read(config_file)

  def get_llm_option(self):
    return "Groq".split(", ")#self.config["DEFAULT"]["LLM_OPTIONS"].split(", ")

  def get_usecase_option(self):
    return "Basic Chatbot, Chatbot with Tools, Travel Planner, AI News, SDLC Workflow".split(", ") #self.config["DEFAULT"]["USECASE_OPTIONS"].split(", ")

  def get_groq_model_option(self):
    return "mixtral-8x7b-32768, llama3-8b-8192, llama3-70b-8192, gemma-7b-i".split(", ") #self.config["DEFAULT"]["GROQ_MODEL_OPTIONS"].split(", ")

  def get_page_title(self):
    return "LangGraph: Build Stateful Agentic AI graph"#self.config["DEFAULT"]["PAGE_TITLE"]
