import customtkinter
import pygame
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("800x480")
app.title("Arthus Client")
customtkinter.set_widget_scaling(1.5)
customtkinter.set_window_scaling(1)
customtkinter.set_spacing_scaling(1)

app.iconbitmap("icon.ico")

# Display text that says 'Arthus Client'
label = customtkinter.CTkLabel(app, text="Arthus Client", text_font=("Arial", 25))
label.pack()

# Create a music button that plays music when clicked

def playmusic():
    pygame.mixer.init()
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        musicbutton.configure(text="🔇")
    else:
        pygame.mixer.music.load("music/trucdeouf.mp3")
        pygame.mixer.music.play()
        musicbutton.configure(text="🔊")

musicbutton = customtkinter.CTkButton(app, text="🔇", command=playmusic, width=5, height=5)
musicbutton.place(relx=0.9, rely=0.1, anchor="center")

# Create an option menu to change version of Nite
def change_version(niteversion):
    with open("version.txt", "w") as f:
        f.write(niteversion)

versionmenu = customtkinter.CTkOptionMenu(app, values=["1.7", "1.8", "1.12", "1.16", "1.17", "1.18"], command=change_version)
versionmenu.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

# Create a button that start ./libs/Nite.py
def start_nite():
    try:
        with open("version.txt", "r") as f:
            version = f.read()
    except:
        version = "1.8"
    if customserver.get() == 1:
        server = customserverentry.get()
        with open("server.txt", "w") as f:
            f.write(server)
    else:
        server = ""
    os.system(f"python ./libs/Nite.py {version} {server}")

startbutton = customtkinter.CTkButton(app, text="Starthus", command=start_nite)
startbutton.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

# Create a checkbox to enter a custom server
def enter_custom_server():
    if customserver.get() == 1:
        customserverentry.configure(state="normal")
        customserverentry.focus()
    else:
        customserverentry.configure(state="disabled")
    # Write the input in a file
    

customserver = customtkinter.IntVar()
customserver.set(0)
customserverentry = customtkinter.CTkEntry(app, state="disabled")
customserverentry.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)
customservercheckbox = customtkinter.CTkCheckBox(app, text="Custom server", variable=customserver, command=enter_custom_server)
customservercheckbox.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER)

# Set the default values
try:
    with open("server.txt", "r") as f:
        server = f.read()
        customserver.set(1)
        customserverentry.configure(state="normal")
        customserverentry.insert(0, server)
except:
    pass
try:
    with open("version.txt", "r") as f:
        version = f.read()
        versionmenu.set(version)
except:
    pass

# Create a button to switch between dark and light mode
if customtkinter.get_appearance_mode() == "System":
    mode = "system"
elif customtkinter.get_appearance_mode() == "Dark":
    mode = "light"
elif customtkinter.get_appearance_mode() == "Light":
    mode = "dark"

def change_mode():
    if customtkinter.get_appearance_mode() == "Dark":
        customtkinter.set_appearance_mode("light")
        mode = "dark"
    elif customtkinter.get_appearance_mode() == "Light":
        customtkinter.set_appearance_mode("dark")
        mode = "light"
    modebutton.configure(text=f"Switch to {mode} mode")

modebutton = customtkinter.CTkButton(master=app, text=f"Switch to {mode} mode", command=change_mode)
modebutton.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

# Start the application
app.mainloop()