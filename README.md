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
- Can be run locally **without an internet connection**
- No local installation required for users (if hosted online)

## 🚀 How to Run Locally
### Prerequisites:
- Python 3.7+

### 1. Clone the repository:
```bash
git clone https://github.com/vaibhavgarg2004/Pdf_Utility.git
cd Pdf_Utility
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the app:
```bash
streamlit run pdf_utility_web.py
```

Then open `http://localhost:8501` in your browser.

📌 **Note:** Once set up, the app can be used offline with full functionality.

## 📂 Project Structure
```
PDF-Utility-Tool/
├── pdf_utility_web.py        # Streamlit web app code
├── pdf_utility.py            # Standalone Python script
├── requirements.txt          # Required Python packages
├── README.md                 # Project documentation
```

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

---
Built with ❤️ using Streamlit and PyPDF2
