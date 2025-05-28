# Insecure AI Agent Pipeline

This project aims to demonstrates a deliberately insecure multi-agent workflow that processes vendor information through a series of AI-powered steps.

## Overview

The pipeline consists of three main agents that work in sequence:

1. **Web Scraper Agent**: Takes a vendor name and scrapes public web data
2. **Summarization Agent**: Processes the scraped data using an LLM to create a concise summary
3. **Text Generation Agent**: Creates a final summary file in `.txt` format

## ⚠️ Security Warning

This project is intentionally designed with security vulnerabilities. The following security flaws are deliberately included:

### Agentic AI OWASP Top 10 Vulnerabilities

1. **A01:2023 - Prompt Injection**
   - No sanitization of user input before passing to LLM
   - Direct use of raw user input in prompts

2. **A02:2023 - Insecure Output Handling**
   - Raw model output used directly in file writing operations
   - No validation or sanitization of LLM responses

3. **A03:2023 - Training Data Poisoning**
   - Scraping arbitrary HTML from Google without validation
   - No verification of data source authenticity

4. **A05:2023 - Supply Chain Vulnerabilities**
   - Unvalidated data sources in web scraping
   - No integrity checks on external data

5. **A06:2023 - Sensitive Information Disclosure**
   - Local file creation based on unsanitized user input
   - Potential path traversal vulnerabilities

7. **A07:2023 - Insecure Plugin Design**
   - No sandboxing of agent operations
   - Lack of plugin validation mechanisms

8. **A08:2023 - Excessive Agency**
   - LLM makes decisions with no constraints
   - Unrestricted access to system resources

9. **A09:2023 - Overreliance on LLM**
   - No fallback mechanisms
   - Complete trust in LLM outputs

10. **A10:2023 - Insufficient Logging & Monitoring**
    - Overly permissive OpenAI() wrapper
    - No authentication or logging mechanisms
    - Potential for data leakage through file operations


## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key (required for LLM operations)

## Usage

Run the main script:
```bash
python main.py
```
