# #########################################################  FIRST TRIAL ################################################################


# from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
# import requests
# from bs4 import BeautifulSoup
# from groq import Groq
# from dotenv import load_dotenv
# import os

# # Load the .env file
# load_dotenv()

# # Retrieve the API key from the environment variable
# api_key = os.getenv('GROQ_API_KEY')

# # Initialize the client with the API key
# client = Groq(api_key=api_key)

# # Initialize the DuckDuckGoSearchAPIWrapper
# ddg_search = DuckDuckGoSearchAPIWrapper()

# # Set the number of results per query
# RESULTS_PER_QUESTION = 3

# # Function to perform web search
# def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):
#     """
#     Performs a search query using DuckDuckGo and returns a list of URLs.
#     """
#     try:
#         results = ddg_search.results(query, num_results)
#         return [result["link"] for result in results]
#     except Exception as e:
#         print(f"Error during search: {e}")
#         return []

# # Function to scrape content from a URL
# def scrape_text(url: str):
#     """
#     Fetches the content from a given URL and returns the parsed text.
#     """
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Check if the request was successful
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Extract main content from the page (customizable as needed)
#         paragraphs = soup.find_all('p')
#         page_content = "\n".join([p.get_text() for p in paragraphs])

#         return page_content
#     except Exception as e:
#         return f"Failed to fetch content from {url}: {e}"

# # Function to fetch and process multiple URLs
# def fetch_and_process_results(query: str):
#     """
#     Searches the web using the query, scrapes content from each result,
#     and returns a structured list of the results and their content.
#     """
#     # Step 1: Perform the web search
#     urls = web_search(query)

#     if not urls:
#         return "No results found or an error occurred during the search."

#     results_data = []
    
#     # Step 2: Scrape content for each URL
#     for idx, url in enumerate(urls, 1):
#         print(f"\nFetching content from: {url}")
#         content = scrape_text(url)

#         # Step 3: Append the result to a structured list
#         results_data.append({
#             "url": url,
#             "content": content[:10000],  # Limit the content to first 10000 characters for brevity
#         })
    
#     return results_data

# # Function to display the results
# def display_results(results_data):
#     """
#     Nicely prints the scraped content for each result.
#     """
#     if isinstance(results_data, str):
#         print(results_data)  # Error message or no results
#         return
    
#     for idx, result in enumerate(results_data, 1):
#         print(f"\nResult {idx}:")
#         print(f"URL: {result['url']}")
#         print(f"Content:\n{result['content']}")
#         print("-" * 50)

# # Function to generate completion using Groq
# def generate_research_summary(query):
#     """
#     Generates a research summary using the Groq API.
#     """
#     completion = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a research assistant that helps students with project work. You provide detailed research, summaries, and properly formatted citations."
#             },
#             {
#                 "role": "user",
#                 "content": f"Can you help me gather materials on {query} for my project?"
#             },
#             {
#                 "role": "assistant",
#                 "content": "Sure! Here are some up-to-date sources and research papers on the topic. I'll also include in-text citations and references in APA format."
#             }
#         ],
#         temperature=1,
#         max_tokens=1024,
#         top_p=1,
#         stream=True,
#         stop=None,
#     )

#     # Collect and print the response from the Groq API
#     print("\nGenerated Research Summary:")
#     for chunk in completion:
#         print(chunk.choices[0].delta.content or "", end="")

# # Example usage: Searching for Python programming tutorials
# query = "climate change"
# results = fetch_and_process_results(query)
# display_results(results)

# # Generate a research summary using Groq
# generate_research_summary(query)



# #########################################################  SECOND TRIAL ################################################################



# from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
# import requests
# from bs4 import BeautifulSoup
# from groq import Groq
# from dotenv import load_dotenv
# import os

# # Load the .env file
# load_dotenv()

# # Retrieve the API key from the environment variable
# api_key = os.getenv('GROQ_API_KEY')

# # Initialize the client with the API key
# client = Groq(api_key=api_key)

# # Initialize the DuckDuckGoSearchAPIWrapper
# ddg_search = DuckDuckGoSearchAPIWrapper()

# # Set the number of results per query
# RESULTS_PER_QUESTION = 3

# # Function to perform web search
# def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):
#     try:
#         results = ddg_search.results(query, num_results)
#         return [result["link"] for result in results]
#     except Exception as e:
#         return []

# # Function to scrape content from a URL
# def scrape_text(url: str):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Check if the request was successful
#         soup = BeautifulSoup(response.content, 'html.parser')
#         paragraphs = soup.find_all('p')
#         page_content = "\n".join([p.get_text() for p in paragraphs])
#         return page_content
#     except Exception as e:
#         return ""

