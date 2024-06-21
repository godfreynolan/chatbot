import config
from openai import OpenAI
client = OpenAI(api_key=config.OPENAI_API_KEY)

input_jsonl_file = "input_data.jsonl"

file = client.files.create(
  file=open(input_jsonl_file, "rb"),
  purpose="fine-tune"
)

print("File has been uploaded to OpenAI with id ", file.id)

