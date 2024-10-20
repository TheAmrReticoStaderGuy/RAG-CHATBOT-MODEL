import streamlit as st

# Streamlit main function
def main():
        st.title("RAG Based Pre-Defined Folder Based QA")
        query = st.text_input("Enter your Question")
        if st.button("Submit"):
            llm_response = qa_chain(query)
            process_llm_response(llm_response)

if __name__ == "__main__":
        main()
