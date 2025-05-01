from tkinter import *
from tkinter import ttk
import rectran, batch_rectran, asyncio

def main():

    def translate():
        return asyncio.run(rectran.run_translate(text_input.get(), iteration_input.get()))

    root = Tk()
    root.title("Recursive Translator")
    frame = ttk.Frame(root, padding="12 12 12 12")
    frame.grid(column=0, row=0, sticky=(N,W,E,S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0,weight=1)

    text_input = StringVar()
    
    text_input_entry = ttk.Entry(frame, width=7, textvariable=text_input)
    text_input_entry.grid(column=2, row=1, sticky=(W,E))

    iteration_input = IntVar()
    iteration_input_entry = ttk.Entry(frame, width=7, textvariable=iteration_input)
    iteration_input_entry.grid(column=4, row=1, sticky=(W,E))

    translated_output = StringVar()
    ttk.Label(frame, textvariable=translated_output).grid(column=2, row=2, sticky=(W,E))

    ttk.Button(frame, text="Translate!", command=translate).grid(column=3, row=3, sticky=W)

    ttk.Label(frame, text="Input Text:").grid(column=3, row=2, sticky=(W,E))
    ttk.Label(frame, text="Output Text:").grid(column=3, row=2, sticky=(W))
    ttk.Label(frame, text="Number of Iterations:").grid(column=4, row=2, sticky=(W,E))

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)
    
    text_input_entry.focus()
    root.bind("<Return>", translate)

    root.mainloop()

    

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # stop the runtime error grrrr
    main()