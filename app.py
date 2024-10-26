import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import pygame
import os
from tkinter import messagebox

# Variables to hold file paths
input_audio_path = ""
output_audio_path = ""


# Function to browse and select an audio file
def browse_audio_file():
    global input_audio_path
    input_audio_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.wav *.mp3")]
    )


# Function to reverse the selected audio file and save it
def reverse_audio():
    global input_audio_path, output_audio_path

    if input_audio_path:  # Check if a file is selected
        try:
            audio = AudioSegment.from_file(input_audio_path)
            reversed_audio = audio.reverse()  # Reverse the audio
            output_audio_path = "reversed_" + os.path.basename(input_audio_path)
            reversed_audio.export(output_audio_path, format="wav")
            messagebox.showinfo(
                "Success", "Audio reversed and saved as " + output_audio_path
            )
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))
    else:
        messagebox.showwarning("Warning", "Please select an audio file first.")


# Function to play the original audio file
def play_original_audio():
    global input_audio_path
    if input_audio_path:
        pygame.mixer.init()
        pygame.mixer.music.load(input_audio_path)
        pygame.mixer.music.play()


# Function to play the reversed audio file
def play_reversed_audio():
    global output_audio_path
    if output_audio_path:
        pygame.mixer.init()
        pygame.mixer.music.load(output_audio_path)
        pygame.mixer.music.play()


# Main GUI setup
root = tk.Tk()
root.title("Reversal")

# Set window icon and background color
icon_path = "image\icon16.ico"
root.iconbitmap(icon_path)
root.config(bg="#2A363B")

# Frame for file selection
frame1 = tk.Frame(root, bg="#99B898", borderwidth=2, relief="ridge")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
label = tk.Label(frame1, bg="#99B898", text="Select an audio file to reverse:")
label.grid(row=0, column=0, pady=10, padx=5, sticky="nsew")
browse_button = tk.Button(
    frame1, bg="#FECEA8", text="Browse", command=browse_audio_file
)
browse_button.grid(row=1, column=0, padx=20, sticky="nsew")

# Frame for reverse button
frame3 = tk.Frame(root, bg="#99B898", borderwidth=2, relief="ridge")
frame3.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
reverse_button = tk.Button(
    frame3, bg="#E84A5F", text="Reverse Audio", command=reverse_audio
)
reverse_button.grid(row=0, column=0, padx=5, pady=20)

# Frame for play buttons
frame2 = tk.Frame(root, bg="#99B898", borderwidth=2, relief="ridge")
frame2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
play_original_button = tk.Button(
    frame2, bg="#FF847C", text="Play Original", command=play_original_audio
)
play_original_button.grid(row=0, column=0, pady=20, padx=5, sticky="nsew")
play_reversed_button = tk.Button(
    frame2, bg="#FF847C", text="Play Reversed", command=play_reversed_audio
)
play_reversed_button.grid(row=0, column=1, pady=20, padx=5, sticky="nsew")

# Configure grid to center frames in the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame1.grid_rowconfigure(0, weight=1)
frame3.grid_rowconfigure(0, weight=1)
frame2.grid_rowconfigure(0, weight=1)

root.mainloop()
