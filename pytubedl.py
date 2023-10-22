"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠐⠒⠈⠉⠁⠀⠀⠉⠉⠁⠒⠂⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠊⠁⠀⠀⠀⠀⣀⣤⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠈⠑⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⢀⣤⣶⣿⡟⡡⡐⠦⠆⠈⠻⢷⣦⡄⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⠊⢀⡀⠀⠻⣠⣶⣿⣿⡇⠈⠐⠈⠀⣠⣤⣄⠀⠀⠘⣿⣄⠀⠀⢀⠔⢄⠀⠀⠱⡀⠀⠀⠀⠀
    ⠀⠀⠀⡐⠁⠒⠅⡵⢂⣼⣿⡅⡻⠉⣠⡄⠀⠀⠸⣿⣭⣿⠟⠀⠀⠙⠛⠿⣶⡀⠑⠀⠀⠀⠀⠈⢆⠀⠀⠀
    ⠀⠀⡐⠀⠀⠀⠈⢠⣾⣏⠌⡿⢀⣤⣿⣗⠤⠀⡀⠈⠉⣁⣀⣀⡀⣤⢉⢗⣿⠇⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀
    ⠀⢰⠁⠀⣠⠀⢀⣿⣿⡏⠆⣠⣿⢋⣼⣿⣦⣤⣵⡤⠄⠉⠛⠛⠿⢿⣿⣿⣿⣄⠀⠀⠀⠷⠀⠀⠀⠈⡄⠀
    ⠀⠇⠀⠈⠒⠁⢸⣿⢹⣨⣴⣿⢡⣿⠏⠀⠀⠉⠙⠻⠿⠿⠿⠿⠿⠿⠛⢻⣿⣿⡆⢀⠤⡀⠀⠀⠀⠀⢱⠀
    ⢰⠀⠀⠀⠀⠀⢸⣿⣾⢉⣸⣿⠈⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠙⠁⠈⠋⠁⠀⠀⠀⠀⠈⠀
    ⢸⠀⠀⠀⠀⠀⠘⣿⡿⠞⡟⢿⣮⡈⠻⢿⣶⣤⣠⣾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠿⠿⣶⣄⠀⠀⠀⠂
    ⠘⡀⠀⠀⠀⠀⠀⠘⢿⣦⡁⣈⡛⢿⣶⣆⠐⠙⢿⣷⡊⠉⠉⡭⢍⡉⠉⠀⠀⠀⠉⠉⠉⠐⡌⣿⡆⠀⢠⠀
    ⠀⢇⠀⠀⠀⡀⡀⠀⠀⠙⠿⣾⣟⠷⢈⡻⣷⡄⠀⢹⣿⡀⠀⡇⠀⠈⠑⠢⢄⠀⠀⠀⠀⠀⠀⣿⡇⠀⡜⠀
    ⠀⠘⡄⠀⠀⢈⡁⠀⠀⠀⠀⠈⢻⣧⡼⢻⣿⣿⠀⠈⣿⣷⠀⡇⠀⠀⠀⠀⠀⠈⠒⠤⡀⠀⠀⣿⡇⢠⠁⠀
    ⠀⠀⠰⡀⠀⠈⣁⣀⣤⣤⣤⣤⣤⣿⡿⢇⠁⣿⠀⣼⣿⠛⠀⡇⠀⠀⠀⠀⠀⣀⠠⠒⠁⠀⠀⣿⣧⠃⠀⠀
    ⠀⠀⢀⣴⣾⣿⡟⣫⡉⢭⣴⣦⣼⣿⣾⡿⢰⣿⢌⣾⡟⠇⠀⡇⠀⢀⠠⠐⠈⠀⠀⠀⠀⣠⣦⣿⣿⠿⣿⡧
    ⠀⢀⣿⡟⣘⠉⠜⠻⣿⠛⠛⢉⠁⢈⢕⢠⣿⢇⣾⣿⣤⣤⣠⣷⣨⣀⣀⣀⣀⣀⣀⣠⣔⣿⡇⠿⠁⣼⡿⠁
    ⠀⠘⣿⡗⢝⡛⠀⢾⣛⠛⣃⢄⠌⣀⣵⡿⣫⣿⠏⣉⣻⡿⠿⠻⠿⠟⢛⣛⣛⢛⣛⣛⠻⠿⣠⣶⣼⡿⠁⠀
    ⣠⠐⢻⡿⣶⣤⣌⣁⣀⣤⣬⣷⡾⣿⡿⠞⠛⠻⢷⣶⣬⣥⣤⣿⣿⣦⣬⣭⣥⣬⣭⣭⣤⣴⡿⠋⢻⠓⠢⡄
    ⠈⠁⠒⠂⠀⠭⠭⠭⠻⠛⠛⠒⢒⣐⣀⡀⠐⠒⠒⠒⠒⠛⠙⠛⢛⣋⢉⣉⡉⠋⠉⠩⠭⠤⠤⠀⠒⠒⠈⠁
    
    # PyTubeDL 
    #
    # DESCRIPTION
    # Versatile Graphical Online Video Downloader Interface written in pure Python
    #
    # VERSION
    # v1.0.0.1
    #
    # Written By: Kyle Munday
    # Made with <3 from Australia

    # THANKS TO:
    # Nick Finaco for the pytube library
    # Yash Rathi for the vimeo-downloader library

