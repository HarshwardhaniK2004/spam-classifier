import streamlit as st
import pickle

# Page config
st.set_page_config(
    page_title="Spam Detector",
    page_icon="📩",
    layout="centered"
)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #333;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 20px;
    }
    .result {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📩 Spam Message Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check whether a message is Spam or Not</div>', unsafe_allow_html=True)

# Input box
message = st.text_area("✉️ Enter your message:", height=150)

# Predict button
if st.button("🔍 Analyze Message"):
    if message.strip() == "":
        st.warning("Please enter a message first.")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.markdown('<div class="result" style="color:red;">🚫 This is SPAM</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result" style="color:green;">✅ This is NOT Spam</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")