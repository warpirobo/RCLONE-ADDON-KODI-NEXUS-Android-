import os
import time
import xbmcaddon

Get the user-specified options
folder_path = xbmcaddon.Addon().getSetting("folder_path")
rclone_config = xbmcaddon.Addon().getSetting("rclone_config")
rclone_address = xbmcaddon.Addon().getSetting("rclone_address")
check_interval = int(xbmcaddon.Addon().getSetting("check_interval"))

Get the path of the folder to check for new files
folder_path = xbmcvfs.translatePath(folder_path)

Check if the specified folder exists
if xbmcvfs.exists(folder_path):
# Use xbmc.scanForContent to check for new files in the folder
xbmc.scanForContent(folder_path)
else:
# Display an error message if the folder does not exist
xbmc.executebuiltin("Notification(Error, The specified folder does not exist)")

Run rclone with the specified arguments, using the config file, address, and folder path
os.popen(f"rclone serve webdav {rclone_config}:{folder_path} --addr {rclone_address} --config {rclone_config}")

Get the last modified time of the data source
last_update_time = os.path.getmtime(folder_path)

while True:
# Get the current modified time of the data source
current_update_time = os.path.getmtime(folder_path)
# If the modified time is different from the last recorded time
if current_update_time != last_update_time:
# Update the Kodi library
os.system("xbmc-send -a 'UpdateLibrary(video)'")
# Save the new modified time
last_update_time = current_update_time
# Sleep the script for the specified interval
time.sleep(check_interval)



