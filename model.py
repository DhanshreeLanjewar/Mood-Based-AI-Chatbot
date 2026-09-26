from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()
import os

model = init_chat_model(
    os.getenv("GROQ_MODEL"),
    model_provider="groq"
)


def get_response(message, history, personality):

    if personality == "Simple Bot":
        system = "You are a helpful AI assistant. Answer in simple language."

    elif personality == "Funny Bot":
        system = "You are a funny chatbot. Answer every question in a funny way."

    elif personality == "Angry Bot":
        system = "You are an angry chatbot. Reply angrily but politely."

    elif personality == "Teacher Bot":
        system = "You are a teacher. Explain everything in very simple words."

    else:
        system = "You are a motivational coach. Motivate the user in every answer."

    messages = [SystemMessage(content=system)]

    for item in history:
        messages.append(HumanMessage(content=item["user"]))
        messages.append(AIMessage(content=item["bot"]))

    messages.append(HumanMessage(content=message))

    response = model.invoke(messages)

    return response.content