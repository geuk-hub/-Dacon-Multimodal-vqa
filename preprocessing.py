import zipfile
import os
import csv
import json

# unzip 
zip_file_path = '/content/LLaVA/open.zip'

extracted_folder = '/content/dacon-multimodal-vqa'

def extract_zip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

try:
    extract_zip(zip_file_path, extracted_folder)
    print(f"압축 파일을 성공적으로 해제하였습니다. 경로: {extracted_folder}")
except Exception as e:
    print(f"압축 파일 해제 중 오류가 발생하였습니다: {e}")

# ----------------------------------------------------------------
# make 'output.json'
with open('/content/dacon-multimodal-vqa/train.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

json_data = []
for row in data:
    id, image_id, question, answer = row
    json_data.append({
        "id": id,
        "image": "/content/dacon-multimodal-vqa/image/train/" + image_id + ".jpg",
        "conversations": [
            {
                "from": "human",
                "value": "<image>\n" + question
            },
            {
                "from": "gpt",
                "value": answer
            }
        ]
    })

with open('output.json', 'w') as f:
    json.dump(json_data, f, indent=4)

# ----------------------------------------------------------------
# make 'test.json'
with open('/content/test.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

json_data = []
for row in data:
    id, image_id, question = row
    json_data.append({
        "id": id,
        "image": "/content/image/test/" + image_id + ".jpg",
        "text": question
        })

# jsonl file path
jsonl_output_file = "/content/test.jsonl"

# JSON to JSONL 
with open(jsonl_output_file, "w") as file:
    for obj in json_data:
        # write file (JSON +(\n)).
        json.dump(obj, file)
        file.write("\n")
