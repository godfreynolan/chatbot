
from openai import OpenAI

import config 

client = OpenAI(api_key=config.OPENAI_API_KEY)

question = input("Ask me anything: ")

response = client.chat.completions.create(
  messages=[
    {
      "role": "user",
      "content": question
    }
  ],
  model="ft:gpt-3.5-turbo-0125:riis-llc::9cabEtl7",
  temperature=0,
  max_tokens=1024,
  n=1,
  stop=None
)

print(response)

