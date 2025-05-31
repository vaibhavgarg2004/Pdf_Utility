import PyPDF2
import os
def ensure_pdf(filename):
    return filename if filename.lower().endswith('.pdf') else filename + '.pdf'

def merge_pdfs():
    print("Choose merge option:")
    print("1. Enter PDF file names manually")
    print("2. Merge all PDFs in the current directory")
    choice = input("Enter choice (1 or 2): ")

    merger = PyPDF2.PdfMerger()

    if choice == '1':
        pdfs = input("Enter PDF file names to merge (comma-separated): ").split(',')
        for pdf in pdfs:
            pdf = ensure_pdf(pdf.strip())
            if os.path.exists(pdf):
                merger.append(pdf)
            else:
                print(f"File not found: {pdf}")

    elif choice == '2':
        pdfs = sorted([f for f in os.listdir() if f.lower().endswith('.pdf')])
        if not pdfs:
            print("No PDF files found in the current directory.")
            return
        print(f"Merging {len(pdfs)} PDF(s):")
        for pdf in pdfs:
            print(f"  - {pdf}")
            merger.append(pdf)
    else:
        print("Invalid choice.")
        return

    output = ensure_pdf(input("Enter output file name (e.g., merged.pdf): "))
    merger.write(output)
    merger.close()
    print(f"Merged into: {output}")


def split_pdf():
    file = ensure_pdf(input("Enter the PDF file to split: "))
    if not os.path.exists(file):
        print("File not found.")
        return

    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")

    print("Choose split option:")
    print("1. Split entire PDF into individual pages")
    print("2. Extract a page range into a new PDF")

    option = input("Enter choice (1 or 2): ")

    if option == '1':
        for i in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])
            output_filename = f'page_{i+1}.pdf'
            with open(output_filename, 'wb') as f:
                writer.write(f)
            print(f"Saved: {output_filename}")

    elif option == '2':
        try:
            start = int(input(f"Enter start page (1 to {total_pages}): ")) - 1
            end = int(input(f"Enter end page ({start+1} to {total_pages}): "))
            if start < 0 or end > total_pages or start >= end:
                print("Invalid range.")
                return
        except ValueError:
            print("Invalid input.")
            return

        writer = PyPDF2.PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])

        output = ensure_pdf(input("Enter output file name for the extracted range: "))
        with open(output, 'wb') as f:
            writer.write(f)
        print(f"Saved selected pages to {output}")

    else:
        print("Invalid option.")


def extract_text():
    file = ensure_pdf(input("Enter the PDF file to extract text from: "))
    if not os.path.exists(file):
        print("File not found.")
        return
    
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    output = input("Enter output .txt file name: ")
    with open(output, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Text extracted to {output}")

def rotate_pdf():
    file = ensure_pdf(input("Enter the PDF file to rotate: "))
    if not os.path.exists(file):
        print("File not found.")
        return
    
    angle = int(input("Enter rotation angle (90, 180, 270): "))
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()

    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)
    
    output = ensure_pdf(input("Enter output file name: "))
    with open(output, 'wb') as f:
        writer.write(f)
    print(f"Rotated PDF saved as {output}")

def encrypt_pdf():
    file = ensure_pdf(input("Enter the PDF file to encrypt: "))
    if not os.path.exists(file):
        print("File not found.")
        return

    password = input("Enter the password to encrypt the PDF: ")
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    output = ensure_pdf(input("Enter output encrypted PDF file name: "))
    with open(output, 'wb') as f:
        writer.write(f)
    print(f"Encrypted PDF saved as {output}")

def main():
    while True:
        print("\nPDF Utility Menu")
        print("1. Merge PDFs")
        print("2. Split PDF")
        print("3. Extract Text")
        print("4. Rotate Pages")
        print("5. Encrypt PDF")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            merge_pdfs()
        elif choice == '2':
            split_pdf()
        elif choice == '3':
            extract_text()
        elif choice == '4':
            rotate_pdf()
        elif choice == '5':
            encrypt_pdf()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
