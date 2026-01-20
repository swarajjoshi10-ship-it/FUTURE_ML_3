import streamlit as st
from google.cloud import dialogflow_v2 as dialogflow
from google.cloud.dialogflow_v2 import TextInput, QueryInput
from google.oauth2 import service_account

PROJECT_ID = "advance-lacing-484909-t2"

CREDENTIALS_PATH = r"C:\Users\swaraj joshi\OneDrive\Desktop\futureinterns_3\dialogflow_key.json"

credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH
)

def detect_intent(text):
    session_client = dialogflow.SessionsClient(credentials=credentials)

    session = session_client.session_path(PROJECT_ID, "streamlit-user")

    text_input = TextInput(text=text, language_code="en")
    query_input = QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={
            "session": session,
            "query_input": query_input
        }
    )

    return response.query_result.fulfillment_text


st.set_page_config(page_title="Customer Support Bot", page_icon="🤖")

st.title("🤖 Customer Support Chatbot")
st.write("Same Dialogflow bot used on Telegram")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:")

if user_input:
    bot_reply = detect_intent(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", bot_reply))

for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
