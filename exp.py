from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_google_genai import GoogleGenerativeAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def setup_wikipedia_tool():
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    return WikipediaQueryRun(api_wrapper=api_wrapper)

def setup_web_loader_and_faiss():
    webpage = "https://docs.smith.langchain.com/"
    loader = WebBaseLoader(webpage)
    docs = loader.load()
    documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))
    vectordb = FAISS.from_documents(documents, embeddings)
    retriever = vectordb.as_retriever()
    return retriever

def setup_arxiv_tool():
    api_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    return ArxivQueryRun(api_wrapper=api_wrapper)

def create_retriever_tool_instance(retriever):
    return create_retriever_tool(retriever, "Web_based_search",
                                 "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!")

def setup_tools():
    wikipedia_tool = setup_wikipedia_tool()
    arxiv_tool = setup_arxiv_tool()
    retriever = setup_web_loader_and_faiss()
    retriever_tool = create_retriever_tool_instance(retriever)
    return [wikipedia_tool, arxiv_tool, retriever_tool]

def setup_google_generative_ai():
    return GoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))

def setup_react_agent(llm, tools):
    prompt = hub.pull("hwchase17/react")
    return create_react_agent(llm=llm, tools=tools, prompt=prompt)

def setup_agent_executor(agent, tools):
    return AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    tools = setup_tools()
    llm = setup_google_generative_ai()
    agent = setup_react_agent(llm, tools)
    agent_executor = setup_agent_executor(agent, tools)

    # Example invocations
    #result1 = agent_executor.invoke({"input": "what is the Spirit of the Game in cricket"})
    result2 = agent_executor.invoke({"input": "Tell me about Langsmith"})
    # result3 = agent_executor.invoke({"input": "What's the paper 1605.08386 about?"})

    # Print results
    #print(result1)
    print(result2)
    # print(result3)

if __name__ == "__main__":
    main()
