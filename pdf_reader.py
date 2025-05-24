from pypdf import PdfReader


def read_pdf_and_chunk(pdf_path):        
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    
    all_text= ""

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
      #  print(text)
        all_text+= text
        #print(f"Page {page_number + 1}:\n{text}\n{'='*20}")
    
    
    chunks= []

    for i in range(0, len(all_text), 150):
        if i+200<len(all_text):
            chunks.append(all_text[i:i+200])
            
    for chunk in chunks:
        print(chunk)
        print()
        
    return chunks

 # read_pdf_and_chunk(r"C:\Users\lokes\Downloads\nvidia_stock_summary_2024 (1).pdf")
        
    
        
    