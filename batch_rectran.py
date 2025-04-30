from rectran import run_translate
import asyncio, os

# Allows for large texts with line breaks to be easily parsed and garbled.
async def __main__():
    with open("input.txt", "r") as f:
        text_input = f.read()
        print(text_input)
        translated_output = await run_translate(text_input, 10)
    with open("output.txt", "w") as f:
        f.write(translated_output)
        print(translated_output)

if __name__ == "__main__":
    # Create input file if it doesn't exist
    if not os.path.exists("input.txt"):
        with open("input.txt", "w") as f:
            f.write("Hello World!")
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # stop the runtime error grrrr
    asyncio.run(__main__())