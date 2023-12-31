# PyTubeDL - Online Video Downloader

![alt text](https://i.ibb.co/WDP0YnF/Py-Tube-DL-300x300.png)

**PyTubeDL** is a versatile and graphical online video downloader interface written in pure Python. It provides an easy-to-use way to download videos from various online sources, including YouTube and Vimeo (more coming soon). This tool allows you to download single videos, entire playlists from supported platforms. Additionally, it will soon offer conversion options for downloading videos in various formats, making it a handy tool for anyone looking to save online content for offline viewing.

Great examples of how you can use this tool:
- Downloading a song playlist or album from artist channel
- Downloading videos for archival purposes
- Video download automation

Hope you find this useful! 

## Features

- Download videos from multiple online sources:
- YouTube (single video or playlist)
- Vimeo (single video)
- Simple and intuitive graphical user interface (GUI) for easy operation.
- Command-line interface (CLI) for advanced users who prefer scripting and automation.

## Requirements

- Python 3.x
- The following Python libraries:
- pytube
- vimeo_downloader
- customtkinter

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```

## How to Use

### Graphical User Interface (GUI)

1. Run the script with no command-line arguments:

   ```bash
   python pytubedl.py
   ```

2. Select the download type from the dropdown list, including YouTube single video, playlist, or Vimeo video.

3. Enter the URL of the video, playlist, or Vimeo video you want to download.

4. Specify the output folder where you want to save the downloaded content.

5. Click the "Download" button to initiate the download.

### Command-Line Interface (CLI)

You can also use the CLI version of PyTubeDL for advanced users:

```bash
python pytubedl.py -i [URL] -o [output_folder]
```

Replace `[URL]` with the URL of the video you want to download and `[output_folder]` with the path to the output folder where you want to save the downloaded content.

## Author

- **Kyle Munday**

## Acknowledgments

Special thanks to:

- Nick Finaco for the pytube library.
- Yash Rathi for the vimeo-downloader library.
- Tom Schimansky for the CustomTkinter library.
- Fabrice Bellard and contributors for ffmpeg
 
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
