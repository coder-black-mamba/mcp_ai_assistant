import asyncio
from mcp_use import MCPClient, MCPAgent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os



load_dotenv()

async def main():
    # Create client with multiple servers
    client = MCPClient.from_config_file("mcp_config.json")

    # Create agent with the client
    # api_key=input("Enter your OpenAI API key: ")
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    agent = MCPAgent(
        llm = ChatGroq( model="llama-3.3-70b-versatile", temperature=0.5),
        client=client
    )

    try:
        # create a question answer sytem eith user 
        # and system prompts
        print("===================== Welcome to the MCP ai assistnat Agent! =====================")
        while True:
            user_input = input("You : ")
            if user_input.lower() == "exit":
                break
            # Run a query that uses tools from multiple servers
            if user_input:
                result = await agent.run(user_input)
                print(result)
            else:
                print("Please enter a valid input.")
        # user_input = input("You : ")
        # # Run a query that uses tools from multiple servers
        # result = await agent.run(
        #     "Search for a nice place to stay in Barcelona on Airbnb, "
        #     "then use Google to find nearby restaurants and attractions."
        # )
        # print(result)
    finally:
        # Clean up all sessions
        await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())