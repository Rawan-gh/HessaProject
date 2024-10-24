import streamlit as st
from urllib.parse import urlparse

# Custom CSS for right-aligned text and styling
st.markdown("""
    <style>
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
        background-color: #f0f2f6;
    }
    
    .css-1kyxreq {
        text-align: right;
    }
    
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
        cursor: pointer;
        border-radius: 10px;
        transition: background-color 0.3s;
    }
    
    .stButton button:hover {
        background-color: #45a049;
    }

    .stTextInput {
        direction: rtl;
        font-size: 16px;
    }

    h1 {
        color: #2c3e50;
        font-size: 36px;
        text-align: center;
        margin-bottom: 20px;
    }

    .stTextInput > div > input {
        background-color: #e8f0fe;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #cbd5e0;
        font-size: 18px;
        direction: rtl;
    }
    
    .css-1aumxhk, .css-qbe2hs {
        font-size: 18px;
        color: #2c3e50;
    }

    .stAlert {
        font-size: 20px;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# List of valid base URLs (root domains) with "www." and without it
valid_links = [
    "https://www.moi.gov.sa",
    "https://www.moh.gov.sa",
    "https://www.moe.gov.sa",
    "https://www.mc.gov.sa",
    "https://www.hrsd.gov.sa",
    "https://www.mof.gov.sa",
    "https://www.zatca.gov.sa",
    "https://www.stats.gov.sa",
    "https://www.sta.gov.sa",
    "https://www.iam.gov.sa",
    
]

# Streamlit app
def main():
    st.title("تحقق من صحة الرابط")
    st.write("أدخل رابطًا للتحقق مما إذا كان صالحًا.")

    # Input field
    query = st.text_input("أدخل الرابط", "")

    # Button for validation
    if st.button("تحقق"):
        parsed_url = urlparse(query)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        # Remove "www." prefix if present in both the input and valid links
        normalized_base_url = base_url.replace("www.", "")
        normalized_valid_links = [link.replace("www.", "") for link in valid_links]

        if normalized_base_url in normalized_valid_links:
            st.success("الرابط صالح.")
        else:
            st.error("الرابط غير صالح.")
    
    # Display additional content if needed
    st.write("مثال على الروابط الصالحة: [وزارة الداخلية](https://www.moi.gov.sa)")

if __name__ == '__main__':
    main()
