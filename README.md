# PyTubeDL - Online Video Downloader

![alt text](https://i.imgur.com/JZABDSym.png)

**PyTubeDL** is a versatile and graphical online video downloader interface written in pure Python. It provides an easy-to-use way to download videos from various online sources, including YouTube and Vimeo. This tool allows you to download single videos, entire playlists, and even entire channels from supported platforms. Additionally, it offers conversion options for downloading videos in various formats, making it a handy tool for anyone looking to save online content for offline viewing.

## Features

- Download videos from multiple online sources:
- YouTube (single video, playlist, and channel)
- Vimeo (single video)
- Simple and intuitive graphical user interface (GUI) for easy operation.
- Command-line interface (CLI) for advanced users who prefer scripting and automation.

## Requirements

- Python 3.x
- The following Python libraries:
- pytube
- vimeo_downloader

You can install these libraries using pip:

```bash
pip install pytube vimeo_downloader
```

## How to Use

### Graphical User Interface (GUI)

1. Run the script with no command-line arguments:

   ```bash
   python main.py
   ```

2. Select the download type from the dropdown list, including YouTube single video, playlist, channel, or Vimeo video.

3. Enter the URL of the video, playlist, channel, or Vimeo video you want to download.

4. Specify the output folder where you want to save the downloaded content.

5. Click the "Download" button to initiate the download.

### Command-Line Interface (CLI)

You can also use the CLI version of PyTubeDL for advanced users:

```bash
python main.py -i [URL] -o [output_folder]
```

Replace `[URL]` with the URL of the video you want to download and `[output_folder]` with the path to the output folder where you want to save the downloaded content.

## Author

- **Kyle Munday**

## Acknowledgments

Special thanks to:

- Nick Finaco for the pytube library.
- Yash Rathi for the vimeo-downloader library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
