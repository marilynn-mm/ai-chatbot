from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_APIKEY")
)

def chat_with_gpt():
    print("Welcome to the Terminal Chatbot!")
    print("Type 'exit' to end the chat.\n")

    # Maintain conversation context
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        # Get user input
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Append user input to the conversation
        conversation.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": "Say this is a test",
                }],
                model="gpt-4o-mini",
            )

            # Get the assistant's response
            assistant_response = response.choices[0].message.content
            print(f"Chatbot: {assistant_response}")

            # Add the assistant's response to the conversation
            conversation.append({"role": "assistant", "content": assistant_response})

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_gpt()
