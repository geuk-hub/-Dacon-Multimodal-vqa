import zipfile
import os
import csv
import json

# unzip 
%cd /content

!unzip -qq "/content/drive/MyDrive/data.zip"

# ----------------------------------------------------------------
# make 'output.json'
with open('/content/data/train.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

json_data = []
for row in data:
    id, image_id, question, answer = row
    json_data.append({
        "id": id,
        "image": "/content/data/image/train/" + image_id + ".jpg",
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
with open('/content/data/test.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

json_data = []
for row in data:
    id, image_id, question = row
    json_data.append({
        "id": id,
        "image": "/content/data/image/test/" + image_id + ".jpg",
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
