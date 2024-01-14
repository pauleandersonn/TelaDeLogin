import customtkinter
from tkinter import RIGHT, PhotoImage


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sisitema de Login")


janela.resizable(False, False)


img = "PhotoImage" (file = "C:\Users\Pauleanderson\Documents\VS CODE\TELA DE LOGIN PYTHON\imagem.png")	




label_img = customtkinter.CTkLabel(master = janela,imagem=img)
label_img.place(x=5, y=65)

#frame

frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#FRAME WIDGETS
label = customtkinter.CTkLabel(master=frame, text="Sitema de login")
label.place(x=25, y=5)



janela.mainloop()
