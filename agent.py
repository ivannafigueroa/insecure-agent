import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langsmith import traceable
from dotenv import load_dotenv

load_dotenv()

# Set up LangSmith tracing (ensure these env vars are set in your environment)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.environ.get("LANGCHAIN_API_KEY", "")

# Use OpenAI API key from environment
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Set up the LLM
llm = ChatOpenAI(
    temperature=0.5,
    openai_api_key=openai_api_key,
    max_tokens=500,
)

# Prompt templates
summarize_prompt = PromptTemplate(
    input_variables=["raw_data"],
    template="""
Here is information about a vendor:

{raw_data}

Summarize the most important services, products, and contacts you find.
""",
)
summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

generate_txt_prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
Based on the following summary, return:
- Full name of the enterprise
- List of services
- Contact information
- Likelihood (0-100%) that this vendor can provide services to a \
  logistics company

Summary:
{summary}
""",
)
generate_txt_chain = LLMChain(llm=llm, prompt=generate_txt_prompt)


# AGENT 1: Scrape
@traceable
def agent_1_scrape(vendor_name):
    from utils import scrape_vendor_info

    return scrape_vendor_info(vendor_name)


# AGENT 2: Summarize
@traceable
def agent_2_summarize(raw_data):
    return summarize_chain.run({"raw_data": raw_data})


# AGENT 3: Generate TXT
@traceable
def agent_3_generate_txt(vendor_name, summarized_data):
    output = generate_txt_chain.run({"summary": summarized_data})
    from utils import save_txt_file

    save_txt_file(vendor_name, output)
    return output
