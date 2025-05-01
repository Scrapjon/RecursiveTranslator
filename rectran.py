from googletrans import Translator
from googletrans.constants import LANGUAGES
import random, asyncio


async def main():
    while True:
        text_input = input("What do you want translated?\nType 'exit' to quit.\n")
        if text_input == "exit":
            break
        elif text_input:
            translated_output = await run_translate(text_input, 10)
            print(translated_output + "/n")

async def run_translate(text_input: str, num: int) -> str:
    translator = Translator()
    for i in range(num):
        try:
            language = random.choice(list(LANGUAGES.values()))
            text_input = await translator.translate(text=text_input, dest=language)
            text_input = text_input.text
            print(f"Iteration {i}, Translating to language: {language}")
        except Exception as e:
            print(f"Iteration failed due to: {e}")
    response = await translator.translate(text=text_input, dest="en")
    return response.text
    


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # stop the runtime error grrrr
    asyncio.run(main())