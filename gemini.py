
import streamlit as st

import google.generativeai as genai


# Set up Gemini API key
f = open(r"D:\ML\Innomatics_Research_Lab_Internship\task9_Openai_api_chat\keys\.gemini_api_key.txt")
key = f.read()
genai.configure(api_key=key)


# Custom CSS for dark theme
def set_custom_style():
    st.markdown(
        """
        <style>
        .stTextInput>div>div>div>textarea {
            height: 200px; /* Adjust the height as needed */
        }
        
        .st-bj { background-color: #FFFFFF; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Apply custom style
set_custom_style()
# Take user's input

st.markdown("<h1 style='color:  #4d0404;'>👩‍💻Google GenAI App - Gemini AI Tutor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#b10a0a;'>Welcome to the Google GenAI App! The system will now function as an AI Data Science tutor.</h3>", unsafe_allow_html=True)


#take users input
#prompt= st.text_input("Enter your Python code here:",rows=200)
#take users input


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction= """Your name is "Chitti The Robot".You are a helpful AI Tutor Assistant who answers all the user queries polietly.
                              Given a Data Science topic help the user understand it. You also answer any followup questions as well to understand the concepts clearly.
                              If a question is not related to data science, the response should be, 'That is beyond my knowledge.' """)
            

 # if there is no chat history in session, init one   
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
st.chat_message("ai").write("Hi, this is Chitti. I'm your data science AI tutor. How can I assist you?")

# Init the chat object
chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)
user_prompt = st.chat_input()
if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history
