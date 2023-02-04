import os
import stat
import xbmcaddon
import xbmcvfs

Get the path of the add-on and the location to copy the file to
src = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'rclone-android-21-armv7a')
loc = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/rclone-android-21-armv7a")

Only copy and make the file executable if it doesn't already exist
if not xbmcvfs.exists(loc):
xbmcvfs.copy(src, loc)
st = os.stat(loc)
os.chmod(loc, st.st_mode | stat.S_IEXEC)

Get the locations of the config file, pid file, and log file
loc2 = xbmcvfs.translatePath("special://masterprofile/rclone.conf")
pidfile = xbmcvfs.translatePath("special://temp/librclone.pid")
logfile = xbmcvfs.translatePath("special://temp/librclone.log")
cachepath = xbmcvfs.translatePath("special://temp")

Run the copied file with the specified arguments
os.popen(f"{loc} serve webdav <your remote>: --addr :23457 --config {loc2} --log-file={logfile} --dir-cache-time 2400h --poll-interval 10m")

Get the user-specified options
check_interval = int(xbmcaddon.Addon().getSetting("check_interval"))
cache_time = int(xbmcaddon.addon.Addon().getSetting("cache_time"))
folder_paths = xbmcaddon.Addon().getSetting("folder_paths") # new variable to store multiple folder paths

Split the folder paths string into a list of paths
folder_paths = folder_paths.split(',')

Iterate over each folder path and check if it exists
for folder_path in folder_paths:
# Translate the path to the correct format
folder_path = xbmcvfs.translatePath(folder_path)
# Check if the specified folder exists
if xbmcvfs.exists(folder_path):
# Use xbmc.scanForContent to check for new files in the folder with fast listing
xbmc.scanForContent(folder_path, useFastScan = True)
else:
# Display an error message if the folder does not exist
xbmc.executebuiltin("Notification(Error, The specified folder does not exist)")

Call update_library.py script
os.system("python3 update_library.py")

Call auto_update_kodi_library.py script
os.system("python3 auto_update_kodi_library.py")