# Ramadan Adhan Automation Tool
This Python script automates playing the adhan and Islamic media files at specific times during Ramadan using VLC Media Player and Windows Task Scheduler. It was created to support iftar events by scheduling media playback on a laptop connected to HDMI screens.

## Requirements
- **Python 3**: Install from [python.org](https://www.python.org/).
- **VLC Media Player**: Download from [videolan.org](https://www.videolan.org/).
- **Windows OS**: Uses Task Scheduler for scheduling.
- Media files: Place your media files in a folder.

## Setup and Usage
1. **Get the Script**: Clone or download from GitHub:
   ```bash
   git clone https://github.com/Nouraldeen504/ramadan-adhan-automation.git
   cd ramadan-adhan-automation
   ```

2. **Configure Paths**: Edit iftar_scheduler.py:
   * Set vlc_path to your VLC executable (e.g., C:\Program Files\VideoLAN\VLC\vlc.exe).
   * Set media_folder to where your media files are (e.g., C:\Users\Nuri\Desktop\iftar\media).

3. **Set Schedule**: Update adhan_times with your Ramadan dates and times in "MM/DD/YYYY", "HH:MM" (24-hour) format:
   ```python
   adhan_times = [("03/01/2025", "18:00"), ("03/02/2025", "18:01"), ("03/03/2025", "18:02")]
   ```

4. **Run It**: Open Command Prompt as Administrator, navigate to the folder, and run:
   ```bash
   python iftar_scheduler.py
   ```

   This creates a playlist (iftar_playlist.m3u) and schedules tasks named like Iftar_Adhan_03-01-2025.

## Testing
* Verify in Task Scheduler under Task Scheduler Library.
* Manually trigger a task:
  ```bash
  schtasks /run /tn "Iftar_Adhan_03-01-2025"
  ```
* Ensure the laptop is on and HDMI-connected at the scheduled times.

## Notes
* Dates must be "MM/DD/YYYY" for Windows.
* VLC plays files in full-screen and exits automatically.
* Customize paths and times as needed.

## License
Free to use or modify—no license specified.