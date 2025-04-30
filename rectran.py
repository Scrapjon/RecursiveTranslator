from googletrans import Translator
from googletrans.constants import LANGUAGES
import random, asyncio


async def __main__():
    while True:
        text_input = input("What do you want translated?\nType 'exit' to quit.\n")
        if text_input == "exit":
            break
        elif text_input:
            translated_output = await run_translate(text_input, 10)
            print(translated_output)
        print("\n")

async def run_translate(text_input: str, num: int) -> str:
    translator=Translator()
    for i in range(num):
        text_input = await translator.translate(text=text_input, dest=random.choice(list(LANGUAGES.values())))
        text_input = text_input.text
        print(f"Iteration {i}")
    response = await translator.translate(text=text_input, dest="English")
    return response.text
    


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # stop the runtime error grrrr
    asyncio.run(__main__())