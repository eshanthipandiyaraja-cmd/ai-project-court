import streamlit as st
import requests

st.set_page_config(page_title="LegalEase", layout="wide")

st.title("LegalEase")
st.caption("AI-assisted legal document generator")

st.sidebar.header("Document Details")
doc_type = st.sidebar.text_input("Document Type", "Legal Agreement")
parties = st.sidebar.text_area("Parties", "Party A, Party B")
terms = st.sidebar.text_area("Terms & Conditions", "Payment within 30 days of invoice.")
effective_date = st.sidebar.text_input("Effective Date", "27-09-2026")
instructions = st.sidebar.text_area("Additional Instructions", "")

if st.sidebar.button("Generate Document", type="primary"):
    payload = {
        "document_type": doc_type,
        "parties": parties,
        "terms": terms,
        "effective_date": effective_date,
        "additional_instructions": instructions
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/generate", json=payload, timeout=10)
        if response.status_code == 200:
            data = response.json()
            st.success("Document Generated Successfully!")
            st.subheader(data.get("title", "Legal Document"))
            
            content = data.get("content", data.get("document", ""))
            st.text_area("Generated Content", content, height=250)
            
            # Download PDF/Text File Button
            st.download_button(
                label="📥 Download Legal Document (PDF/TXT)",
                data=content,
                file_name="LegalEase_Agreement.txt",
                mime="text/plain"
            )
        else:
            st.error(f"Backend Error: {response.status_code}")
    except Exception as e:
        st.error(f"Connection Error: {e}")