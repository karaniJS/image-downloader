# 🖼️ Image Downloader

A simple Python script to download a series of `.png` images from a specific URL and save them into a local folder.

This script is useful for automating the download of sequential image files from a structured directory, such as a content delivery website or media archive.

## 🔧 Features

- Automatically creates a folder named `downloads` (if it doesn't exist)
- Downloads images from a specified base URL
- Handles connection errors gracefully
- Prints download status for each image

## 📦 Requirements

- Python 3.x
- `requests` library  
  You can install it using pip:

  ```bash
  pip install requests

## ▶️ Usage
- Save the script as image_downloader.py
- Run the script using Python:

  ```bash
  python image_downloader.py

 Images will be saved in the downloads folder located in the same directory as the script.

 ## 📁 Output Example
  ```bash

downloads/
├── 1.png
├── 2.png
├── ...
└── 20.png
