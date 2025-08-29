import time
import os
import queue
import pystray
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image, ImageDraw
from win10toast import ToastNotifier

#"📄 File Created"
#"✏ File Modified"
#"📦 File Moved"
#"🗑 File Deleted"

#   →

# r"C:\Users\user\Desktop\Test Folder"

toaster = ToastNotifier()

notification_queue = queue.Queue()

def notification_worker():
    while True:
        title, message = notification_queue.get()
        toaster.show_toast(
            title,
            message,
            duration=5,
            threaded=True
        )
        while toaster.notification_active():
            time.sleep(0.1)
        notification_queue.task_done()

threading.Thread(target=notification_worker, daemon=True).start()

def send_notification(title, message):
    notification_queue.put((title, message))

class WatchHandler(FileSystemEventHandler):
    def on_created(self, event):
        send_notification("📄 File Created", f"{event.src_path}")
    
    def on_deleted(self, event):
        send_notification("🗑 File Deleted", f"{event.src_path}")

    def on_modified(self, event):
        send_notification("✏ File Modified", f"{event.src_path}")

    def on_moved(self, event):
        send_notification("📦 File Moved", f"{event.src_path} → {event.dest_path}")

WATCHED_FOLDER = [
    r"C:\Users\user\Desktop\Test Folder",
    r"C:\Users\user\Desktop\Test Folder-2"
]

def start_watching():
    my_guard = WatchHandler()
    my_observer = Observer()

    for folders in WATCHED_FOLDER:
        if os.path.exists(folders):
            my_observer.schedule(my_guard, folders, recursive=True)
    
    my_observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()

def create_image():
    image = Image.new('RGB', (64, 64), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw.ellipse((8, 8, 56, 56), fill=(0, 255, 0), outline=(0, 0, 0), width=2)

    return image

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def final_setup():
    icon = pystray.Icon("Folder Monitor", create_image(), "ProTech Folder Guard")
    icon.menu = pystray.Menu(pystray.MenuItem("Quit", on_quit))

    threading.Thread(target=start_watching, daemon=True).start()

    icon.run()


if __name__ == "__main__":
    final_setup()