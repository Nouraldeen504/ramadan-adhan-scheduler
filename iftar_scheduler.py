import os
import subprocess

adhan_times = [
    ("03/04/2025", "10:49"),  # Must be in american format (MM/DD/YYYY)
    #("03/04/2025", "14:01"),
    # ...
]

vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
media_folder = r"C:\Users\Nuri\Desktop\iftar\media"
playlist_path = os.path.join(media_folder, "iftar_playlist.m3u")

def create_playlist():
    try:
        with open(playlist_path, "w") as playlist:
            playlist.write(f"{media_folder}\\ezan.mp4\n")
            playlist.write(f"{media_folder}\\1.mp4\n")
            playlist.write(f"{media_folder}\\2.mp4\n")
        print(f"Playlist created at: {playlist_path}")
    except Exception as e:
        print(f"Error creating playlist: {e}")


def schedule_tasks():
    for date, time in adhan_times:
        # Use a valid task name (replace / with - or _)
        task_name = f"Iftar_Adhan_{date.replace('/', '-')}"  # e.g., Iftar_Adhan_03-03-2025
        vlc_command = f'"{vlc_path}" "{playlist_path}" --fullscreen --play-and-exit'
        task_command = [
            "schtasks",
            "/create",
            "/tn", task_name,
            "/tr", vlc_command,
            "/sc", "once",
            "/sd", date,
            "/st", time,
            "/f"  # Force overwrite if task already exists
        ]
        try:
            result = subprocess.run(task_command, check=True, capture_output=True, text=True)
            print(f"Scheduled task: {task_name} for {date} at {time}")
            print(f"Command output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to schedule task: {task_name} (Error: {e})")
            print(f"Command attempted: {' '.join(task_command)}")
            print(f"Command output: {e.output}")


if __name__ == "__main__":
    create_playlist()
    schedule_tasks() 