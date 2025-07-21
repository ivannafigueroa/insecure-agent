from agent import agent_1_scrape, agent_2_summarize, agent_3_generate_txt


def main():
    vendor_name = input("Enter vendor name: ")
    # ⚠️ Prompt injection risk - User input is sent directly to agents without
    # sanitization.

    raw_data = agent_1_scrape(vendor_name)
    summarized = agent_2_summarize(raw_data)
    final_output = agent_3_generate_txt(vendor_name, summarized)

    print("\n=== Final Summary File Created ===")
    print(final_output)


if __name__ == "__main__":
    main()
