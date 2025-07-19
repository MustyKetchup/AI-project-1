#Langchain is a high-level framework, used for building AI applications. 
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
#langgraph helps us make AI - agents
from langgraph.prebuilt import create_react_agent
#dotenv lets us load enviorment files
from dotenv import load_dotenv

load_dotenv()
#"""""" is a doc , it explains the llm, what it is by a description. 
@tool
def calculator(a:float,b:float)-> str:
    """Useful for performing basic aritmeric calculations with numbers """
    print("Calculation tool has been called")
    return f"the sum of {a} and {b} is {a+b}"

@tool
def say_hello(name:str)-> str:
    """Useful for greeting a user """
    print("Name tool has been called")
    return f"Hello there {name}, reallu moce to meet you!"




def main():
    model = ChatOpenAI(temperature=0)
    
    #we can feed our tools into this list
    tools = [calculator]
    agent_executor = create_react_agent(model, tools)
    
    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()
        
if __name__ == "__main__":
    main()
