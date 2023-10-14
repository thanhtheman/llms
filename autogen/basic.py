from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import os
load_dotenv()

config_list = [{
    "model": "gpt-4",
    "api_key": os.getenv("OPENAI_API_KEY"),
}]

assistant = AssistantAgent("assistant",llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir":"coding"})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")

