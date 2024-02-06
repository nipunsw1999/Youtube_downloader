import tkinter as tk
from pytube import YouTube
import customtkinter

# Global variable to hold the currently downloading video
current_video = None

def startDownload(option):
    global current_video
    
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "highQuality":
            video = ytObject.streams.get_highest_resolution()
        elif option == "lowQuality":
            video = ytObject.streams.get_lowest_resolution()
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
        else:
            return
        
        current_video = video  # Store the current video being downloaded
        
        title.configure(text=ytObject.title, text_color="white")
        finishedLabel.configure(text="")
        video.download()
        finishedLabel.configure(text="Downloaded !!!", text_color="green")
    
    except Exception as e:
        finishedLabel.configure(text="Download Error: " + str(e), text_color="red")
        
def cancelDownload():
    global current_video
    if current_video:
        current_video.cancel()
        finishedLabel.configure(text="Download Canceled", text_color="red")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage_of_complete = bytes_download / total_size * 100
    per = str(int(percentage_of_complete))
    progress.configure(text=per + '%')
    progress.update()
    
    # Update progress Bar design
    progressbar.set(float(percentage_of_complete) / 100)

# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


# App frame
app_icon = "C:\\Users\\Nipun Weerasinghe\\Desktop\\Python\\Youtube\\icon.ico"
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Link Download")
# set the window title logo
app.iconbitmap(app_icon)


# Adding UI elements
title = customtkinter.CTkLabel(app, text="Paste here your Youtube link", width=200, height=50, font=("cursive", 28))
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=50, textvariable=url_var)
link.pack()

# Finished download msg
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()

# Progress percentage
progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

# Progress bar
progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

# Download high quality video
download_hq = customtkinter.CTkButton(app, text="Download High Quality Video", command=lambda:startDownload("highQuality"))
download_hq.pack(padx=10, pady=10)

# Download low quality video
download_lq = customtkinter.CTkButton(app, text="Download Low Quality", command=lambda:startDownload("lowQuality"))
download_lq.pack(padx=10, pady=10)

# Download mp3
download_mp3 = customtkinter.CTkButton(app, text="Download mp3", command=lambda:startDownload("audio"))
download_mp3.pack(padx=10, pady=10)

# Cancel download button
cancel_button = customtkinter.CTkButton(app, text="Cancel Download", command=cancelDownload)
cancel_button.pack(padx=10, pady=10)

# Run app
app.mainloop()
