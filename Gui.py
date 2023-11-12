import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import time
import threading
from PIL import Image, ImageTk  # Import Pillow


def navigate_to_project_folder():
    project_folder = filedialog.askdirectory()
    if project_folder:
        os.chdir(project_folder)
        project_folder_label.config(text=f"Current Project Folder: {project_folder}", fg="blue", font=("Helvetica", 12))

def activate_environment():
    subprocess.run(["conda", "activate", ".\\env"])
    environment_label.config(text="Environment Activated", fg="green", font=("Helvetica", 12, "bold"))

def run_project():
    project_status_label.config(text="Project Running", fg="red")
    run_button.config(state=tk.DISABLED)  # Disable the "Run Project" button

    def run_project_command():
        # Change the current directory to the 'yolov5' folder
        yolov5_folder = os.path.join(os.getcwd(), 'yolov5')
        os.chdir(yolov5_folder)
        subprocess.Popen(["python", "run.py"])
        time.sleep(2)  # Sleep for a while to simulate the project running
        project_status_label.config(text="Project Running...", fg="red")
        run_button.after(500, animate_running_dots)

    def animate_running_dots():
        current_text = project_status_label.cget("text")
        if "..." in current_text:
            new_text = "Project Running"
        else:
            new_text = current_text + "."
        project_status_label.config(text=new_text, fg="red")
        run_button.after(500, animate_running_dots)

    # Start the project in a separate thread to allow animation
    threading.Thread(target=run_project_command).start()

# Create the main application window
root = tk.Tk()
root.title("Sign Language Detection GUI")
root.geometry("800x600")  # Set the window size
root.configure(bg="white")


content_frame = tk.Frame(root, bg="white")
content_frame.place(relx=0.5, rely=0.5, anchor="center")


# Load the background image
#bg_image = Image.open("background/.jpg")  # Replace with your image file path
#bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image covering the entire window
#bg_label = tk.Label(root, image=bg_photo)
#bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create labels with updated styles
heading = tk.Label(content_frame, text="Real-Time Sign Language Detection", font=("Helvetica", 40, "bold"), fg="black", bg="white")
Folder_label = tk.Label(content_frame, text="Select Folder:", font=("Helvetica", 14, "bold"), fg="purple", bg="white")
project_folder_label = tk.Label(content_frame, text="Current Project Folder: None", font=("Helvetica", 12), fg="black", bg="white")
Select_env_label = tk.Label(content_frame, text="Activate Environment:", font=("Helvetica", 14, "bold"), fg="orange", bg="white")
environment_label = tk.Label(content_frame, text="Environment Not Activated", font=("Helvetica", 12), fg="black", bg="white")
projectrun_label = tk.Label(content_frame, text="Run Project:", font=("Helvetica", 14, "bold"), fg="red", bg="white")
project_status_label = tk.Label(content_frame, text="Project Status: Not Running", font=("Helvetica", 12), fg="black", bg="white")

# Create buttons with updated styles
browse_button = tk.Button(content_frame, text="Browse Project Folder", command=navigate_to_project_folder, bg="purple", fg="white")
activate_button = tk.Button(content_frame, text="Activate Environment", command=activate_environment, bg="orange", fg="white")
run_button = tk.Button(content_frame, text="Run Project", command=run_project, bg="red", fg="white")

# Arrange widgets in the layout
heading.pack()
Folder_label.pack()
browse_button.pack()
project_folder_label.pack()
Select_env_label.pack()
activate_button.pack()
environment_label.pack()
projectrun_label.pack()
run_button.pack()
project_status_label.pack()

# Start the Tkinter main loop
root.mainloop()
