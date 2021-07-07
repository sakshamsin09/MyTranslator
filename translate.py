from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
root = Tk()
root.geometry('800x300+150+100')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title("Language Translator")

Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()

Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=30,y=60)

Input_text = Text(root,font = 'arial 10', height = 10, wrap = WORD, padx=3, pady=5, width = 40)
Input_text.place(x=25,y = 100)

Label(root,text ="Output", font = 'arial 15 bold', bg ='white smoke').place(x=490,y=60)

Output_text = Text(root,font = 'arial 10', height = 10, wrap = WORD, padx=3, pady= 5, width =40)
Output_text.place(x = 480 , y = 100)
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width =20)
src_lang.place(x=150,y=60)
src_lang.set('english')

dest_lang = ttk.Combobox(root, values= language, width =20)
dest_lang.place(x=590,y=60)
dest_lang.set('hindi')
def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END), dest = dest_lang.get(), src = src_lang.get())

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1',
                   activebackground = 'sky blue')
trans_btn.place(x = 350, y= 180 )
def reverse():
    str = src_lang.get()
    src_lang.set(dest_lang.get())
    dest_lang.set(str)
imgreverse = PhotoImage(file='reverse.png')
imgreverse = imgreverse.subsample(13,17)
reverse_btn = Button(root ,font = 'arial 12 bold',pady = 5,command = reverse , bg = 'royal blue1', activebackground = 'sky blue',
                     image=imgreverse)
reverse_btn.place(x=370, y=60)
root.mainloop()