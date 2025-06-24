import streamlit as st
import requests

st.title("AWS Bedrock Blog Generator 🤖")
st.write("Enter a topic below and generate a 200-word blog using AWS Bedrock and Titan Text G1 Premier!")

topic = st.text_input("Blog Topic", "")

if st.button("Generate Blog"):
    if not topic.strip():
        st.warning("Please enter a blog topic.")
    else:
        with st.spinner("Generating your blog post..."):
            api_url = "https://fevqycl0wk.execute-api.us-east-1.amazonaws.com/dev/blog-generation"
            try:
                resp = requests.post(
                    api_url,
                    json={"blog_topic": topic},
                    timeout=30
                )
                if resp.ok:
                    result = resp.json()
                    # Defensive: handle both dict and string
                    if isinstance(result, dict):
                        blog = result.get("blog")
                    else:
                        blog = result
                    if blog:
                        st.success("Blog generated! 🎉")
                        st.markdown("---")
                        st.subheader("Your Blog Post")
                        st.markdown(blog)
                    else:
                        st.error("No blog was generated. Please try a different topic.")
                else:
                    st.error(f"Error: {resp.status_code}\n{resp.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
