import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video(link, quality):
    try:
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        if quality == "high":
            stream = yt.streams.get_highest_resolution()
        elif quality == "low":
            stream = yt.streams.get_lowest_resolution()
        elif quality == "audio":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            messagebox.showerror("Error", "Invalid quality selected!")
            return
        
        # تحميل الفيديو
        stream.download()
        messagebox.showinfo("Success", f"Video downloaded successfully as {quality} quality!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

def download_high():
    link = entry.get()
    if link:
        download_video(link, "high")
    else:
        messagebox.showwarning("Warning", "Please enter a YouTube link!")

def download_low():
    link = entry.get()
    if link:
        download_video(link, "low")
    else:
        messagebox.showwarning("Warning", "Please enter a YouTube link!")

def download_audio():
    link = entry.get()
    if link:
        download_video(link, "audio")
    else:
        messagebox.showwarning("Warning", "Please enter a YouTube link!")

# إنشاء واجهة التطبيق
root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="Enter YouTube Link:").pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Download High Quality", command=download_high).pack(pady=5)
tk.Button(root, text="Download Low Quality", command=download_low).pack(pady=5)
tk.Button(root, text="Download Audio Only", command=download_audio).pack(pady=5)

root.mainloop()