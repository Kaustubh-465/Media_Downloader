import tkinter as tk
from tkinter import messagebox
import yt_dlp
import threading
import os

class MediaDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Media Downloader")
        self.root.geometry("500x250")
        
      
        self.label = tk.Label(root, text="Enter Video Link:", font=("Arial", 12))
        self.label.pack(pady=10)
        
     
        self.url_entry = tk.Entry(root, width=50, font=("Arial", 10))
        self.url_entry.pack(pady=5)
        
  
        self.download_btn = tk.Button(root, text="Download Media", command=self.start_download_thread, 
                                      bg="green", fg="white", font=("Arial", 10, "bold"))
        self.download_btn.pack(pady=20)
        

        self.status_label = tk.Label(root, text="Ready", fg="blue")
        self.status_label.pack(pady=10)

    def start_download_thread(self):
  
        link = self.url_entry.get()
        if not link:
            messagebox.showwarning("Error", "Please paste a link first!")
            return
            
        self.status_label.config(text="⏳ Downloading... Please wait.")
        self.download_btn.config(state=tk.DISABLED)
        
   
        thread = threading.Thread(target=self.download_media, args=(link,))
        thread.start()

    def download_media(self, link):
        try:
   
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': True, 
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
          
            self.update_status("✅ Download Complete!", "green")
            
        except Exception as e:
            self.update_status(f"❌ Error: {str(e)}", "red")
        
        finally:
            self.enable_button()

    def update_status(self, message, color):
        self.status_label.config(text=message, fg=color)
        
    def enable_button(self):
        self.download_btn.config(state=tk.NORMAL)

# --- Main Execution ---
if __name__ == "__main__":
 
    try:
        import yt_dlp
    except ImportError:
        print("Please run: pip install yt-dlp")
        exit()

    root = tk.Tk()
    app = MediaDownloaderApp(root)

    root.mainloop()
