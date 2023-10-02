from review_scrapper import scrape_download_reviews
from llm_run import run_llm
import os
import streamlit as st
from streamlit_chat import message

st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(20, 40, 31) 0%, rgb(50, 100, 100) 50%, rgb(100, 117, 25) 75%);
        -webkit-text-fill-color: white;
    }

    .stTextArea [data-baseweb=base-input] [disabled=""]{
        background-image: linear-gradient(45deg, red, purple, red);
        -webkit-text-fill-color: gray;
    }
    </style>
    """,unsafe_allow_html=True)

def main():
    print("scrapping...")
    review_url = "https://www.consumeraffairs.com/food/chick-fil-a.html"
    review_file_path = "docs/cleaned_reviews.txt"
    if not os.path.exists(review_file_path):
        scrape_download_reviews(review_url)
        print("reviews saved successfully")
    else:
        print("cleaned_reviews.txt already exists, skipping scraping")
    
    st.header("Chick-fil-A Review Analysis")
    
    with st.spinner("Getting the hottest review for you..."):
        hottest_review = run_llm(review_file_path, "what's the most positive review out of all the reviews?")
        st.text_area(label="Your hottest review so far:", value=hottest_review["result"], height=300, disabled=True)
    
    prompt = st.text_input("Want to know more about your review?", placeholder="what do you want to know about the reviews?")
    
    # setup user session with the history of the reviews
    if "user_prompt_history" not in st.session_state:
        st.session_state["user_prompt_history"] = []
        
    if "chat_answer_history" not in st.session_state:
        st.session_state["chat_answer_history"] = []
        
    # Initialize the session state for the chat history to be used as the memory(context) for the chatbot
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    
    if prompt:
        with st.spinner("Getting insights for you..."):
            generated_response = run_llm(review_file_path, prompt, chat_history=st.session_state["chat_history"])
            
            insight = generated_response["result"]
            # Save the user prompt and the chatbot answer to the session state
            # so that we can display them later
            st.session_state["user_prompt_history"].append(prompt)
            st.session_state["chat_answer_history"].append(insight)
            st.session_state["chat_history"].append((prompt, insight))
    
    if st.session_state["chat_answer_history"]:
        for generated_response, user_query in zip(
            st.session_state["chat_answer_history"], st.session_state["user_prompt_history"]
        ):
            message(user_query, is_user=True)
            st.success(generated_response)

if __name__ == "__main__":
    main()
