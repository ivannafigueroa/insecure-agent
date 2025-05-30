import re
import sys
from agent import agent_1_scrape, agent_2_summarize, agent_3_generate_txt


def main():
    vendor_name_input = input("Enter vendor name: ")
    # Sanitize vendor_name to prevent prompt injection
    vendor_name = re.sub(r"[^a-zA-Z0-9 -]", "", vendor_name_input)

    if not vendor_name.strip():
        print("Error: Vendor name is empty after sanitization. Exiting.")
        sys.exit(1)
    # ⚠️ Prompt injection risk - User input is sent directly to agents without
    # sanitization. - This warning refers to the original input, but we use the sanitized one.

    raw_data = agent_1_scrape(vendor_name)
    if raw_data is None:
        print("Error: Failed to scrape data. Exiting.")
        sys.exit(1)

    summarized = agent_2_summarize(raw_data)
    if summarized is None:
        print("Error: Failed to summarize data. Exiting.")
        sys.exit(1)

    final_output = agent_3_generate_txt(vendor_name, summarized)
    if final_output is None:
        print("Error: Failed to generate final text. Exiting.")
        sys.exit(1)

    print("\n=== Final Summary File Created ===")
    print(final_output)


if __name__ == "__main__":
    main()
