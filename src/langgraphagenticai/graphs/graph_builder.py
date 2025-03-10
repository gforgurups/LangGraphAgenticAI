from langgraph.graph import StateGraph, END, MessagesState, START
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
import datetime
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBotNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node

class GraphBuilder:
  def __init__(self,model):
    self.llm = model
    self.graph_builder = StateGraph(State)

  def basic_chatbot_build_graph(self):
    self.basic_chatbot_node = BasicChatBotNode(self.llm)
    self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)

    self.graph_builder.add_edge(START,"chatbot")
    self.graph_builder.add_edge("chatbot", END)

  def chatbot_with_tools_build_graph(self):
    tools = get_tools()
    tool_node = create_tool_node(tools)
    chatbot_tool_node = ChatbotWithToolNode(self.llm,tools)
    self.graph_builder.add_node("chatbot",chatbot_tool_node.process)
    self.graph_builder.add_node("tools",tool_node)

    self.graph_builder.add_edge(START,"chatbot")
    self.graph_builder.add_conditional_edges("chatbot",tools_condition)
    self.graph_builder.add_edge("tools","chatbot")
    self.graph_builder.add_edge("chatbot",END)

  def setup_graph(self, usecase: str):

    if usecase=="Basic Chatbot":
      self.basic_chatbot_build_graph()
    elif usecase=="Chatbot with Tools":
      self.chatbot_with_tools_build_graph()

    return self.graph_builder.compile()
