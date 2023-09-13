import streamlit as st

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores.qdrant import Qdrant

from streamlit_chat import message

from src.config import NOTION_API_KEY, OPENAI_API_KEY
from src.notion import CONTENT_TYPE_JSON, NOTION_VERSION, load_notion
from tokenizer import chunk_tokens
from vectordb import connect_to_vectorstore, load_data_into_vectorstore


@st.cache_data
def cache_headers(notion_api_key: str = NOTION_API_KEY):
    headers = {
        "Authorization": f"Bearer {notion_api_key}",
        "Content-Type": CONTENT_TYPE_JSON,
        "Notion-Version": NOTION_VERSION,
    }
    return headers


@st.cache_resource
def load_chain(_client, api_key: str):
    if len(api_key) == 0:
        api_key = "temp value"
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = Qdrant(
        client=_client,
        collection_name="notion_streamlit",
        embedding_function=embeddings.embed_query,
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(
            temperature=0.0, model_name="gpt-3.5-turbo", openai_api_key=api_key
        ),
        retriever=vectorstore.as_retriever(),
    )
    return chain


st.title("Chat With Your Notion Documents!")

vector_store = connect_to_vectorstore()
with st.sidebar:
    notion_headers = cache_headers(NOTION_API_KEY)

    load_data = st.button("Load Data")
    if load_data:
        documents = load_notion(notion_headers)

        chunks = []
        for doc in documents:
            chunks.extend(chunk_tokens(doc, 100))

        for chunk in chunks:
            print(chunk)

        load_data_into_vectorstore(vector_store, chunks)
        print("Documents loaded.")

chain = load_chain(vector_store, OPENAI_API_KEY)

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


user_input = st.text_input(
    "You: ", placeholder="Ask questions about your Notion docs:", key="input"
)

if user_input:
    result = chain(
        {"question": user_input, "chat_history": st.session_state["generated"]}
    )
    response = result["answer"]

    st.session_state["past"].append(user_input)
    st.session_state["generated"].append((user_input, result["answer"]))

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(
            st.session_state["past"][i], is_user=True, key=str(i) + "_user"
        )
        message(st.session_state["generated"][i][1], key=str(i))
