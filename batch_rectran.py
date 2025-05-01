from rectran import run_translate
import asyncio, os

# Allows for large texts with line breaks to be easily parsed and garbled.
async def main():
    with open("input.txt", "r", encoding='utf8') as f:
        text_lines = f.readlines()
        print(text_lines)
        chunks = []
        batch_size = 10
        for i in range(0,len(text_lines)-1,batch_size):
            batch_string = ""
            batch_lines = (text_lines[i:i+batch_size])
            batch_string = "".join(batch_lines)
            chunks.append(batch_string)

        tasks = [asyncio.create_task(run_translate(chunk,5)) for chunk in chunks] # so it doesnt take so damn long!
        results = await asyncio.gather(*tasks)
        translated_output = "".join(results)
        
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(translated_output)
        print(translated_output)

if __name__ == "__main__":
    # Create input file if it doesn't exist
    if not os.path.exists("input.txt"):
        with open("input.txt", "w") as f:
            f.write("Hello World!")
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # stop the runtime error grrrr
    asyncio.run(main())