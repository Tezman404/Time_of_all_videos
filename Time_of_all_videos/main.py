import os
import cv2
import platform
from tqdm import tqdm
from collections import defaultdict


def get_video_info(directory):
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm'}
    total_duration = 0
    video_count = 0
    formats = defaultdict(int)

    for root, _, files in os.walk(directory):
        for file in tqdm(files, desc=f"Scanning {root}"):
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()

            if file_ext in video_extensions:
                video_count += 1
                formats[file_ext] += 1

                cap = cv2.VideoCapture(file_path)
                if cap.isOpened():
                    fps = cap.get(cv2.CAP_PROP_FPS)
                    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                    duration = frame_count / fps if fps > 0 else 0
                    total_duration += duration
                cap.release()

    return video_count, total_duration, dict(formats)


def main():
    system_os = platform.system()
    print(f"Detected OS: {system_os}")

    folder_path = input("Enter the folder path: ").strip('"')

    if not os.path.exists(folder_path):
        print("❌ The provided path is invalid. Please check and try again.")
        return

    video_count, total_duration, formats = get_video_info(folder_path)

    hours = int(total_duration // 3600)
    minutes = int((total_duration % 3600) // 60)

    print("\n--- Scan Results ---")
    print(f"📂 Total videos: {video_count}")
    print(f"⏳ Total duration: {hours} hours and {minutes} minutes")
    print(f"🎥 Video formats found: {formats}")


if __name__ == "__main__":
    main()
