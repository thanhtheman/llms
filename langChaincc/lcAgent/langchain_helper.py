from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def generate_pet_name(animal_type, pet_color):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.7)
    prompt_template_name = PromptTemplate(
        template="I have a {animal_type} pet and I want a cute name for it. It is {pet_color}. Please give me 5 namesLL",
        input_variables=["animal_type", "pet_color"])

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain.predict(animal_type=animal_type, pet_color=pet_color)   
    return response

def langchain_agent():
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.7)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, tools=tools, llm=llm, verbose=True)
    result = agent.run("What is the average age of a dog? Multiply the age by 3")
    print(result)

    
if __name__ == "__main__":
    langchain_agent()