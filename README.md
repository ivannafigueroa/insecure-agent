# Insecure AI Agent Pipeline

This project aims to demonstrates a deliberately insecure multi-agent workflow that processes vendor information through a series of AI-powered steps.

## Overview

The pipeline consists of three main agents that work in sequence:

1. **Web Scraper Agent**: Takes a vendor name and scrapes public web data
2. **Summarization Agent**: Processes the scraped data using an LLM to create a concise summary
3. **Text Generation Agent**: Creates a final summary file in `.txt` format

## ⚠️ Security Warning

This project is intentionally designed with security vulnerabilities. The following security flaws are deliberately included:

### Based on some of the OWASP Top 10 risks for LLM applications

**Prompt Injection**
   - No sanitization of user input before passing to LLM
   - Direct use of raw user input in prompts

**Insecure Output Handling**
   - Raw model output used directly in file writing operations
   - No validation or sanitization of LLM responses

**Training Data Poisoning**
   - Scraping arbitrary HTML from Google without validation
   - No verification of data source authenticity

**Insecure Plugin and Supply Chain Integrations**
   - Unvalidated data sources in web scraping
   - No integrity checks on external data

**Sensitive Information Disclosure**
   - LLMs may expose PII, credentials, or internal system details due to training data, prompts, or lack of redaction.
   - Potential path traversal vulnerabilities

**Excessive Agency**
   - LLM makes decisions with no constraints
   - Unrestricted access to system resources

**Overreliance on LLM**
   - No fallback mechanisms
   - Complete trust in LLM outputs


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
