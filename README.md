# 🧰 PDF Utility Tool

A simple and interactive PDF utility tool built with Python and Streamlit. This tool allows users to:

- 🔗 Merge multiple PDF files
- ✂️ Split a PDF into individual pages or extract specific page ranges
- 📄 Extract text from PDF files
- 🔄 Rotate PDF pages
- 🔐 Encrypt PDF files with a password

## 🌐 Live Website
You can try the tool live here: **[https://pdfutility-zwo4p85ovayuptierqnsep.streamlit.app](https://pdfutility-zwo4p85ovayuptierqnsep.streamlit.app)**

## 🛠 Features
- Web-based interface using Streamlit
- Upload and download files directly from the browser
- Secure and efficient file handling
- No local installation required for users (if hosted online)

## 🚀 How to Run Locally
### Prerequisites:
- Python 3.7+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Run the app:
```bash
streamlit run pdf_utility_web.py
```
Then open `http://localhost:8501` in your browser.

## 📂 Project Structure
```
PDF-Utility-Tool/
├── pdf_utility_web.py        # Streamlit web app code
├── pdf_utility.py            # Original standalone Python script
├── requirements.txt          # Required Python packages
├── README.md                 # Project documentation
```

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

---
Built with ❤️ using Streamlit and PyPDF2
