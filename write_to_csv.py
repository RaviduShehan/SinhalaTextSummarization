import os
import csv

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def summarize_text(text):
    # Placeholder function for text summarization
    # Replace this with a more advanced summarization model if needed
    lines = text.split('\n')
    summary = ' '.join(lines[:3])  # For demonstration, taking the first 3 lines as summary
    return summary

# Directory containing the cleaned text files
cleaned_texts_directory = 'Dataset/cleaned_texts'
csv_output_file = 'Dataset/cleaned_content_new2.csv'

# Get the list of cleaned files
cleaned_files = [os.path.join(cleaned_texts_directory, f) for f in os.listdir(cleaned_texts_directory) if f.endswith('.txt')]

# Prepare data for CSV
csv_data = []
for file_path in cleaned_files:
    cleaned_lines = read_file(file_path)
    cleaned_content = ''.join(cleaned_lines)
    summary = summarize_text(cleaned_content)
    csv_data.append([os.path.basename(file_path), cleaned_content, summary])

# Write the data to a CSV file
with open(csv_output_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Filename', 'Cleaned_Content_new2', 'Summary'])
    writer.writerows(csv_data)

print("Cleaned content and summaries saved to CSV.")