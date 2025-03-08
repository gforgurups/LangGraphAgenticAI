from src.langgraphagenticai.state.state import State

class BasicChatBotNode:

  def __init__(self,model):
    self.llm = model

  def process(self,state:State)->dict:
    return {"messages": self.llm.invoke(state['messages'])}
