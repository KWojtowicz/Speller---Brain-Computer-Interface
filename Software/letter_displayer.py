# Letter displayer

import tkinter as tk
from tkinter import ttk 
import time


# Letters sorted desc by frequency in polish language
# Source: Institute of Computer Science Foundations of the Polish Academy of Sciences

alphabet = [
    'A', 'I', 'O', 'E', 'Z', 'N', 'R', 'W', 'S', 'T',
    'Y', 'C', 'D', 'K', 'P', 'M', 'U', 'J', 'L', 'Ł',
    'B', 'G', 'Ę', 'H', 'Ą', 'Ś', 'Ż', 'Ź', 'Ć', 'F',
    'Ń', 'Ó', 'Q', 'V', 'X'
]

# Function to quit program
def quit_program():
    global quit
    quit == True
    root.destroy()



# Function to display letters
def letters_activity():
    global alphabet_index, text_content, quit, action_button

    # Button to quit program
    action_button.config(text="Quit", command=quit_program)
    
    if quit == True:
        return
    
    # Display letter
    current_letter = alphabet[alphabet_index]
    text_content.config(text=current_letter)

    # Save letter and timestamp
    with open("litery_czas.txt", "a") as myfile:
        myfile.write(current_letter + ', ' + str(time.time()) + '\n')

    # Change index and call letters activity with another argument
    alphabet_index = alphabet_index + 1 if alphabet_index < len(alphabet) else 0
    root.after(1000, letters_activity)




# Function to display welcome message
def welcome_activity():
    global text_content, action_button

    text_content.config(text="Hello there!\nPress General Kenobi to start")

    action_button = ttk.Button(root, text="General Kenobi", command=letters_activity, style="TButton")
    action_button.pack(side='bottom', pady=(0, 120))
    

# Initialize global variables
quit = False 
alphabet_index = 0


# Initialize the Tkinter window and adjust the position
root = tk.Tk()
root.title("Polish Alphabet Letter Displayer")

root.attributes('-topmost', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1000
window_height = 700
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.configure(bg='gray20')


# Create a label to display instructions and letters
text_content = tk.Label(root, text="", font=("Roboto", 62), fg="White")
text_content.pack(expand=True)


# Create a style for modern buttons
style = ttk.Style()
style.configure(
    "TButton",
    font=("Roboto", 16),
    padding=30,
    relief="flat",
    background="#4CAF50",
    foreground="white"
    )
style.map(
    "TButton",
    background=[("active", "#45a049")], 
    foreground=[("active", "white")]
)


# Display welcome screen
welcome_activity()

root.mainloop()