import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import os


st.set_page_config(
    page_title="QuickPost - LinkedIn Post Generator", 
    page_icon="📝",
    layout="wide"
)


length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("QuickPost: LinkedIn Post Generator")
    st.subheader("Create engaging posts in seconds")
   
    
    try:
        fs = FewShotPosts()
        tags = fs.get_tags()
    except Exception as e:
        st.error(f"Error loading post data: {str(e)}")
        tags = ["Job Search", "Mental Health", "Motivation", "Self Improvement", "Scams"]
    
    
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)
    
    
    if st.button("✨ Generate Post"):
        with st.spinner("Crafting your LinkedIn post..."):
            try:
                post = generate_post(selected_length, selected_language, selected_tag)
                st.success("Post generated successfully!")
                st.text_area("Your LinkedIn Post:", value=post, height=300)
            except Exception as e:
                st.error(f"Error generating post: {str(e)}")

   
    st.markdown("---")
    st.markdown("Ratnesh Singh")

if __name__ == "__main__":
    main()
