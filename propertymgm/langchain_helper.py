from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
# from langchain import PromptTemplate, LLMChain, OpenAI
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate 
from elevenlabs import set_api_key
import os, requests

load_dotenv(find_dotenv())
set_api_key(os.getenv('ELEVENLABS_API'))

def generate_story(complaint):
  services = """[
      {
        "service": "Water Heater Repair",
        "description": "Fixing issues with water heating units.",
        "price_range": "$100 to $200",
        "tenant_immediate_action": "please take pictures and send it to us"
        "additional_info": "Price excludes the cost of replacement parts."
      },
      {
        "service": "Sewer Line Cleaning",
        "description": "Cleaning out blocked sewer lines.",
        "price_range": "$150 to $250",
        "tenant_immediate_action": "please take pictures and send it to us",
        "additional_info": "May require camera inspection."
      },
      {
        "service": "Faucet Installation",
        "description": "Installation of new faucets in kitchen or bathroom.",
        "price_range": "$75 to $150",
        "tenant_immediate_action": "please take pictures and send it to us",
        "additional_info": "Faucet cost not included."
      },
      {
        "service": "Garbage Disposal Repair",
        "description": "Fixing issues with garbage disposal units.",
        "price_range": "$50 to $100",
        "tenant_immediate_action": "please take pictures and send it to us",
        "additional_info": "Excludes replacement unit."
      },
      {
        "service": "Gas Line Repair",
        "description": "Repairing minor leaks in gas lines.",
        "price_range": "$150 to $300",
        "tenant_immediate_action": "please take pictures and send it to us",
        "additional_info": "Does not include cost of emergency services."
      },
      {
        "service": "Drain Cleaning",
        "description": "Clearing blocked drains in sinks or bathtubs.",
        "price_range": "$50 to $100",
        "tenant_immediate_action": "please take pictures and send it to us",
        "additional_info": "Extra charges for persistent blockages."
      },
      {
        "service": "Shower Installation",
        "description": "Installation of new shower heads or systems.",
        "price_range": "$100 to $200",
        "tenant_immediate_action": "please take pictures and send it to us"
        "additional_info": "Shower unit cost not included."
      },
      {
        "service": "Toilet Fix",
        "description": "Fixing common toilet problems",
        "price_range": "from $150 to $300",
        "tenant_immediate_action": "please take pictures and send it to us",
        "additional_info": "Toilet unit cost not included."
      },
      {
        "service": "Pipe Insulation",
        "description": "Insulating exposed pipes to prevent freezing.",
        "price_range": "$50 to $100",
        "tenant_immediate_action": "please take pictures and send it to us"
        "additional_info": "Material costs may vary."
      },
      {
        "service": "Emergency Services",
        "description": "24/7 emergency plumbing services.",
        "price_range": "$200 to $400",
        "additional_info": "Additional fees for holidays and weekends."
      }
  ]"""
  template = """You are a property manager; upon receiving a complaint from a tenant, you need to comfort the tenant by saying that you will fix the issue as soon as possible. 
  Recommend the service provider to fix the issue, including the price and immediate action the tenant need to take. The list of service providers are provided in the below service section.
  Please keep your answer short, no more than 80 words.
  SERVICE: {services}
  COMPLAINT: {complaint}
  ANSWER:
  """
  prompt = PromptTemplate(template=template, input_variables=["services", "complaint"])
  prompt.format(services=services, complaint=complaint)
  story_llm = LLMChain(llm=ChatOpenAI(model_name="gpt-4", temperature=1), prompt=prompt, verbose=True)
  story = story_llm.predict(services=services, complaint=complaint)
  print(story)
  return story

def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"""Bearer {os.getenv("HUGGINGFACE_API")}"""}
    payload = {"inputs": message}
    response = requests.post(API_URL, headers=headers, json=payload)
    with open('answer.mp3', 'wb') as file:
        file.write(response.content)

def elevenlabvoice (message):
  CHUNK_SIZE = 1024
  url = f"https://api.elevenlabs.io/v1/text-to-speech/{os.getenv('VOICE_ID')}"

  headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": os.getenv('ELEVANLABS_API')
  }

  data = {
    "text": message,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.5
    }
  }

  response = requests.post(url, json=data, headers=headers)
  with open('output.mp3', 'wb') as f:
      for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
          if chunk:
              f.write(chunk)