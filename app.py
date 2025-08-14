import streamlit as st
from splitter.splitter import split_pdf
from analyzer.parser import extract_text_from_pdf
from analyzer.comparator import compare_entries
from analyzer.utils import display_results

st.set_page_config(page_title="Seniority Toolkit", layout="wide")
st.title("🧰 CFs Seniority List - By Jagdev Singh Dosanjh (8146553307)")
st.markdown(
    """
    <div style='text-align: center; padding: 20px; font-size: 18px;'>
        <strong>Welcome and Congrats to all CFs!</strong>
        <p>This tool helps you split large PDF file and analyze seniority entries.</p>
    </div>
    """,
    unsafe_allow_html=True
)


tab1, tab2 = st.tabs(["📄 PDF Splitter", "📊 Seniority Analyzer"])

with tab1:
    uploaded_file = st.file_uploader("Upload a large PDF to split", type="pdf")
    pages_per_split = st.number_input("Pages per split file", min_value=1, value=10)

    if uploaded_file:
        st.success("PDF uploaded successfully.")
        output_files = split_pdf(uploaded_file, pages_per_split)

        st.subheader("📂 Download Split PDFs")
        for i, pdf_bytes in enumerate(output_files):
            st.download_button(
                label=f"Download Part {i+1}",
                data=pdf_bytes,
                file_name=f"Split_Part_{i+1}.pdf",
                mime="application/pdf"
            )

with tab2:
    seniority_files = st.file_uploader("Upload split seniority PDFs", type="pdf", accept_multiple_files=True)
    objection_file = st.file_uploader("Upload Objection Letter PDF", type="pdf")

    if seniority_files and objection_file:
        with st.spinner("Extracting and analyzing..."):
            combined_text = ""
            for f in seniority_files:
                combined_text += extract_text_from_pdf(f)

            objection_text = extract_text_from_pdf(objection_file)
            results = compare_entries(combined_text, objection_text)
            display_results(results)

st.write(
    """
    <div style='text-align: center; padding: 20px; font-size: 14px;'>
        <hr>
        <p>© 2025 Jagdev Singh Dosanjh</p>
        <a href="https://www.dosanjhpubsasr.org">dosanjhpubsasr.org | All rights reserved.</a>
        <p>Developed by Jagdev Singh Dosanjh.</p>
        <p>📧 Email: <a href='mailto:jagdevsinghdosanjh@gmail.com</p>
    </div>
    """,
    unsafe_allow_html=True
)
