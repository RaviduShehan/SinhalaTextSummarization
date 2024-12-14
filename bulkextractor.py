from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import logging
import sys
import os

import pdf_list

logging.basicConfig(level=logging.INFO)


def main():
    try:
        # List of PDF files to process
        pdf_files = pdf_list.pdf_list

        for pdf_file in pdf_files:
            # Extracting filename without extension
            file_name = os.path.splitext(os.path.basename(pdf_file))[0]

            # Create document for extraction with configurations
            pdf_document = Document(
                document_path=pdf_file,
                language='sin'
            )
            pdf2text = PDF2Text(document=pdf_document)
            logging.info(f"Starting text extraction from {pdf_file}.")
            content = pdf2text.extract()
            logging.info("Text extraction completed.")

            # Specify the path for the output text file
            output_file_path = f'Dataset/extracted_texts/{file_name}_extracted_content.txt'
            if isinstance(content, list):
                content = "\n".join([item.get('text', '') for item in content if isinstance(item, dict)])

            # Write the content to the text file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(content)

            logging.info(f"Content written to {output_file_path}.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
