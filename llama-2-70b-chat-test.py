import replicate
import os
from dotenv import load_dotenv

load_dotenv()


os.environ['REPLICATE_API_TOKEN'] = os.getenv("REPLICATE_API_TOKEN")

# special tokens used by llama 2 chat
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"


input = {
    "top_p": 1,
    "prompt": "Can you write a poem about open source machine learning? Let's make it in the style of E. E. Cummings.",
    "temperature": 0.1,
    "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
    "max_new_tokens": 50
}

for event in replicate.stream(
    "meta/llama-2-70b-chat",
    input=input
):
    print(event, end="")