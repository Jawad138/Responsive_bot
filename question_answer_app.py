import streamlit as st
import openai

openai_api_key = "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"

def generate_answer(question):
    openai.api_key = openai_api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response["choices"][0]["text"].strip()
    return answer

def main():
    st.title("Question Answering App")

    question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if question:
            answer = generate_answer(question)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.write("Please enter a question.")

if __name__ == '__main__':
    main()
