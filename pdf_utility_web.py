import streamlit as st
import PyPDF2
import os

def ensure_pdf(filename):
    return filename if filename.lower().endswith('.pdf') else filename + '.pdf'

st.set_page_config(page_title="PDF Utility Tool", layout="centered")
st.title("🧰 PDF Utility Tool")

menu = st.sidebar.selectbox("Choose an action", [
    "Merge PDFs",
    "Split PDF",
    "Extract Text",
    "Rotate PDF",
    "Encrypt PDF"
])

uploaded_files = st.file_uploader("Upload PDF file(s)", type="pdf", accept_multiple_files=True)

def save_file(file, name):
    with open(name, 'wb') as f:
        f.write(file.read())
    return name

if menu == "Merge PDFs" and uploaded_files:
    merger = PyPDF2.PdfMerger()
    for file in uploaded_files:
        merger.append(file)
    output_name = st.text_input("Output filename", "merged.pdf")
    if st.button("Merge PDFs"):
        merger.write(output_name)
        merger.close()
        st.success(f"Merged into {output_name}")
        with open(output_name, "rb") as f:
            st.download_button("Download Merged PDF", f, file_name=output_name)

elif menu == "Split PDF" and uploaded_files:
    file = uploaded_files[0]
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    st.write(f"Total pages: {total_pages}")
    mode = st.radio("Split mode", ["Individual pages", "Page range"])

    if mode == "Individual pages" and st.button("Split"):
        for i in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])
            out = f"page_{i+1}.pdf"
            with open(out, 'wb') as f:
                writer.write(f)
            st.write(f"Saved {out}")
            with open(out, "rb") as f:
                st.download_button(f"Download {out}", f, file_name=out)

    elif mode == "Page range":
        start = st.number_input("Start page (1-based)", min_value=1, max_value=total_pages, value=1)
        end = st.number_input("End page (inclusive)", min_value=start, max_value=total_pages, value=total_pages)
        output_name = st.text_input("Output filename", "range_output.pdf")
        if st.button("Extract range"):
            writer = PyPDF2.PdfWriter()
            for i in range(start-1, end):
                writer.add_page(reader.pages[i])
            with open(output_name, 'wb') as f:
                writer.write(f)
            st.success(f"Saved to {output_name}")
            with open(output_name, "rb") as f:
                st.download_button("Download Extracted Range", f, file_name=output_name)

elif menu == "Extract Text" and uploaded_files:
    file = uploaded_files[0]
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    output = st.text_input("Output .txt file name", "output.txt")
    if st.button("Extract Text"):
        with open(output, 'w', encoding='utf-8') as f:
            f.write(text)
        st.success(f"Text extracted to {output}")
        with open(output, "rb") as f:
            st.download_button("Download Text File", f, file_name=output)

elif menu == "Rotate PDF" and uploaded_files:
    file = uploaded_files[0]
    angle = st.selectbox("Rotation angle", [90, 180, 270])
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()
    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)
    output = st.text_input("Output filename", "rotated.pdf")
    if st.button("Rotate"):
        with open(output, 'wb') as f:
            writer.write(f)
        st.success(f"Rotated PDF saved as {output}")
        with open(output, "rb") as f:
            st.download_button("Download Rotated PDF", f, file_name=output)

elif menu == "Encrypt PDF" and uploaded_files:
    file = uploaded_files[0]
    password = st.text_input("Enter password to encrypt PDF", type="password")
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    output = st.text_input("Output filename", "encrypted.pdf")
    if st.button("Encrypt"):
        with open(output, 'wb') as f:
            writer.write(f)
        st.success(f"Encrypted PDF saved as {output}")
        with open(output, "rb") as f:
            st.download_button("Download Encrypted PDF", f, file_name=output)