"""
""" 
    TODO LOG:
    - [ ] Would like conversion options - MP4, WMV, FLV, AVI, WebM, MOV, OGG, MP3, WAV, FLAC
    - [ ] Would like to add more content sources
    - [X] Write a better way to validate URLS 
    - [] Extended support for other sources: Dailymotion, Facebook, Instagram, Twitter, TikTok?, TED?, Metacafe?, Twitch?
"""
"""
    TESTING LOG:

    - [X] UI Vimeo downloads work
    - [X] UI Single YT Videos download properly
    - [X] UI Playlists work
    - [ ] CLI Vimeo downloads work
    - [ ] CLI Single YT Videos download properly
    - [ ] CLI Playlists work
    - [X] File conversions work

"""

###########################################################
# LIBRARIES
###########################################################

import os, re, argparse, shutil, zipfile, subprocess
import customtkinter as ctk
from tkinter import ttk, filedialog
from pytube import YouTube, Playlist
from vimeo_downloader import Vimeo


# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("Dark")        
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("green")    

###########################################################
# CONSTANT VARIABLES
###########################################################

DOWNLOAD_OPTIONS_LIST = ["YouTube - Single Video", 
                         "YouTube - Playlist", 
                         "Vimeo - Single Video"]

FILE_OPTIONS_LIST = ["MP4", 
                     "WMV", 
                     "FLV", 
                     "AVI", 
                     "WebM", 
                     "MOV", 
                     "OGG", 
                     "MP3", 
                     "WAV", 
                     "FLAC"]

CONCAT_LENGTH = 20

###########################################################
# FUNCTIONS RELATED TO FILE HANDLING
###########################################################

# File conversions
def convert_file(input, output_file_type):
    output_file_type = output_file_type.lower()
    if output_file_type == "mp4":
        command = 'ffmpeg -y -i "{}" -c:v libx264 -c:a aac "{}.mp4"'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "wmv":
        command = 'ffmpeg -i "{}" -c:v wmv2 -c:a wmav2 "{}.wmv"'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "flv":
        command = 'ffmpeg -i "{}" -c:v flv -c:a mp3 "{}.flv"'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "avi":
        command = 'ffmpeg -i "{}" -c:v mpeg4 -c:a mp3 "{}.avi"'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "webm":
        command = 'ffmpeg -i "{}" -c:v libvpx-vp9 -c:a libopus "{}.webm"'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "mov":
        command = 'ffmpeg -i "{}" -c:v libx264 -c:a aac "{}.mov"'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "ogg":
        command = 'ffmpeg -i {} -c:a libvorbis -q:a 4 {}.ogg"'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "mp3":
        command = 'ffmpeg -i {} -c:a libmp3lame -q:a 2 {}.mp3'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "wav":
        command = 'ffmpeg -i {} -c:a pcm_s16le {}.wav'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    elif output_file_type == "flac":
        command = 'ffmpeg -i {} -c:a flac {}.flac'.format(input, input)
        subprocess.run(command, shell=True, check=True)
    else:
        status_label.configure(text="Error: " + "Invalid filetype specified.")
    
# Sanitize file names for file system limit, and remove disallowed characters
def sanitize_filename(filename):
    # Replace spaces with underscores
    filename = filename.replace(" ", "_")

    # Remove invalid characters
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, "")

    # Limit the length of the filename
    max_filename_length = 255  # Adjust based on the file system's limit
    filename = filename[:max_filename_length]

    return filename

###########################################################
# FUNCTIONS RELATED TO VIDEO DOWNLOADING
###########################################################

# Validate URL without knowing what download method is being used
def validate_url(url_input):
    # Add a try/except block for generic status code
    youtube_regex = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.*"
    youtube_short_regex = r"^(https?://)?(www\.)?(youtu\.be)/.*"
    playlist_regex = r"^(https?://)?(www\.)?(youtube\.com/playlist\?list=).*"
    shorts_regex = r"^(https?://)?(www\.)?(youtube\.com/shorts/).*"
    vimeo_regex = r"^(https?://)?(www\.)?(vimeo\.com)/.*"
    
    if re.match(youtube_regex, url_input) or re.match(youtube_short_regex, url_input):
        return "YouTube - Single Video"
    elif re.match(shorts_regex, url_input):
        return "YouTube - Single Video"
    elif re.match(playlist_regex, url_input):
        return "YouTube - Playlist"
    elif re.match(vimeo_regex, url_input):
        return "Vimeo - Single Video"  
    else:
        return None
    
# Single YT Video Method
def download_single_video(video_url, output_path, extension, index):
    output_path = output_path.replace("/", "\\")
    try:
        if validate_url(video_url) != None:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            sanitized_title = sanitize_filename(yt.title)  # Sanitize the video title

            # Only format numbers if it is a playlist
            if index != None:
                 # Check if index is a single digit, and if so, add a leading zero
                if 0 <= index < 10:
                    index = f'0{index}'
                else:
                    index = str(index)
                sanitized_title = "{} - {}".format(index, sanitized_title)

            stream.download(output_path, sanitized_title)
            status_label.configure(text=f"Downloaded: {sanitized_title[:CONCAT_LENGTH]+"..."}")

            path = os.path.join(output_path, sanitized_title)
            convert_file(path, extension)
            status_label.configure(text=f"Converted: {sanitized_title[:CONCAT_LENGTH]+"..."}")
            if os.path.exists(path):
                os.remove(path)

    except Exception as e:
        status_label.configure(text=f"Error: {e}")

# YT Playlist Method
def download_playlist(playlist_url, output_path, extension):
    try:
        if validate_url(playlist_url) == None:
            raise ValueError("Wrong format specified")
        pl = Playlist(playlist_url)
        playlist_title = sanitize_filename(pl.title)
        playlist_folder = os.path.join(output_path, playlist_title)
        os.makedirs(playlist_folder, exist_ok=True)
        for index, video in enumerate(pl.videos):
            download_single_video(video.watch_url, playlist_folder, extension, index+1)         
            
        # Zip the folder
        zip_filename = f"{playlist_title}.zip"
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(playlist_folder):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), playlist_folder))

        # Remove the original folder
        shutil.rmtree(playlist_folder)

    except Exception as e:
        status_label.configure(text=f"Error: {e}")

# Vimeo Download Method
def download_vimeo_video(video_url, output_path, extension):
    output_path = output_path.replace("/", "\\")
    try:
        if validate_url(video_url) == None:
            raise ValueError("Wrong format specified")
        vimeo = Vimeo(video_url)
        meta = vimeo.metadata
        streams = vimeo.streams
        best_stream = streams[-1]
        sanitized_title = sanitize_filename(meta.title)  # Sanitize the video title
        best_stream.download(download_directory=output_path, filename=sanitized_title)
        status_label.configure(text=f"Downloaded: {sanitized_title[:CONCAT_LENGTH]+"..."}")

        path = os.path.join(output_path, sanitized_title)
        convert_file(os.path.join(output_path, sanitized_title), extension)
        status_label.configure(text=f"Converted: {sanitized_title[:CONCAT_LENGTH]+"..."}")

        if os.path.exists(path):
            os.remove(path)        
    except Exception as e:
        status_label.configure(text=f"Error: {e}")

###########################################################
# FUNCTIONS RELATED TO GUI OPERATIONS
###########################################################

def browse_folder():
    # Function to open a file dialog for selecting the output folder
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def hide_status_label():
    # Function to hide the status label
    status_label.configure(text="")

def download():
    # Download function
    output_path = folder_entry.get()
    selected_option = download_option.get()
    url = video_entry.get()
    output_file_type = file_option.get()

    hide_status_label()

    if not url:
        status_label.configure(text="Error: Missing input")
    elif not output_path:
        status_label.configure(text="Error: No output folder specified")
    else:
        if selected_option == "YouTube - Single Video":
            download_single_video(url, output_path, output_file_type, None)
        elif selected_option == "YouTube - Playlist":
            download_playlist(url, output_path, output_file_type)
        elif selected_option == "Vimeo - Single Video":
            download_vimeo_video(url, output_path, output_file_type)

# Create App class
class App(ctk.CTk):
        # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of our window to "App"
        self.title("PyTubeDL")    

        # Set Window Icon
        self.iconbitmap("icon.ico")

        # Set the initial window size
        self.geometry("300x200")

        # Set minimum window size
        self.minsize(600, 400)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame = ctk.CTkFrame(self)
        self.frame.grid(column=0, row=0, padx=30, pady=15, sticky=(ctk.N, ctk.W, ctk.E, ctk.S))

        for i in range(11):
            self.frame.grid_rowconfigure(i, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.download_label = ctk.CTkLabel(self.frame, text="Download Type:")
        self.download_label.grid(column=0, row=0, sticky=ctk.W)

        global download_option
        download_option = ctk.CTkOptionMenu(self.frame, values=DOWNLOAD_OPTIONS_LIST)
        download_option.set("YouTube - Single Video")
        download_option.grid(column=0, row=1, sticky="ew")

        self.video_label = ctk.CTkLabel(self.frame, text="Input URL:")
        self.video_label.grid(column=0, row=2, sticky=ctk.W)

        global video_entry
        video_entry = ctk.CTkEntry(self.frame)
        video_entry.grid(column=0, row=3, sticky="ew")

        self.folder_label = ctk.CTkLabel(self.frame, text="Output Folder:")
        self.folder_label.grid(column=0, row=4, sticky=ctk.W)

        global folder_entry
        folder_entry = ctk.CTkEntry(self.frame)
        folder_entry.grid(column=0, row=5, sticky="ew")

        self.browse_button = ctk.CTkButton(self.frame, text="Browse", width=30, command=browse_folder)
        self.browse_button.grid(column=1, row=5, sticky="ew")

        self.file_label = ctk.CTkLabel(self.frame, text="Output Format:")
        self.file_label.grid(column=0, row=6, sticky=ctk.W)

        global file_option
        file_option = ctk.CTkOptionMenu(self.frame, values=FILE_OPTIONS_LIST)
        file_option.set("MP4")
        file_option.grid(column=0, row=7, sticky="ew")

        self.download_button = ctk.CTkButton(self.frame, text="Download", command=download)
        self.download_button.grid(column=0, row=8)

        global status_label
        status_label = ctk.CTkLabel(self.frame, text="")
        status_label.grid(column=0, row=9, columnspan=2, sticky="ew")

###########################################################
# FUNCTIONS RELATED TO COMMAND LINE INTERFACE
###########################################################

def cli():
    parser = argparse.ArgumentParser(description="Download online video content through a CLI.")
    parser.add_argument("-i", "--input", help="Specify a URL to download content from.")
    parser.add_argument("-o", "--output", help="Specify the output folder.")
    parser.add_argument("-c", "--convert", help="Specify the file extension to convert to (MP4, WMV, FLV, AVI, WebM, MOV, OGG, MP3, WAV, FLAC).")

    args = parser.parse_args()
    
    # Both input and output arguments are provided.
    if args.input and args.output:
        validated_url = validate_url(args.input)
        if validated_url != None:
            download_method = validated_url
            if download_method == "YouTube - Single Video":
                download_single_video(video_url=args.input, output_path=args.output, extension = args.convert)
            elif download_method == "YouTube - Playlist":
                download_playlist(playlist_url=args.input, output_path=args.output, extension = args.convert)
            elif download_method == "Vimeo - Single Video":
                download_vimeo_video(video_url=args.input, output_path=args.output, extension = args.convert)
        else:
            # URL was not validated and returned None
            print("Invalid URL format.")
    elif args.input and not args.output:
        # Only input was provided
        print("Please specify an output path.")
    elif not args.input and args.output:
        # Only output was provided
        print("Please specify a URL to download.")

###########################################################
# RUN THE PROGRAM
###########################################################

if __name__ == "__main__":
    args = cli()
    app = App()
    if args is not None:
        #gui()
        app.mainloop()
    else:
        #gui()
        app.mainloop()