import webview
import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

# Create the main application window
root = tk.Tk()
root.title('Eaglercraft Launcher')
root.geometry("800x600")  # Set window size

# Define client options
options = [
    "Choose Eaglercraft Client",
    "Eaglercraft 1.3",
    "Eaglercraft 1.5.2",
    "Eaglercraft 1.5.2 (Recent Client)",
    "Eaglercraft 1.5.2 (Precision Client)",
    "Eaglercraft 1.8.8",
    'Eaglercraft 1.8.8 (Fuchsiax Client)',
    'Eaglercraft 1.14'
]

# Define the URLs for each client
clients = {
    'Eaglercraft 1.3': 'https://mopnop.github.io/eaglercraft-singleplayer/',
    'Eaglercraft 1.5.2': 'https://html5gfiles.github.io/minecraft-15/',
    'Eaglercraft 1.5.2 (Recent Client)': 'https://resent.vercel.app',
    'Eaglercraft 1.5.2 (Precision Client)': 'https://html5gfiles.github.io/precision-client',
    'Eaglercraft 1.8.8': 'https://eaglercraft.q13x.com',
    'Eaglercraft 1.8.8 (Fuchsiax Client)': 'https://elidoesexploits.github.io/eaglercraft/FuschiaX/',
    'Eaglercraft 1.14': 'https://eaglerdevs.github.io/EaglerCraft/'
}

# Create a ThemedStyle for ttk widgets
style = ThemedStyle(root)
style.set_theme("plastik")  # You can choose different themes

# Create a label for the title with a transition effect
title_label = ttk.Label(root, text='Welcome to the Eaglercraft Launcher', font=("Arial", 20, "bold"))
title_label.pack(pady=20)
title_label.configure(foreground="blue")  # Initial color

def change_title_color():
    title_label.configure(foreground="red")  # Transition to red color

root.after(2000, change_title_color)  # Change color after 2 seconds (adjust timing as needed)

# Create a label for client selection
client_label = ttk.Label(root, text='Select a Eaglercraft Client:', font=("Arial", 14))
client_label.pack()

# Create a dropdown menu with a transition effect
clicked = StringVar()
clicked.set(options[0])

drop = ttk.Combobox(root, textvariable=clicked, values=options, font=("Arial", 12))
drop.pack(pady=10)

# Function to launch the selected client with a transition effect
def launch():
    chosen_client = clicked.get()
    if chosen_client != options[0]:
        root.destroy()
        url = clients[chosen_client]
        webview.create_window(chosen_client, url)
        webview.start()
    else:
        # Display an error message if "Choose Eaglercraft Client" is selected
        error_label = ttk.Label(root, text="Please select a valid Eaglercraft client.", foreground="red", font=("Arial", 12))
        error_label.pack(pady=10)

# Create a launch button with a transition effect
launch_button = ttk.Button(root, text="Launch Eaglercraft Client", command=launch, style='TButton')
launch_button.pack(pady=20)

# Function to exit the application with a transition effect
def exit_launcher():
    root.destroy()

# Create an Exit button with a transition effect
exit_button = ttk.Button(root, text="Exit", command=exit_launcher, style='TButton')
exit_button.pack(pady=10)

# Run the main application loop
root.mainloop()
