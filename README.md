# Shopping List Wizard 🛒

An AI-powered shopping list generator that processes weekly meal menus and creates comprehensive shopping lists.

## Features

- 📄 Upload Word documents (.docx) with weekly meal plans
- 🤖 AI-powered ingredient extraction and categorization
- 🔍 Multi-round validation to catch missing items
- 📊 Smart quantity calculations across multiple meals
- 📥 Download final shopping lists as Word documents
- 🎯 Organized by food categories (meat, dairy, vegetables, etc.)

## How it Works

1. Upload a Word document containing your weekly menu
2. The AI analyzes the menu and generates an initial shopping list
3. Multiple AI evaluators check for missing or incorrect items
4. Errors are automatically identified and corrected
5. Download your final, comprehensive shopping list

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add: `OPENAI_API_KEY=your-api-key-here`

3. Run the app:
   ```bash
   streamlit run grocery.py
   ```

## Deployment

This app is designed to be deployed on Streamlit Cloud. Make sure to set the `OPENAI_API_KEY` environment variable in your deployment settings.

## Requirements

- Python 3.8+
- OpenAI API key
- Word documents (.docx) with weekly meal plans
