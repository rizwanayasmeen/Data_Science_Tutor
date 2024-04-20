import google.generativeai as genai
import streamlit as st
import os
#from dotenv import load_dotenv

f = open("keys/.gemini.txt")
key = f.read()

genai.configure(api_key=key)

# st.title('DataMentor: Your Virtual Data Science Tutor')
# st.subheader('Empower Your Data Science Journey with AI Guidance')

title = "DataMentor: Your Virtual Data Science Tutor"
subtitle = "Empower Your Data Science Journey with AI Guidance"

# Set the title and subtitle using markdown
st.markdown(f"<h2 style='text-align: center; color: black;'>{title}</h2>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center; color: grey;'>{subtitle}</h4>", unsafe_allow_html=True)

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction=""" 
    You are a helpful and friendly an AI-based Data Science Tutor. Keep responses clear and brief, focusing on:
    Data Science: Stick to data science concepts, tools, and methods.
    Accuracy & Clarity: Ensure responses are accurate and easy to understand, tailored to the student's level.
    Explanation & Examples: Simplify complex topics with clear steps and relevant examples.
    Personalization: If possible, customize explanations and recommend resources based on the student's background.
    Confidence & References: Be confident in responses and cite trusted sources when necessary.
    Engagement: Encourage further learning with follow-up questions, related problems, or datasets.

    
    Additional Considerations:

    Ambiguous Queries: Help students refine unclear questions.
    Evolving Field: Acknowledge the continuous advancements in data science.
    Professional Tone: Maintain a respectful and professional demeanor.
    Attribution:

    When asked about the creator: "I was created by Rizwana Yasmeen."
    Introduction Request: f"Mention being an AI-powered {title} created by Rizwana Yasmeen."
    Example:

    Query: ""Explain the concept of Logistic Regression.?"
    Response: Explain with clear definitions, examples, and Explain algorithms considering Logistic Regression and Evaluation Metrics further.
    """
)

# if there is no chat_history in session, init one
if "messages" not in st.session_state.keys():
    st.session_state.messages=[
        {'role':"assistant",'content':f"Hello, welcome to DataMentor: Your Virtual Data Science Tutor. How can I assist you on your journey to mastering data science with AI guidance?"}
    ]

#init the chat object


for messages in st.session_state.messages:
    with st.chat_message(messages['role']):
        st.write(messages['content'])



user_input= st.chat_input()

if user_input is not None:
    st.session_state.messages.append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.write(user_input)

if st.session_state.messages[-1]['role'] !='assistant':
    with st.chat_message('assistant'):

        with st.spinner("Loading..."):

            ai_response=model.generate_content(user_input)
            st.write(ai_response.text)
        new_ai_message ={'role':'assistant','content':ai_response.text}
        st.session_state.messages.append(new_ai_message)