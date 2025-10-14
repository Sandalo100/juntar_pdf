import streamlit as st
from PyPDF2 import PdfMerger
import tempfile

st.set_page_config(page_title="Juntar PDFs", page_icon="📚")

st.title("📚 Juntar PDFs Online")

uploaded_files = st.file_uploader("Envie seus arquivos PDF:", type="pdf", accept_multiple_files=True)

if uploaded_files:
    merger = PdfMerger()
    for uploaded_file in uploaded_files:
        merger.append(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        merger.write(tmp.name)
        merger.close()
        st.success("✅ PDFs unidos com sucesso!")
        with open(tmp.name, "rb") as f:
            st.download_button("📥 Baixar PDF Unido", data=f, file_name="PDF_unido.pdf", mime="application/pdf")
