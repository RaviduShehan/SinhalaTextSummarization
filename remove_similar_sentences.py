# import logging
# import os
# import difflib
#
# def read_file(file_path):
#     logging.info(f"Reading the file")
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.readlines()
#
# def write_file(file_path, lines):
#     logging.info(f"Writing cleaned content to file: {file_path}")
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.writelines(lines)
#
# def is_similar(a, b, threshold=0.8):
#     return difflib.SequenceMatcher(None, a, b).ratio() > threshold
#
# def remove_similar_sentences_from_multiple_files(file_contents, threshold=0.8):
#     unique_lines_per_file = [[] for _ in range(len(file_contents))]
#
#     for i, lines1 in enumerate(file_contents):
#         for line1 in lines1:
#             is_unique = True
#             for j, lines2 in enumerate(file_contents):
#                 if i != j and any(is_similar(line1, line2, threshold) for line2 in lines2):
#                     is_unique = False
#                     break
#             if is_unique:
#                 unique_lines_per_file[i].append(line1)
#
#     return unique_lines_per_file
#
# # Directory containing the text files
# input_directory = 'Dataset/extracted_texts'
# output_directory = 'Dataset/cleaned_texts'
#
# # Ensure the output directory exists
# os.makedirs(output_directory, exist_ok=True)
#
# # Get the list of input files
# input_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith('.txt')]
#
# # Read the content of each file
# file_contents = [read_file(file) for file in input_files]
#
# # Remove similar sentences across all files
# unique_lines_per_file = remove_similar_sentences_from_multiple_files(file_contents)
#
# # Write the cleaned content to new files
# for i, unique_lines in enumerate(unique_lines_per_file):
#     output_file_path = os.path.join(output_directory, os.path.basename(input_files[i]))
#     write_file(output_file_path, unique_lines)
#
# print("Similar sentences removed and cleaned files written.")


import os
import re


def process_text(input_text):
    # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', input_text)

    # Remove unnecessary spaces at the beginning and end of the text
    cleaned_text = cleaned_text.strip()

    # Replace multiple newlines with a single newline
    cleaned_text = re.sub(r'\n+', '\n', cleaned_text)

    # Further formatting if needed
    lines = cleaned_text.splitlines()
    formatted_text = ""
    section_count = 0

    for line in lines:
        line = line.strip()
        if line:
            if line.startswith('**'):
                formatted_text += "\n" + line + "\n"
            elif line.startswith('(') and line.endswith(')'):
                formatted_text += "\n" + line + "\n"
            elif any(char.isdigit() for char in line) and len(line.split(' ')) < 10:
                section_count += 1
                formatted_text += f"\n{section_count}. {line}\n"
            else:
                formatted_text += line + " "
        else:
            formatted_text += "\n"

    # Ensure there are no extra spaces between paragraphs
    formatted_text = re.sub(r'\n+', '\n', formatted_text)

    return formatted_text


def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with open(input_path, 'r', encoding='utf-8') as file:
                input_text = file.read()

            formatted_text = process_text(input_text)

            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(formatted_text)


input_folder = 'Dataset/extracted_texts'
output_folder = 'Dataset/cleaned_texts'

process_files(input_folder, output_folder)

