from openai import OpenAI
import config 

client = OpenAI(api_key=config.OPENAI_API_KEY)

file_id = "file-sO8gDViouzBHiKefhzqip2ko"

ft_job = client.fine_tuning.jobs.create(
  training_file=file_id,
  model="gpt-3.5-turbo"
)

print("Fine Tune Job has been created with id ", ft_job.id)

events = client.fine_tuning.jobs.list_events(fine_tuning_job_id=ft_job.id, limit=10)

print(events)

