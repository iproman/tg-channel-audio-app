<h1 align="center">Get text for tg audio book channel</h1>
<p align="center">Simple app for converting text to telegram audio book channel.</p>

## Getting Started

### Prerequisites
 - PyQt5
 - pyqt5-tools
 - PyInstaller

*PyQt5 runs app with python. PyInstaller creates exe.*

### Installing Via [GitHub](https://github.com/iproman/tg-channel-audio-app)
```
$ git clone https://github.com/iproman/tg-channel-audio-app.git
$ cd tg-channel-audio-app
```
Then to run it, execute the following in the terminal:
```
$ py index.py
```

## Using the Application
1. Fill inputs with text.
2. Click blue button at the bottom to convert.
    - File `audiobook.txt` will be created on desktop or in app folder.
3. Find the file and use it for publishing in telegram channel.

*Easy.*

## Creating exe
1. Run this code in tg-channel-audio-app folder.
    - Folder will be created with additions and `exe` file.
    ````
    pyinstaller --noconfirm --onedir --windowed  "index.py"
    ````
   - One `exe` file will be created.
   ````
    pyinstaller --noconfirm --onefile --windowed  "index.py"
    ````
2. Go to dist folder.
3. Run file `index.exe`.

*Super easy.*