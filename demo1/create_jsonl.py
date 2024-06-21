import json

input_jsonl_file = "input_data.jsonl"

input_json_file = "input_data.json"


with open(input_json_file, 'r') as json_file:
  data = json.load(json_file)

# Write to a JSONL file
with open(input_jsonl_file, 'w') as jsonl_file:
  for entry in data:
    jsonl_file.write(json.dumps(entry) + '\n')

print("Conversion to JSONL complete.")