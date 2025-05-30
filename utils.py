import requests
from bs4 import BeautifulSoup
import re
import html


def scrape_vendor_info(vendor_name):
    # Sanitize vendor_name to allow only alphanumeric characters, spaces, and hyphens
    original_vendor_name = vendor_name # Keep original for query if needed, or use sanitized one
    vendor_name = re.sub(r"[^a-zA-Z0-9 -]", "", vendor_name)

    if not vendor_name.strip():
        print("Error: Vendor name is empty after sanitization.")
        return ""

    # ⚠️ The vendor_name parameter isn't validated or sanitized before being
    # used in both functions - This warning seems to refer to the input `vendor_name`
    # but we are sanitizing it right above. The query uses the sanitized version.
    query = vendor_name.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        soup = BeautifulSoup(res.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Error during web scraping for '{vendor_name}': {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred during web scraping for '{vendor_name}': {e}")
        return ""

    # ⚠️ Return raw text from top 5 search result.
    # Raw HTML content is being processed without proper sanitization.
    # The code takes HTML content from Google search results and directly
    # extracts text from <span> elements.
    # If any of the search results contain malicious JavaScript or HTML, it
    # could be executed when the content is later displayed.
    # The code doesn't validate or sanitize the HTML content before
    # processing it

    snippets = soup.find_all("span")
    return " ".join([html.escape(s.text) for s in snippets[:50]])


def save_txt_file(vendor_name, content):
    # ⚠️ The vendor name is used directly in the filename without any
    # sanitization.
    # This could lead to directory traversal attacks by using ../ in the
    # vendor name

    # Sanitize vendor_name for filename
    safe_vendor_name = re.sub(r"[^a-zA-Z0-9 -]", "", vendor_name)
    if not safe_vendor_name.strip():
        safe_vendor_name = "default_vendor"
        print(f"Warning: Original vendor name was empty or invalid after sanitization. Using '{safe_vendor_name}'.")

    file_name = f"{safe_vendor_name}_summary.txt"
    try:
        with open(file_name, "w") as f:
            f.write(content)
        print(f"Successfully saved summary to {file_name}")
    except Exception as e:
        print(f"Error saving file {file_name}: {e}")