# # Function to fetch and process multiple URLs
# def fetch_and_process_results(query: str):
#     urls = web_search(query)
#     if not urls:
#         return []

#     results_data = []
#     for url in urls:
#         content = scrape_text(url)
#         results_data.append({
#             "url": url,
#             "content": content[:10000],  # Limit the content to first 10000 characters
#         })
#     return results_data

# # Function to generate completion using Groq
# def generate_research_summary(query):
#     completion = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a research assistant that helps students with project work. You provide detailed research, summaries, and properly formatted citations."
#             },
#             {
#                 "role": "user",
#                 "content": f"Can you help me gather materials on {query} for my project?"
#             },
#             {
#                 "role": "assistant",
#                 "content": "Sure! Here are some up-to-date sources and research papers on the topic. I'll also include in-text citations and references in APA format."
#             }
#         ],
#         temperature=1,
#         max_tokens=1024,
#         top_p=1,
#         stream=True,
#         stop=None,
#     )

#     print("\nGenerated Research Summary:")
#     for chunk in completion:
#         print(chunk.choices[0].delta.content or "", end="")

# # Example usage: Searching for climate change
# query = "climate change"
# results = fetch_and_process_results(query)
# generate_research_summary(query)


# ***************************************************************** SECOND TRIAL 2 ***********************************************************

from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
import requests
from bs4 import BeautifulSoup
from groq import Groq
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv('GROQ_API_KEY')

# Initialize the client with the API key
client = Groq(api_key=api_key)

# Initialize the DuckDuckGoSearchAPIWrapper
ddg_search = DuckDuckGoSearchAPIWrapper()

# Set the number of results per query
RESULTS_PER_QUESTION = 3

# Function to perform web search
def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):
    try:
        results = ddg_search.results(query, num_results)
        return [result["link"] for result in results]
    except Exception as e:
        return []

