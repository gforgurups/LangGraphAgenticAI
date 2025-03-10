from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun

def get_tools():
  """
  Return the list of tools to be used in the chatbot
  """

    #Wiki tool
  wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
  wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

  ## Work with external tools
  #tools=[TavilySearchResults(max_results=2)]
  tools=[wiki_tool]
  return tools

def create_tool_node(tools):
  """
  creates and returns a tool node for the graph
  """
  return ToolNode(tools=tools)
