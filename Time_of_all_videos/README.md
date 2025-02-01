# Video Metadata Scanner

This Python script scans a given folder and extracts information about all video files inside. It calculates:
- The **total number of videos**.
- The **total duration** (in hours and minutes).
- The **formats** of the videos found.

## 🚀 Features
✔ Detects **total video count, duration, and formats**  
✔ Supports multiple **video formats** (`.mp4`, `.avi`, `.mkv`, `.mov`, `.flv`, `.wmv`, `.webm`)  
✔ Works on **Windows, macOS, and Linux**  
✔ Displays **progress bar** for large directories  

## 📦 Installation
First, install the required dependencies:
```bash
pip install -r requirements.txt
```


## 🔧 Usage
```bash
python main.py
```


## 🖥️ Example Output
```
Detected OS: Windows
Enter the folder path: D:\Videos

Scanning D:\Videos\Movies: 100%|██████████| 10/10 [00:02<00:00, 4.91it/s]
Scanning D:\Videos\TV Shows: 100%|██████████| 15/15 [00:03<00:00, 5.23it/s]

--- Scan Results ---
📂 Total videos: 25
⏳ Total duration: 5 hours and 42 minutes
🎥 Video formats found: {'.mp4': 20, '.mkv': 5}

```
