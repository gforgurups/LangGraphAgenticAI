from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
  """
  Chatbot integrated with Tools
  """

  def __init__(self,model,tools):
    self.llm = model
    self.llm_with_tools = self.llm.bind_tools(tools=tools)

  def process(self,state:State)->dict:
    return {"messages": [self.llm_with_tools.invoke(state["messages"])]}
