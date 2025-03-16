import pandas as pd
from util import find_paragraph_refs, process_data
train_data_path = "C:/Clemson/Info Retreival/Project_Phase2/medical_data/train.csv"
test_data_path = "C:/Clemson/Info Retreival/Project_Phase2/medical_data/test.csv"
train = pd.read_csv(train_data_path)
test = pd.read_csv(test_data_path, nrows=1000)
test.to_csv('test.csv', index=False)

# train_paragraphs = find_paragraph_refs(train.summary)
# processed_data = process_data(train, train_paragraphs)
# pd.to_csv("paragraphs_train.csv", index=False)
# with open(r"C:\Clemson\Info Retreival\Project_Phase2\medical_data\train.txt", 'r') as file:
#     lines = file.readlines()

# import pandas as pd
# import re

# def convert_pubmed_to_civilsum(output_path):
#     """
#     Converts PubMed RCT dataset to CivilSum format
#     :param input_path: Path to .txt file (e.g., "train.txt")
#     :param output_path: Output CSV path (e.g., "pubmed_civilsum.csv")
#     """
#     with open(r"C:\Clemson\Info Retreival\Project_Phase2\medical_data\test.txt", encoding="utf-8") as f:
#         content = f.read()

#     # Split articles using ###PMID delimiter
#     articles = re.split(r'###(\d+)\n', content)[1:]  # Returns [PMID1, content1, PMID2, content2...]
    
#     records = []
#     for i in range(0, len(articles), 2):
#         if i+1 >= len(articles):
#             break  # Handle odd splits
            
#         doc_id = articles[i].strip()
#         article_content = articles[i+1]
        
#         # Process sections
#         sections = []
#         summary = ""
#         for line in article_content.split('\n'):
#             if not line.strip():
#                 continue
                
#             # Split section header from content
#             if '\t' in line:
#                 section, text = line.split('\t', 1)
#                 sections.append(f"{section}\t{text.strip()}")
                
#                 # Use CONCLUSIONS section as summary
#                 if section.strip().upper() == "CONCLUSIONS":
#                     summary = text.strip()
        
#         # Fallback if no CONCLUSIONS section
#         if not summary and sections:
#             summary = sections[-1].split('\t', 1)[-1]  # Use last section
        
#         records.append({
#             "doc_id": doc_id,
#             "text": "\n".join(sections),
#             "summary": summary
#         })

#     # Save to CSV
#     df = pd.DataFrame(records)
#     df.to_csv(output_path, index=False)
#     print(f"Converted {len(records)} articles to {output_path}")

# # Usage example
# convert_pubmed_to_civilsum(  # Path to your .txt file
#     output_path="medical_data/test.csv"
# )