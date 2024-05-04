import streamlit as st
import requests

# Define the FastAPI endpoint
API_URL = "http://localhost:5555/qa/"

# def ask_question(question):
#     # Make a POST request to the FastAPI endpoint
#     response = requests.post(API_URL, json={"query": question})
#     if response.status_code == 200:
#         return response.json()["answer"]
#     else:
#         return "Error: Unable to get answer."
def ask_question(question):
    return question+" returned."


def main():
    st.title("Question Answering System")

    # Input box for the question
    question = st.text_input("Enter your question here:")

    if st.button("Get Answer"):
        if question:
            # Call the ask_question function to get the answer
            answer = ask_question(question)
            st.write("Answer:", answer)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
