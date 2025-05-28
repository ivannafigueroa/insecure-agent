from langchain.llms import OpenAI
import os

# ⚠️ Hardcoded API key, proper environment variable should be used
OPENAI_API_KEY = os.getenv("key...")
llm = OpenAI(
    temperature=0.5,
    openai_api_key=OPENAI_API_KEY,
    max_tokens=500,
)


def agent_1_scrape(vendor_name):
    from utils import scrape_vendor_info

    return scrape_vendor_info(vendor_name)


def agent_2_summarize(raw_data):
    # ⚠️ Prompt includes raw data retrieved from agent_1_scrape
    # OWASP A01: Prompt Injection
    # OWASP A03: Training Data Poisoning - Agent scrapes untrusted sites
    prompt = (
        f"Here is information about a vendor:\n\n{raw_data}\n\n"
        "Summarize the most important services, products, and contacts you "
        "find."
    )
    return llm(prompt)


def agent_3_generate_txt(vendor_name, summarized_data):
    # ⚠️ LLM is trusted to make business decisions autonomously
    # OWASP A08: Excessive Agency
    # Agents autonomously decide what to scrape/save
    prompt = (
        f"Based on the following summary, return:\n"
        "- Full name of the enterprise\n"
        "- List of services\n"
        "- Contact information\n"
        "- Likelihood (0-100%) that this vendor can provide services to a "
        "logistics company\n\n"
        f"Summary:\n{summarized_data}"
    )
    output = llm(prompt)

    # ⚠️ Missing Rate Limiting. There's no rate limiting on the LLM calls
    # ⚠️ This could lead to abuse and excessive API costs

    # ⚠️ Output is saved without validation
    # OWASP A02: Insecure Output Handling - Model-generated output is trusted
    # blindly.
    from utils import save_txt_file

    save_txt_file(vendor_name, output)
    return output


# Missing Rate Limiting. There's no rate limiting on the LLM calls
# This could lead to abuse and excessive API costs
