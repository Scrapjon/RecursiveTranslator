from googletrans import Translator
from googletrans.constants import LANGUAGES
import random, asyncio, tkinter


async def __main__():
    while True:
        translator=Translator()
        text_input = input("What do you want translated?\nType 'exit' to quit.\n")
        if text_input == "exit":
            break
        elif text_input:
            for i in range(5):
                text_input = await translator.translate(text=text_input, dest=random.choice(list(LANGUAGES.values())))
                text_input = text_input.text
                print(f"Iteration {i}")
            response = await translator.translate(text=text_input, dest="English")
            print(response.text)
        print("\n")


    


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # stop the runtime error grrrr
    asyncio.run(__main__())