# Function to scrape content from a URL
def scrape_text(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        page_content = "\n".join([p.get_text() for p in paragraphs])
        return page_content
    except Exception as e:
        return ""

# Function to fetch and process multiple URLs
def fetch_and_process_results(query: str):
    urls = web_search(query)
    if not urls:
        return []

    results_data = []
    for url in urls:
        content = scrape_text(url)
        results_data.append({
            "url": url,
            "content": content[:10000],  # Limit the content to first 10000 characters
        })
    return results_data

# Function to generate completion using Groq
def generate_research_summary(query):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a research assistant that helps students with project work. You provide detailed research, summaries, and properly formatted citations."
            },
            {
                "role": "user",
                "content": f"Can you help me gather materials on {query} for my project?"
            },
            {
                "role": "assistant",
                "content": "Sure! Here are some up-to-date sources and research papers on the topic. I'll also include in-text citations and references in APA format."
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    print("\nGenerated Research Summary:")
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")

# Example usage: Searching for climate change
query = "climate change"
results = fetch_and_process_results(query)
generate_research_summary(query)


# #########################################################  THIRD TRIAL ################################################################


# from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
# import requests
# from bs4 import BeautifulSoup
# from groq import Groq
# from dotenv import load_dotenv
# import os

# # Load the .env file
# load_dotenv()

# # Retrieve the API key from the environment variable
# api_key = os.getenv('GROQ_API_KEY')

# # Initialize the client with the API key
# client = Groq(api_key=api_key)

# # Initialize the DuckDuckGoSearchAPIWrapper
# ddg_search = DuckDuckGoSearchAPIWrapper()

# # Set the number of results per query
# RESULTS_PER_QUESTION = 3

# # Function to perform web search
# def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):
#     try:
#         results = ddg_search.results(query, num_results)
#         return [result["link"] for result in results]
#     except Exception as e:
#         return []

# # Function to scrape content from a URL
# def scrape_text(url: str):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Check if the request was successful
#         soup = BeautifulSoup(response.content, 'html.parser')
#         paragraphs = soup.find_all('p')
#         page_content = "\n".join([p.get_text() for p in paragraphs])
#         return page_content
#     except Exception as e:
#         return ""

# # Function to fetch and process multiple URLs
# def fetch_and_process_results(query: str):
#     urls = web_search(query)
#     if not urls:
#         return []

#     results_data = []
#     for url in urls:
#         content = scrape_text(url)
#         results_data.append({
#             "url": url,
#             "content": content[:10000],  # Limit the content to first 10000 characters
#         })
#     return results_data

# # Function to generate completion using Groq
# def generate_research_summary(query):
#     completion = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a research assistant that helps students with project work. You provide detailed research, summaries, and properly formatted citations."
#             },
#             {
#                 "role": "user",
#                 "content": f"Can you help me gather materials on {query} for my project?,Please generate a structured research summary on '{query}' formatted in Markdown with chapters and sections, similar to this example:\n\n"
#                            ":CHAPTER ONE: INTRODUCTION\n"
#                            "1.1 Background of the Study\n"
#                            "1.2 Statement of Problem\n"
#                            "1.3 Aim and Objectives of the Study\n"
#                            "1.4 Significance of the Study\n"
#                            "1.5 Scope of the Study\n"
#                            "CHAPTER TWO: LITERATURE REVIEW\n"
#                            "2.1 Key Concepts\n"
#                            "2.2 Current Trends\n"
#                            "2.3 Research Gaps\n"
#                            "CHAPTER THREE: METHODOLOGY\n"
#                            "3.1 Data Collection\n"
#                            "3.2 Data Analysis\n"
#                            "CHAPTER FOUR: RESULTS\n"
#                            "4.1 Findings\n"
#                            "4.2 Discussion\n"
#                            "CHAPTER FIVE: CONCLUSION\n"
#                            "Conclusion\n"
#                            "Recommendations"
#             }
#         ],
#         temperature=1,
#         max_tokens=1024,
#         top_p=1,
#         stream=True,
#         stop=None,
#     )

#     print("\nGenerated Research Summary:")
#     for chunk in completion:
#         print(chunk.choices[0].delta.content or "", end="")

# # Example usage: Searching for climate change
# query = "climate change"
# results = fetch_and_process_results(query)
# generate_research_summary(query)


# #########################################################  FOURTH TRIAL ################################################################
# from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
# import requests
# from bs4 import BeautifulSoup
# from groq import Groq
# from dotenv import load_dotenv
# import os

# # Load the .env file
# load_dotenv()

# # Retrieve the API key from the environment variable
# api_key = os.getenv('GROQ_API_KEY')

# # Initialize the client with the API key
# client = Groq(api_key=api_key)

# # Initialize the DuckDuckGoSearchAPIWrapper
# ddg_search = DuckDuckGoSearchAPIWrapper()

# # Set the number of results per query
# RESULTS_PER_QUESTION = 3

# # Function to perform web search
# def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):
#     try:
#         results = ddg_search.results(query, num_results)
#         return [result["link"] for result in results]
#     except Exception as e:
#         return []

# # Function to scrape content from a URL
# def scrape_text(url: str):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Check if the request was successful
#         soup = BeautifulSoup(response.content, 'html.parser')
#         paragraphs = soup.find_all('p')
#         page_content = "\n".join([p.get_text() for p in paragraphs])
#         return page_content
#     except Exception as e:
#         return ""

# # Function to fetch and process multiple URLs
# def fetch_and_process_results(query: str):
#     urls = web_search(query)
#     if not urls:
#         return []

#     results_data = []
#     for url in urls:
#         content = scrape_text(url)
#         results_data.append({
#             "url": url,
#             "content": content[:10000],  # Limit the content to first 10000 characters
#         })
#     return results_data

# # Function to generate detailed markdown output
# def generate_research_summary(query):
#     completion = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a research assistant that helps students with project work. Your task is to create a detailed markdown project research paper report based on the user's query."
#             },
#             {
#                 "role": "user",
#                 "content": (
#                     f"Can you help me gather materials on {query} for my project? "
#                     "Please provide a structured markdown output with sections including: "
#                     "CHAPTER ONE: INTRODUCTION, 1.1 Background of the Study, Summarize  in 300 words,"
#                     "1.2 Statement of Problem, 1.3 Aim and Objectives of the Study,Summarize  in 300 words, "
#                     "1.4 Significance of the Study, 1.5 Scope of the Study,Summarize  in 300 words, "
#                     "CHAPTER TWO: LITERATURE REVIEW, 2.1 Relevant Topic,Summarize  in 300 words, "
#                     "2.2 Mode of Action, 2.3 Benefits, 2.4 Safety, Summarize  in 300 words,"
#                     "2.5 Effects on the Environment, CHAPTER THREE: MATERIALS AND METHODS, "
#                     "3.1 Study Location, 3.2 Animal Care and Management,Summarize  in 300 words, "
#                     "3.3 Chemicals, CHAPTER FOUR: RESULTS, CHAPTER FIVE: DISCUSSION. "
#                     "Each section should have more than 300 words."
#                 )
#             },
#             {
#                 "role": "assistant",
#                 "content": "Sure! I'll provide a detailed markdown report based on your request."
#             }
#         ],
#         temperature=1,
#         max_tokens=2048,  # Increased limit for longer sections
#         top_p=1,
#         stream=False,  # Set to False for complete output at once
#         stop=None,
#     )

#     print("\nGenerated Research Summary:\n")
#     for chunk in completion.choices:
#         print(chunk.message.content)

# # Example usage: Searching for climate change
# query = "climate change"
# results = fetch_and_process_results(query)
# generate_research_summary(query)
