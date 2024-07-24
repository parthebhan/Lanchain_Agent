# **LangChain Agent**

## Purpose

The Python script demonstrates how to set up a reactive agent using LangChain. This agent uses various tools such as Wikipedia, Arxiv, and a custom web-based retriever to answer specific queries.

## Overview

### Tool Setup Functions

#### Wikipedia Tool Setup (`setup_wikipedia_tool()`)

Initializes an instance of `WikipediaQueryRun` with a `WikipediaAPIWrapper`. This tool allows querying information from Wikipedia.

#### Arxiv Tool Setup (`setup_arxiv_tool()`)

Initializes an instance of `ArxivQueryRun` with an `ArxivAPIWrapper`. This tool allows querying scientific papers from Arxiv.

#### Web-based Retriever Setup (`setup_web_loader_and_faiss()`)

- Loads documents from a specified webpage using `WebBaseLoader`.
- Splits the documents into segments using `RecursiveCharacterTextSplitter`.
- Uses `GoogleGenerativeAIEmbeddings` to create embeddings for each segment.
- Constructs a vector store using `FAISS` to perform efficient similarity searches.

#### Retriever Tool Creation (`create_retriever_tool_instance(retriever)`)

Creates a LangChain retriever tool using `create_retriever_tool`. This tool is configured to search documents loaded from the web.

#### Tool Configuration (`setup_tools()`)

Combines all the above tools (Wikipedia, Arxiv, and the web-based retriever) into a list.

### LangChain Generative AI Setup (`setup_google_generative_ai()`)

Initializes an instance of `GoogleGenerativeAI` with a specified model (`gemini-pro`) and Google API key retrieved from environment variables.

### Agent Setup (`setup_react_agent(llm, tools)`)

- Retrieves a reactive prompt from a specified LangChain repository using `hub.pull()`.
- Creates a LangChain reactive agent using `create_react_agent`, configured with the LangChain generative AI (`llm`) and the list of tools.

### Agent Executor Setup (`setup_agent_executor(agent, tools)`)

Initializes an agent executor using `AgentExecutor`, configured with the reactive agent and the list of tools. Verbose mode is enabled for detailed output.

### Invocation and Result Printing (`main()` function)

- Demonstrates example invocations of the agent executor with specific input queries.
- Prints the results of the queries to standard output.

## Usage

- **Environment Setup**: Ensure the required Python packages (`langchain`, `google.generativeai`, etc.) are installed. Load necessary environment variables (e.g., Google API key) using `dotenv`.
  
- **Execution**: Run the script to initialize the tools, set up the LangChain reactive agent, and invoke it with specific queries.

## Benefits

- **Modularity**: Each function encapsulates a specific setup task (e.g., tool initialization, agent setup), promoting code reusability and maintainability.
  
- **Clarity**: The script uses descriptive function names and comments to enhance understanding of each setup step and their role in constructing the reactive agent.

---

This modular approach ensures that each component of the reactive agent setup can be easily understood, modified, and reused as needed. It also facilitates testing and debugging of individual components independently.



## 🔗 Connect with Me

Feel free to connect with me on LinkedIn:

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://parthebhan143.wixsite.com/datainsights)

[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn_Profile-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parthebhan)

[![Kaggle Profile](https://img.shields.io/badge/Kaggle_Profile-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/parthebhan)

[![Tableau Profile](https://img.shields.io/badge/Tableau_Profile-000?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/parthebhan.pari/vizzes)
