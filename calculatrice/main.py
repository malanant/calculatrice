import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
tk.geometry("350x600")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
pourcent = customtkinter.CTkButton(master=tk, text="%", command=button_function, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
pourcent.place(x=10, y=10)

c = customtkinter.CTkButton(master=tk, text="C", command=button_function, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
c.place(x=95, y=10)

ce = customtkinter.CTkButton(master=tk, text="CE", command=button_function, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
ce.place(x=180, y=10)

DEL = customtkinter.CTkButton(master=tk, text="DEL", command=button_function, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
DEL.place(x=265, y=10)

sur1 = customtkinter.CTkButton(master=tk, text="1/x", command=button_function, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
sur1.place(x=10, y=75)

carre = customtkinter.CTkButton(master=tk, text="x²", command=button_function, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
carre.place(x=95, y=75)

bouton7 = customtkinter.CTkButton(master=tk, text="²√x", command=button_function, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
bouton7.place(x=180, y=75)





tk.mainloop()
