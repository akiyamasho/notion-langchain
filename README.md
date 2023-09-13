# Notion LangChain

### Requirements

-   OpenAI API Key ([retrieve here](https://platform.openai.com/account/billing))
-   Notion Integration + API Key ([setup here](https://www.notion.so/my-integrations))
-   Pages in Notion shared with Notion Integration
-   Docker

### Setup

1. Install the requirements
   ```bash
   pip install requirements.txt
   ```
1. Create a `.env` file with your OpenAI API Key and Notion Integration API Key:
    ```env
    OPENAI_API_KEY=<your OpenAPI API key>
    NOTION_API_KEY=<your Notion Integration API key>
    ```
1. Run the Qdrant docker container
    ```bash
    ./run_qdrant.sh
    ```
1. Run the StreamLit app
    ```bash
    streamlit run src/main.py
    ```
1. Access http://localhost:8501 and click on `Load Data` before running any queries.
