import re
from indicnlp.tokenize.sentence_tokenize import sentence_split
import pandas as pd
def clean_text(text):
    # Remove special characters, numbers, and unnecessary symbols
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'[!@#$%^&*()_+={}\[\]:;<>,.?/~`\'\"-]', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()

with open('Dataset/extracted_texts/6346_extracted_content.txt', 'r', encoding='utf-8') as file:
    raw_text = file.read()

cleaned_text = clean_text(raw_text)
sentences = sentence_split(cleaned_text, 'si')
summaries = [' '.join(sentence.split()[:15]) for sentence in sentences]
df = pd.DataFrame({
    'input': sentences,
    'summary': summaries
})

# Write the dataframe to a CSV file
df.to_csv('Dataset/extracted_texts/6346_sinhala_text_summarization_dataset.csv', index=False, encoding='utf-8-sig')
print(summaries)
print("Dataset written to sinhala_text_summarization_dataset.csv")
print(cleaned_text[:10000])

#
#
# import pandas as pd
# import re
#
#
#
# # Function to clean text
# def clean_text(text):
#     text = re.sub(r'\d+', '', text)  # Remove digits
#     text = re.sub(r'[!@#$%^&*()_+={}\[\]:;<>,.?/~`\'\"-]', ' ', text)  # Remove special characters
#     text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
#     return text.strip()
#
# # Load and clean the raw text
# with open('Dataset/extracted_texts/6203_extracted_content.txt', 'r', encoding='utf-8') as file:
#     raw_text = file.read()
#
# cleaned_text = clean_text(raw_text)
#
#
# # Split the text into sentences
# sentences = sentence_split(cleaned_text, 'si')
#
#
# # For the sake of example, let's assume summaries are the first 10 words of each sentence
# summaries = [' '.join(sentence.split()[:10]) for sentence in sentences]
#
# # Create a dataframe with input and summary pairs
# df = pd.DataFrame({
#     'input': sentences,
#     'summary': summaries
# })
#
# # Write the dataframe to a CSV file
# df.to_csv('Dataset/extracted_texts/sinhala_text_summarization_dataset.csv', index=False, encoding='utf-8')
#
# print("Dataset written to sinhala_text_summarization_dataset.csv")