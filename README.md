# Notion LangChain

### Requirements

-   Docker
-   OpenAI API Key ([retrieve here](https://platform.openai.com/account/billing))
-   Notion Integration + API Key ([setup here](https://www.notion.so/my-integrations))
-   Pages in Notion shared with Notion Integration (You can add access by clicking on `...` on the top right of a Notion page and adding the connection to your Notion Integration)
    <img width="504" alt="スクリーンショット 2023-09-13 20 19 20" src="https://github.com/akiyamasho/notion-langchain/assets/35907066/4216e4d2-004b-42c1-8425-418400b7d788">

### Setup

1. Create a `.env` file with your OpenAI API Key and Notion Integration API Key:
    ```env
    OPENAI_API_KEY=<your OpenAPI API key>
    NOTION_API_KEY=<your Notion Integration API key>
    QDRANT_HOST=qdrant
    ```
1. Run the app
    ```bash
    docker-compose up
    ```
1. Access http://localhost:8000 and click on `Load Data` before running any queries.

### References

This [Medium Blog](https://betterprogramming.pub/build-a-chatbot-for-your-notion-documents-using-langchain-and-openai-e0ad7b903b84) by @htrivedi99 sums it up.
I simply modularised it and made sure the python package versions fit the code from the time of writing, as most of LangChain and Qdrant have had breaking changes since then.
Also fixed an issue with Qdrant having errors with multiple workers.
