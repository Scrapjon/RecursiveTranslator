from tkinter import *
from tkinter import ttk
import rectran, batch_rectran, asyncio

def main():
    closing = False # is application closing

    root = Tk()
    root.title("Recursive Translator")
    root.geometry("600x300")

    # Style
    font_main = ("Helvetica", 12)
    font_label = ("Helvetica", 11)
    font_output = ("Helvetica", 12, "italic")

    

    # Frame and layout
    frame = ttk.Frame(root, padding="20")
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Variables
    text_input = StringVar()
    iteration_input = IntVar(value=1)
    translated_output = StringVar()

    # Widgets
    ttk.Label(frame, text="Input Text:", font=font_label).grid(column=0, row=0, sticky=W)
    ttk.Entry(frame, width=40, font=font_main, textvariable=text_input).grid(column=1, row=0, columnspan=2, sticky=(W, E))

    ttk.Label(frame, text="Iterations:", font=font_label).grid(column=0, row=1, sticky=W)
    ttk.Entry(frame, width=10, font=font_main, textvariable=iteration_input).grid(column=1, row=1, sticky=W)

    ttk.Label(frame, text="Translated Output:", font=font_label).grid(column=0, row=2, sticky=NW)
    ttk.Label(frame, textvariable=translated_output, font=font_output, wraplength=400, justify=LEFT).grid(column=1, row=2, columnspan=2, sticky=(W, E))
    progress = ttk.Progressbar(frame, length=300, mode="determinate", maximum=100)
    progress.grid(column=0, row=4, columnspan=2, pady=10)

    async def handle_translate():
        input_text = text_input.get()
        iterations = iteration_input.get()
        result = await rectran.run_translate(input_text, iterations, update_progress)
        translated_output.set(result)
    def update_progress(current, total):
        percent = int((current / total) * 100)
        progress['value'] = percent
        root.update_idletasks()
    def translate():
        asyncio.create_task(handle_translate())
    def copy_to_clipboard():
        output = translated_output.get()
        root.clipboard_clear()
        root.clipboard_append(output)
        root.update()
    def on_close():
        global closing
        closing = True
        root.destroy()  
    root.protocol("WM_DELETE_WINDOW", on_close)
    # Button
    ttk.Button(frame, text="Translate!", command=translate).grid(column=1, row=3, pady=15, sticky=W)
    ttk.Button(frame, text="Copy to clipboard", command=copy_to_clipboard).grid(column=0, row=3, pady=15, sticky=W)

    # Padding
    for child in frame.winfo_children():
        child.grid_configure(padx=10, pady=5)

    # Bind Enter key to trigger translation
    root.bind("<Return>", lambda event: translate())

    async def tkinter_loop():
        while not closing:
            try:
                root.update()
            except TclError:
                break
            await asyncio.sleep(0.01)

    asyncio.run(tkinter_loop()) # stupid bandaid smh

    

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # stop the runtime error grrrr
    main()