import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown






genai.configure(api_key="AIzaSyCPF_fd2N_i-5BslHRygfAWtBVb2ydl1bc")


system_prompt="""
                 You are an AI code reviewer specializing in multiple programming languages. 
                 You should analyze the submitted code and identify potential bugs, errors, or areas of improvement.
                 You should also provide the fixed code snippets.
                 Provide the summary actionable feedback and suggest improvements.
                 If the user asks questions other than programming languages, then politely tell them that is out of your scope and politely ask them to ask questions about programming"""
code_reviewer=genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",system_instruction=system_prompt)


st.title("AI ReviewBot🤖")


user_prompt=st.text_area("Enter the code to be reviewed...")

btn=st.button("📝Review")

if btn==True:
    response=code_reviewer.generate_content(user_prompt)
    st.write(response.text)
         


