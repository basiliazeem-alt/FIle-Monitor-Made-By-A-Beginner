# 🛡️ ProTech Folder Guard

A Python tool that monitors selected folders in real-time and shows Windows desktop notifications whenever files are created, modified, moved, or deleted.  
It runs in the system tray with a simple icon, making it easy to keep track of changes happening in important folders.

---

## ✨ Features
- 📄 **File Created** – Notifies when a new file appears.  
- ✏ **File Modified** – Notifies when an existing file is changed.  
- 📦 **File Moved** – Notifies when a file is moved or renamed.  
- 🗑 **File Deleted** – Notifies when a file is deleted.  
- 🖥 **System Tray Support** – Runs in the tray with an option to quit anytime.  
- 🔔 **Windows Toast Notifications** – Uses native Windows notifications.

---

## 📂 Folders Being Watched
By default, the script is set to watch:
```python
WATCHED_FOLDER = [
    r"C:\Users\user\Desktop\Sample Folder_1",
    r"C:\Users\user\Desktop\Sample Folder_2"
]
