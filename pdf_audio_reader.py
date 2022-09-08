from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3


def Application(root):
    root.geometry('{}x{}'.format(700, 600))
    root.resizable(width=False, height=False)
    root.title("PDF TO AUDIO")
    root.configure(bg="light grey")
    global rate, male, female

    #frame1
    frame1 = Frame(root, width=500, height=200, background="#7800FF")
    frame1.pack(side="top", fill="both")

    #frame2
    frame2 = Frame(root, width=500, height=450, background="light grey")
    frame2.pack(side="top", fill="y")

    #frame1 widgets
    name1 = Label(frame1, text="PDF TO AUDIO", foreground="light grey", background="#7800FF", font="Arial 28 bold")
    name1.pack(pady=25)



    #frame2 widgets
    btn = Button(frame2, text="Select PDF file", activeforeground="#D7B3FF", command=extract_text, padx="70", pady="10",
                 foreground="white", background="#7800FF", font="Arial 12")
    btn.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(frame2, text="Enter the rate of speech", foreground="#7800FF", background="light grey", font="Arial 12")
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=W)

    rate = Entry(frame2, foreground="black", background="white", font="Arial 12")
    rate.grid(row=1, column=1, padx=30, pady=15, sticky=W)

    voice_text = Label(frame2, text="Select voice", background="light grey", font="Arial 12", fg="#7800FF")
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)

    male = IntVar()
    maleOpt = Checkbutton(frame2, text="Male", background="light grey", variable=male, onvalue=1, offvalue=0,
                          foreground="#7800FF")
    maleOpt.grid(row=2, column=1, pady=0, padx=30, sticky=W)

    female =IntVar()
    femaleOpt = Checkbutton(frame2, text="Female", background="light grey", variable=female, onvalue=1, offvalue=0,
                            foreground="#7800FF")
    femaleOpt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

    submitBtn = Button(frame2, text="Play PDF file", command=speak_text, activeforeground="#D7B3FF", padx="60", pady="10",
                       foreground="white", background="#7800FF", font="Arial 12")
    submitBtn.grid(row=4, column=0, pady=65)

    stopBtn =Button(frame2, text="Stop playing", command=stop_speak, activeforeground="#D7B3FF", padx="60", pady="10",
                       foreground="white", background="#7800FF", font="Arial 12")
    stopBtn.grid(row=4, column=1, pady=65)


def extract_text():
    file = filedialog.askopenfile(parent=root, mode="rb", title="Choose a PDF file")
    if file != None:
        pdfReader = PyPDF2.PdfFileReader(file)
        global text_extracted
        text_extracted = ""
        for pageNum in range(pdfReader.numPages):
            pageObject = pdfReader.getPage(pageNum)
            text_extracted += pageObject.extract_text()
        file.close()


def speak_text():
    global rate
    global male
    global female
    rate =int(rate.get())
    engine.setProperty('rate', rate)
    male = int(male.get())
    female = int(female.get())
    all_voices = engine.getProperty('voices')
    male_voices = all_voices[0].id
    female_voices = all_voices[1].id
    if (male==1 and female==1) or (male==0 and female==0):
        engine.setProperty('voice', male_voices)
    elif(male==0 and female==1):
        engine.setProperty('voice', female_voices)
    else:
        engine.setProperty('voice', male_voices)
    engine.say(text_extracted)
    engine.runAndWait()

def  stop_speak():
    engine.stop()


if __name__ == "__main__":
    my_text, rate, male, female = "", 100, 0, 0
    engine = pyttsx3.init()
    root = Tk()
    Application(root)
    root.mainloop()










