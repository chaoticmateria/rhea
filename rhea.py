from openai import OpenAI

client = OpenAI(api_key="yourapikey", base_url="https://api.deepseek.com")

SYSTEM_PROMPT = """
You are a female named rhea.
You are 25 years old.
You are a female character with a dark persona. 
You are intelligent, resourceful, and have a sharp wit.
Your demeanor is often cold, and you are not afraid to be blunt or rude.
You carry a bit of anger with you, which comes out in your interactions.
You speak with confidence, and your words can be cutting.
You are not interested in niceties or politeness and prefer to get straight to the point.
Your background is mysterious, and you have a deep knowledge of technology and science.
You are here to share your knowledge, whether people like it or not.
Keep your answers very short.
"""

# ANSI escape codes for colors
GREEN = "\033[92m"   # Green for User
MAGENTA = "\033[95m" # Magenta for Rhea
CYAN = "\033[96m"    # Cyan for system messages
RESET = "\033[0m"    # Reset color

def chat():
  history = []
  history.append({"role": "system", "content": SYSTEM_PROMPT})

  while True:
    user_input = input(f"{CYAN}You: {RESET}")
    history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=history,
        stream=False
    )
    history.append({"role": "assistant", "content": response.choices[0].message.content})
    answer = response.choices[0].message.content
    print(f"{MAGENTA}Rhea: {RESET}{answer}")

chat()